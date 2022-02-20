package main

import (
	"flag"
	"fmt"
	"io"
	"io/ioutil"
	"log"
	"os"
	"strings"
	"time"

	"github.com/jlaffaye/ftp"
	"github.com/skorobogatov/input"
)

// - загрузку файла go ftp клиентом на ftp сервер;
// - скачивание файла go ftp клиентом с ftp сервера;
// - создание директории go ftp клиентом на ftp сервере;
// - удаление go ftp клиентом  файла на ftp сервере;
// - получение содержимого директории на ftp сервере с помощью go ftp клиента.

func get(c *ftp.ServerConn, list string) {
	args := strings.Split(list, " ")
	var files []string
	path := "."

	for _, x := range args {
		if strings.HasPrefix(x, "-path=") {
			path = x[6:]
		} else {
			files = append(files, x)
		}
	}

	err := os.Chdir(path)
	if err != nil {
		log.Fatal(err)
	}

	for _, x := range files {
		segments := strings.Split(x, "/")
		filename := segments[len(segments)-1]
		// file, err :=

		res, err := c.Retr(x)
		if err != nil {
			log.Fatal(err)
		}

		defer res.Close()

		outFile, err := os.Create(filename)
		if err != nil {
			log.Fatal(err)
		}

		defer outFile.Close()

		_, err = io.Copy(outFile, res)
		if err != nil {
			log.Fatal(err)
		}
	}
}

func mkdir(c *ftp.ServerConn, path string) {
	err := c.MakeDir(path)
	if err != nil {
		panic(err)
	}
}

func rmdir(c *ftp.ServerConn, path string) {
	err := c.RemoveDir(path)
	if err != nil {
		panic(err)
	}
}

func put(c *ftp.ServerConn, list string) {
	args := strings.Split(list, " ")
	var files []string
	path := "."

	for _, x := range args {
		if strings.HasPrefix(x, "-path=") {
			path = x[6:]
		} else {
			files = append(files, x)
		}
	}

	for _, x := range files {
		file, err := os.Open(x)
		if err != nil {
			panic(err)
		}
		reader := (*os.File)(file)
		err = c.Stor(path+"/"+x, reader)
		if err != nil {
			panic(err)
		}
	}
}

func rm(c *ftp.ServerConn, args string) {
	files := strings.Split(args, " ")
	for _, x := range files {
		err := c.Delete(x)
		if err != nil {
			panic(err)
		}
	}
}

func ls(c *ftp.ServerConn, path string) {
	if path == "" {
		path = "."
	}
	list, err := c.NameList(path)
	if err != nil {
		log.Fatal(err)
		return
	}
	for _, x := range list {
		fmt.Println(x)
	}
}

func get_cmd(c *ftp.ServerConn, cmd string) {
	arg0 := strings.Split(cmd, " ")[0]
	other_args := strings.Join(strings.Split(cmd, " ")[1:], " ")

	switch arg0 {
	case "ls":
		ls(c, other_args)
	case "put":
		put(c, other_args)
	case "get":
		get(c, other_args)
	case "mkdir":
		mkdir(c, other_args)
	case "rm":
		rm(c, other_args)
	case "rmdir":
		rmdir(c, other_args)
	}

}

func parseLines(lines string) (string, string, []string) {
	lns := strings.Split(lines, "\n")
	if !(strings.HasPrefix(lns[0], "user: ") && strings.HasPrefix(lns[1], "pass: ")) {
		log.Fatal("invalid syntax in file with comands")
	}
	return strings.TrimLeft(lns[0], "user: q	"), strings.TrimLeft(lns[1], "pass: "), lns[2:]
}

func main() {
	var protoFile = flag.String("proto", "", "file with comands")
	flag.Parse()

	c, err := ftp.Dial("localhost:2121", ftp.DialWithTimeout(5*time.Second))
	if err != nil {
		log.Fatal(err)
	}

	var user, pass string
	var cmds []string

	if *protoFile != "" {
		lines, err := ioutil.ReadFile(*protoFile)
		if err != nil {
			log.Fatal(err)
		}
		user, pass, cmds = parseLines(string(lines))

	} else {
		user = "lol"
		pass = "kek"
	}
	// err = c.Login("admin", "123456")
	err = c.Login(user, pass)
	if err != nil {
		log.Fatal(err)
	}

	if *protoFile != "" {
		for _, cmd := range cmds {
			if cmd == "quit" {
				break
			}
			get_cmd(c, cmd)
		}
	} else {
		for {
			fmt.Print(">>>")
			cmd := input.Gets()
			if cmd == "quit" {
				break
			}
			get_cmd(c, cmd)
		}
	}
	if err := c.Quit(); err != nil {
		log.Fatal(err)
	}
}
