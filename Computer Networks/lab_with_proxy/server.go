package main

import (
	"encoding/json"
	"flag"
	"fmt"
	"net"
	"os"
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
	Ident string `json:"ident"`
}

func check(s string) bool {
	var sum int
	for _, x := range s {
		sum += int(x)
	}
	return sum%3 == 0
}

func main() {
	var (
		serverAddrStr string
		helpFlag      bool
	)
	flag.StringVar(&serverAddrStr, "addr", "127.0.0.1:6000", "set server IP address and port")
	flag.BoolVar(&helpFlag, "help", false, "print options list")

	if flag.Parse(); helpFlag {
		fmt.Fprint(os.Stderr, "server [options]\n\nAvailable options:\n")
		flag.PrintDefaults()
	} else if serverAddr, err := net.ResolveUDPAddr("udp", serverAddrStr); err != nil {
		fmt.Println("resolving server address", "error", err)
	} else if conn, err := net.ListenUDP("udp", serverAddr); err != nil {
		fmt.Println("creating listening connection", "error", err)
	} else {
		fmt.Println("server listens incoming messages from clients")
		buf := make([]byte, 2000)
		for {
			if bytesRead, addr, err := conn.ReadFromUDP(buf); err != nil {
				fmt.Println("receiving message from client", err)
			} else {
				fmt.Println("new Responce")
				var req Request
				if json.Unmarshal(buf[:bytesRead], &req); err != nil {
					fmt.Println("error, while parsing request: ", err)
				} else {
					fmt.Println("checking ", req.Number)
					devides := check(req.Number)
					var resp Response
					if devides {
						resp.Answer = req.Number + " is divided by 3"
					} else {
						resp.Answer = req.Number + " is not divided by 3"
					}
					resp.Status = "ok"
					resp.Ident = req.Ident
					rawResp, _ := json.Marshal(&resp)
					if _, err = conn.WriteToUDP(rawResp, addr); err != nil {
						fmt.Println("sending message to client", "error", err, "client", addr.String())
					}
				}
			}
		}
	}
}
