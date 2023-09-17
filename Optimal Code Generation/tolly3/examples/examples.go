package examples

import (
	"fmt"

	"github.com/llir/llvm/ir"
	"github.com/llir/llvm/ir/constant"
	"github.com/llir/llvm/ir/types"
)

func Example1() {
	// Create a new LLVM IR module.
	m := ir.NewModule()
	hello := constant.NewCharArrayFromString("Hello, world!\n\x00")
	str := m.NewGlobalDef("str", hello)
	// Add external function declaration of puts.
	puts := m.NewFunc("puts", types.I32, ir.NewParam("", types.NewPointer(types.I8)))
	main := m.NewFunc("main", types.I32)
	entry := main.NewBlock("")
	// Cast *[15]i8 to *i8.
	zero := constant.NewInt(types.I64, 0)
	gep := constant.NewGetElementPtr(hello.Typ, str, zero, zero)
	entry.NewCall(puts, gep)
	entry.NewRet(constant.NewInt(types.I32, 0))
	fmt.Println(m)
}

func Example2() {
	m := ir.NewModule()

	main := m.NewFunc("main", types.I32)
	entry := main.NewBlock("")

	add := entry.NewAdd(
		constant.NewInt(types.I32, 123),
		constant.NewInt(types.I32, 666),
	)
	a := entry.NewAlloca(types.I32)
	entry.NewStore(add, a)
	entry.NewRet(a)

	fmt.Println(m)
}

func Example3() {
	m := ir.NewModule()

	main := m.NewFunc("main", types.I32)
	entry := main.NewBlock("")

	c321 := constant.NewInt(types.I32, 321)
	b := entry.NewAlloca(types.I32)
	entry.NewStore(c321, b)

	add := entry.NewAdd(
		constant.NewInt(types.I32, 123),
		b,
	)
	a := entry.NewAlloca(types.I32)

	entry.NewStore(add, a)

	entry.NewRet(a)

	fmt.Println(m)
}
