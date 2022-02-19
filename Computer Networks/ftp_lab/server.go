package main

import (
	"flag"
	"log"

	filedriver "github.com/goftp/file-driver"
	"github.com/goftp/server"
)

// - поддерживать авторизацию клиента на ftp сервере;
// - передавать клиенту список содержимого заданной директории 				ftp сервера по запросу;
// - позволять клиенту скачивать файлы из заданной директории ftp 			сервера по запросу;
// - позволять клиенту загружать файлы в заданную директорию ftp 			сервера по запросу;
// - позволять клиенту создавать директории на ftp сервере по запросу;
// - позволять клиенту удалять директории на ftp сервере по запросу.

func main() {
	var (
		root = flag.String("root", "rootdir", "Root directory to serve")
		user = flag.String("user", "lol", "Username for login")
		pass = flag.String("pass", "kek", "Password for login")
		port = flag.Int("port", 2121, "Port")
		host = flag.String("host", "localhost", "Host")
	)
	flag.Parse()
	// if *root == "" {
	// 	log.Fatalf("Please set a root to serve with -root")
	// }

	factory := &filedriver.FileDriverFactory{
		RootPath: *root,
		Perm:     server.NewSimplePerm("user", "group"),
	}

	opts := &server.ServerOpts{
		Factory:  factory,
		Port:     *port,
		Hostname: *host,
		Auth:     &server.SimpleAuth{Name: *user, Password: *pass},
	}

	log.Printf("Starting ftp server on %v:%v", opts.Hostname, opts.Port)
	log.Printf("Username %v, Password %v", *user, *pass)
	server := server.NewServer(opts)
	err := server.ListenAndServe()
	if err != nil {
		log.Fatal("Error starting server:", err)
	}
}
