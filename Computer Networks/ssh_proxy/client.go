package main

import (
	"fmt"
	"log"

	"golang.org/x/crypto/ssh"
	// "github.com/skorobogatov/input"
)

func run_ssh_client() {

	username := "aaa"
	password := "000"
	hostname := "127.0.0.1"
	port := "3000"

	// SSH client config
	config := &ssh.ClientConfig{
		User: username,
		Auth: []ssh.AuthMethod{
			ssh.Password(password),
		},
		// Non-production only
		HostKeyCallback: ssh.InsecureIgnoreHostKey(),
	}

	// Connect to host
	client, err := ssh.Dial("tcp", hostname+":"+port, config)
	if err != nil {
		log.Fatal(err)
	}
	defer client.Close()

	// Create sesssion
	sess, err := client.NewSession()
	if err != nil {
		log.Fatal("Failed to create session: ", err)
	}
	defer sess.Close()

	// StdinPipe for commands
	stdin, err := sess.StdinPipe()
	if err != nil {
		log.Fatal(err)
	}

	stdout, err := sess.StdoutPipe()
	if err != nil {
		log.Fatal(err)
	}

	// var myOut io.ReadWriter
	// Enable system stdout
	// sess.Stdout = os.Stdout
	// // sess.Stdout = myOut
	// sess.Stderr = os.Stderr

	// Start remote shell
	err = sess.Shell()
	if err != nil {
		log.Fatal(err)
	}

	for {
		cmd := <-querCh
		log.Println("ssh client: got new cmd: ", cmd)

		_, err = fmt.Fprintf(stdin, "%s\n", cmd)
		if err != nil {
			log.Fatal(err)
		}
		if cmd == "exit" {
			sess.Close()
			break
		}
		// на клиент приходит ответ с сервера, надо его направить в канал responce
		// осталось только вычленить ответ сервера
		bts := make([]byte, 30000)
		num, _ := stdout.Read(bts)
		// myOut.Read(bts)
		// cmd = string(bts)

		log.Println("ssh client: sending responce: ", cmd)
		responceCh <- string(bts[:num])
	}

}
