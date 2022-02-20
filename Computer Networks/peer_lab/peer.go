package main

import (
	"bufio"
	"encoding/json"
	"flag"
	"fmt"
	"net"
	"os"
	"strings"
	"time"
)

type Message struct {
	PeerName string `json:"PeerName"` // имя пира
	Content  string `json:"Content"`  // содержание сообщения
}

var subsList []string
var done bool

func contains(s []string, e string) bool {
	for _, a := range s {
		if a == e {
			return true
		}
	}
	return false
}

func serverPart(myAddrStr, myName string, connToNextPeer *net.UDPConn) {
	if myAddr, err := net.ResolveUDPAddr("udp", myAddrStr); err != nil {
		fmt.Println("resolving server address", "error", err)
	} else if conn, err := net.ListenUDP("udp", myAddr); err != nil {
		fmt.Println("creating listening connection", "error", err)
	} else {
		fmt.Println("im listening from my unknown master")
		buf := make([]byte, 2000)
		// начинаем слушать
		for {
			if bytesRead, _, err := conn.ReadFromUDP(buf); err != nil {
				fmt.Println("receiving message from my master", err)
			} else {
				var newMsg Message
				if json.Unmarshal(buf[:bytesRead], &newMsg); err != nil {
					fmt.Println("error, while parsing request: ", err)
				} else {
					fmt.Println("got new message from:", newMsg.PeerName, "\ncontent:", newMsg.Content)
					// все же удалось принять и распарсить сообщение
					if newMsg.PeerName == myName { // если наше сообщение дошло до нас
						fmt.Println("got my own message. Stop trying to send")
						// надо записать подтверждение в канал
						done = true
						continue
					}
					// если сообщение не наше
					if contains(subsList, newMsg.PeerName) { // проверим, надо ли его выводить на экран
						fmt.Println("************************************")
						fmt.Println("*************************NEW INCOMING MESSAGE FROM",
							newMsg.PeerName, ":", newMsg.Content)
						fmt.Println("************************************")
					}
					// и передали сообщение дальше
					sendMessage(newMsg.Content, newMsg.PeerName, connToNextPeer)
				}
			}
		}
	}
}

func sendMessage(messageText, peerName string, conn *net.UDPConn) {
	msg := Message{peerName, messageText}
	rawMsg, _ := json.Marshal(msg)
	for { // и пытаемся его отправить
		if _, err := conn.Write(rawMsg); err == nil { // если при отправке не произошло ошибки
			fmt.Println("sending message to next peer")
			return // заканчиваем попытки
		}
	}
}

func createConnectionToNextPeer(serverAddrStr string) *net.UDPConn {
	for {
		if serverAddr, err := net.ResolveUDPAddr("udp", serverAddrStr); err != nil {
			fmt.Println("resolving server address", "error", err)
		} else if conn, err := net.DialUDP("udp", nil, serverAddr); err != nil {
			fmt.Println("creating connection to next peer", "error", err)
		} else {
			return conn
		}
	}
}

func main() {
	// создаем флаги
	var (
		myAddrStr   string
		nextAddrStr string
		peerName    string
		helpFlag    bool
	)
	// парсим флаги
	flag.StringVar(&myAddrStr, "my_addr", "", "set self IP address and port")
	flag.StringVar(&nextAddrStr, "next_addr", "", "set next peer IP address and port")
	flag.StringVar(&peerName, "peer_name", "amogus", "your name in network")
	flag.BoolVar(&helpFlag, "help", false, "print options list")

	if flag.Parse(); helpFlag {
		fmt.Fprint(os.Stderr, "server [options]\n\nAvailable options:\n")
		flag.PrintDefaults()
	}
	// инициализируем переменные множественного пользования
	connToNextPeer := createConnectionToNextPeer(nextAddrStr)
	defer connToNextPeer.Close()
	// defer connToNextPeer.Close()
	// запускаем функцию приема сообщений
	go serverPart(myAddrStr, peerName, connToNextPeer)
	// начинаем считывать команды
	command := ""
	subsMaxLen := 20
	subsList = make([]string, subsMaxLen)
	subsListLastIndex := -1
	sc := bufio.NewScanner(os.Stdin)
	for sc.Scan() {
		command = sc.Text()
		words := strings.Split(command, " ")
		if len(words) != 2 {
			fmt.Println("strange command")
			continue
		} else if words[0] == "subscribe" {
			subsListLastIndex++
			if subsListLastIndex > subsMaxLen {
				fmt.Println("too many subscriptions")
				continue
			}
			subsList[subsListLastIndex] = words[1]
		} else if words[0] == "post" {
			done = false
			for !done {
				// отправляем сообщение
				sendMessage(strings.Join(words[1:], " "), peerName, connToNextPeer)
				time.Sleep(30 * time.Millisecond)
			}
		} else {
			fmt.Println("strange command")
		}
	}

}
