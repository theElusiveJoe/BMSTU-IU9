package main

import (
	"flag"
	"fmt"
	"math/rand"
	"net"
	"os"
	"time"

)

type Mode int

const (
	CLIENT_TO_SERVER Mode = 0
	SERVER_TO_CLIENT      = 1
	DUP                   = 2
)

var failures = map[Mode]string{
	CLIENT_TO_SERVER:       "sending message to server",
	SERVER_TO_CLIENT:       "sending message to client",
	CLIENT_TO_SERVER | DUP: "sending duplicate message to server",
	SERVER_TO_CLIENT | DUP: "sending duplicate message to client",
}

var successes = map[Mode]string{
	CLIENT_TO_SERVER:       "client => server",
	SERVER_TO_CLIENT:       "server => client",
	CLIENT_TO_SERVER | DUP: "client => server (duplicate)",
	SERVER_TO_CLIENT | DUP: "server => client (duplicate)",
}

var drops = map[Mode]string{
	CLIENT_TO_SERVER: "dropping message to server",
	SERVER_TO_CLIENT: "dropping message to client",
}

func send(conn *net.UDPConn, addr *net.UDPAddr, data []byte, mode Mode) {
	if _, err := conn.WriteToUDP(data, addr); err != nil {
		fmt.Println(failures[mode], "error", err, "client", addr.String())
	} else {
		fmt.Println(successes[mode], "size", len(data), "client", addr.String())
	}
}

func buggySend(conn *net.UDPConn, addr *net.UDPAddr, data []byte, mode Mode, loss, dup uint) {
	if rand.Intn(100) < int(loss) {
		fmt.Println(drops[mode], "size", len(data), "client", addr.String())
	} else {
		send(conn, addr, data, mode)
		if rand.Intn(100) < int(dup) {
			dataCopy := make([]byte, len(data))
			copy(dataCopy, data)

			duration := time.Duration(rand.Intn(20)) * time.Millisecond
			time.AfterFunc(duration, func() {
				send(conn, addr, dataCopy, mode|DUP)
			})
		}
	}
}

func serveClient(proxyConn, conn *net.UDPConn, addr *net.UDPAddr, loss, dup uint) {
	addrStr := addr.String()
	fmt.Println("serving new client", "client", addrStr)

	buf := make([]byte, 65507)
	for {
		if bytesRead, err := conn.Read(buf); err != nil {
			fmt.Println("receiving message from server", "error", err, "client", addrStr)
		} else {
			buggySend(proxyConn, addr, buf[:bytesRead], SERVER_TO_CLIENT, loss, dup)
		}
	}
}

func proxy(proxyAddr, serverAddr *net.UDPAddr, loss, dup uint) {
	nat := make(map[string]*net.UDPConn)
	if proxyConn, err := net.ListenUDP("udp", proxyAddr); err != nil {
		fmt.Println("creating listening connection for proxy", "error", err)
	} else {
		fmt.Println("proxy listens incoming messages from clients")

		buf := make([]byte, 65507)
		for {
			if bytesRead, clientAddr, err := proxyConn.ReadFromUDP(buf); err != nil {
				fmt.Println("receiving message from client", "error", err)
			} else {
				clientAddrStr := clientAddr.String()
				conn, found := nat[clientAddrStr]
				if !found {
					addr := &net.UDPAddr{IP: proxyAddr.IP, Port: 0}
					if conn, err = net.ListenUDP("udp", addr); err != nil {
						fmt.Println("creating connection to server", "error", err, "client", clientAddrStr)
						continue
					}
					nat[clientAddrStr] = conn
					go serveClient(proxyConn, conn, clientAddr, loss, dup)
				}
				buggySend(conn, serverAddr, buf[:bytesRead], CLIENT_TO_SERVER, loss, dup)
			}
		}
	}
}

func main() {
	var (
		proxyAddrStr, serverAddrStr string
		loss, dup                   uint
		helpFlag                    bool
	)
	flag.StringVar(&proxyAddrStr, "addr", "127.0.0.1:6060", "set proxy IP address and port")
	flag.StringVar(&serverAddrStr, "server", "127.0.0.1:6000", "set server IP address and port")
	flag.UintVar(&loss, "loss", 0, "set datagram loss rate (in %)")
	flag.UintVar(&dup, "dup", 0, "set datagram duplication rate (in %)")
	flag.BoolVar(&helpFlag, "help", false, "print options list")

	if flag.Parse(); helpFlag {
		fmt.Fprint(os.Stderr, "proxy [options]\n\nAvailable options:\n")
		flag.PrintDefaults()
	} else if loss > 100 {
		fmt.Println("loss rate cannot be greater than 100")
	} else if dup > 100 {
		fmt.Println("duplication rate cannot be greater than 100")
	} else if proxyAddr, err := net.ResolveUDPAddr("udp", proxyAddrStr); err != nil {
		fmt.Println("resolving proxy address", "error", err)
	} else if serverAddr, err := net.ResolveUDPAddr("udp", serverAddrStr); err != nil {
		fmt.Println("resolving server address", "error", err)
	} else {
		proxy(proxyAddr, serverAddr, loss, dup)
	}
}
