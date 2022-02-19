package main

import (
	"encoding/json"
	"flag"
	"fmt"
	"net"
	"os"
	"time"
)

type Request struct {
	// само число, которое будем проверять на кратность тройке
	Number string `json:"number"`
	// Идентификатор запроса, целое число от 0 до n
	Ident string `json:"ident"`
}

type Response struct {
	Status string `json:"status"`
	Answer string `json:"answer"`
	Ident  string `json:"ident"`
}

func interact(conn *net.UDPConn, number string, id uint) {
	// создали запрос
	rawReq, _ := json.Marshal(&Request{number, string(id)})
	buf := make([]byte, 2000)
	for {
		t := time.Now()
		t = t.Add(2000 * time.Millisecond)
		conn.SetDeadline(t)
		if _, err := conn.Write(rawReq); err != nil {
			fmt.Println("sending request to server error")
			fmt.Println("sending the request again")
			break
		}
		t = time.Now()
		t = t.Add(2000 * time.Millisecond)
		conn.SetDeadline(t)
		if bytesRead, err := conn.Read(buf); err != nil {
			fmt.Println("server didnt respond repeating...")
			continue
		} else {
			t = t.Add(2 * time.Hour)
			conn.SetDeadline(t)
			var resp Response
			if err := json.Unmarshal(buf[:bytesRead], &resp); err != nil {
				fmt.Println("cannot parse answer")
			} else {
				if resp.Ident == string(id) {
					fmt.Println("********", resp.Answer, "********")
					break
				}
			}
		}
	}
}

func main() {
	var (
		serverAddrStr string
		n             uint
		helpFlag      bool
	)
	flag.StringVar(&serverAddrStr, "server", "127.0.0.1:6000", "set server IP address and port")
	flag.UintVar(&n, "n", 10, "set the number of requests")
	flag.BoolVar(&helpFlag, "help", false, "print options list")

	if flag.Parse(); helpFlag {
		fmt.Fprint(os.Stderr, "client [options]\n\nAvailable options:\n")
		flag.PrintDefaults()
	} else if serverAddr, err := net.ResolveUDPAddr("udp", serverAddrStr); err != nil {
		fmt.Println("resolving server address", "error", err)
	} else if conn, err := net.DialUDP("udp", nil, serverAddr); err != nil {
		fmt.Println("creating connection to server", "error", err)
	} else {
		defer conn.Close()
		for i := uint(0); i < n; i++ {
			fmt.Printf("input your number: ")
			var number string
			fmt.Scanln(&number)
			interact(conn, number, i)
		}
	}
}
