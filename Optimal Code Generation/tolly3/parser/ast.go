// example1.go
package parser

import (
	"fmt"
	"io"
	"os"
	"strconv"

	"github.com/antlr/antlr4/runtime/Go/antlr/v4"
)

type emlangListener struct {
	*MyEmlangListener
}

func CreateAndProcessTree() *emlangListener {
	n, _ := strconv.Atoi(os.Args[1])
	filename := fmt.Sprintf("emlangProgs/prog%d.emlang", n)

	input, _ := antlr.NewFileStream(filename)
	lexer := NewEmlangLexer(input)
	stream := antlr.NewCommonTokenStream(lexer, antlr.TokenDefaultChannel)
	p := NewEmlangParser(stream)

	mylistener := createMyEmlangListener()
	listener := emlangListener{mylistener}
	antlr.ParseTreeWalkerDefault.Walk(&listener, p.Start())

	irfile := fmt.Sprintf("emlangResults/prog%d.ir", n)
	file, err := os.OpenFile(irfile, os.O_CREATE|os.O_WRONLY, 0660)
	if err != nil {
		file, _ = os.Create(irfile)
	}
	io.WriteString(file, listener.Graph())

	dotfile := fmt.Sprintf("emlangResults/prog%d.dot", n)
	file, err = os.OpenFile(dotfile, os.O_CREATE|os.O_WRONLY, 0660)
	if err != nil {
		file, _ = os.Create(dotfile)
	}
	io.WriteString(file, listener.Graph())

	fmt.Println(listener.String())
	return &listener
}
