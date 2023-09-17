package parser

import (
	"fmt"
	"strconv"
)

type Instruction struct {
	typ  string
	args []string
}

func (i *Instruction) String() string {

	switch i.typ {
	case "alloca":
		return fmt.Sprintf("%s = alloca i32", i.args[0])
	case "load":
		return fmt.Sprintf("%s = load i32, i32* %s", i.args[1], i.args[0])
	case "store":
		return fmt.Sprintf("store i32 %s, i32* %s", i.args[0], i.args[1])
	case "br":
		return fmt.Sprintf("br block_%s", i.args[0])
	case "condbr":
		return fmt.Sprintf("br i1 %s, block_%s, block_%s", i.args[0], i.args[1], i.args[2])
	case "icmp":
		return fmt.Sprintf("%s = icmp eq i32 %s, i32 %s", i.args[2], i.args[0], i.args[1])
	case "mul":
		return fmt.Sprintf("%s = mul i32 %s, i32 %s", i.args[2], i.args[0], i.args[1])
	case "add":
		return fmt.Sprintf("%s = add i32 %s, i32 %s", i.args[2], i.args[0], i.args[1])
	case "sub":
		return fmt.Sprintf("%s = sub i32 %s, i32 %s", i.args[2], i.args[0], i.args[1])
	case "ret":
		return fmt.Sprintf("ret %s", i.args[0])
	case "phi":
		return fmt.Sprintf("phi %s <- %v", i.args[0], i.args[1:])
	}
	return fmt.Sprintf("%s", i.typ)
}

type Variable struct {
	name    string
	version int
}

func (v *Variable) String() string {
	return fmt.Sprintf("%s_%d", v.name, v.version)
}

type BB struct {
	blockNum     int
	instructions []*Instruction
	returned     bool
	// тут мапа имя_переменной -> id-vtnrf
	variables  map[string]*Variable
	varcounter int
	phiSet     map[string][]int
}

// ФУНКЦИОНАЛ Ir.block
func (bb *BB) addInstr(instr *Instruction) {
	bb.instructions = append(bb.instructions, instr)
}

func (bb *BB) allocaVariable(name string) *Variable {
	newvar := &Variable{name, 0}
	bb.variables[name] = newvar
	instr := Instruction{"alloca", []string{bb.variables[name].String()}}
	bb.addInstr(&instr)
	return newvar
}

func (bb *BB) createTempVariable() *Variable {
	name := strconv.Itoa(bb.varcounter)
	bb.varcounter++
	newvar := &Variable{"tmp_" + name, 0}
	return newvar
}

func (bb *BB) newBreak(destbb *BB) {
	instr := Instruction{"br", []string{strconv.Itoa(destbb.blockNum)}}
	bb.addInstr(&instr)
}

func (bb *BB) newRet(val string) {
	if bb.isVariableIn(val) {
		tmpvar := bb.createTempVariable()
		newInstr1 := &Instruction{"load", []string{bb.variables[val].String(), tmpvar.name}}
		bb.addInstr(newInstr1)
		newInstr2 := &Instruction{"ret", []string{tmpvar.name}}
		bb.addInstr(newInstr2)

	} else {
		newInstr1 := &Instruction{"ret", []string{val}}
		bb.addInstr(newInstr1)
	}
}

func (bb *BB) newCondBreak(cond *Variable, desta *BB, destb *BB) {
	instr := Instruction{"condbr", []string{
		cond.name, strconv.Itoa(desta.blockNum), strconv.Itoa(destb.blockNum),
	}}
	bb.addInstr(&instr)
}

func (bb *BB) newCompare(arg1 string, arg2 string) *Variable {
	temp := bb.createTempVariable()
	if bb.isVariableIn(arg1) {
		arg1 = bb.variables[arg1].String()
	}
	if bb.isVariableIn(arg2) {
		arg2 = bb.variables[arg2].String()
	}

	instr := Instruction{"icmp", []string{
		arg1, arg2, temp.name,
	}}
	bb.addInstr(&instr)
	return temp
}

// ФУНКЦИОНАЛ строителя CFG

// func (bb *BB) addVariable(name string) {
// 	varr := bb.block.NewAlloca(types.I32)
// 	bb.variables[name] = varr
// }

func (bb *BB) isVariableIn(name string) bool {
	for _, x := range bb.variables {
		if x.name == name {
			return true
		}
	}
	return false
}

func (bb *BB) setVariable(name string, val string) {
	// ВАЖНО
	// переменная - кусок стека
	// само значение мы тут не храним - только ссылку на место в стеке
	// поэтому, не надо беспокоиться из-за областей видимости
	// из любого места, откуда переменную видно
	// по этой ссылке можно поменять ее значение

	bb.variables[name].version++
	if bb.isVariableIn(val) { // если перекидываем из одной переменной в другую
		// создаем временную переменную
		tmpvar := bb.createTempVariable()
		// загружаем значение в первую переменную
		newInstr1 := &Instruction{"load", []string{bb.variables[val].String(), tmpvar.name}}
		bb.addInstr(newInstr1)
		// если строим ssa, то увеличиваем версию переменной
		// перекидываем значение в переменную-назначение
		newInstr2 := &Instruction{"store", []string{tmpvar.name, bb.variables[name].String()}}
		bb.addInstr(newInstr2)

	} else {
		// в нее загружаем значение (а оно только численное может быть)
		newInstr1 := &Instruction{"store", []string{val, bb.variables[name].String()}}
		bb.addInstr(newInstr1)
	}
}

func (bb *BB) setMap(bbParent *BB) {
	for name, val := range bbParent.variables {
		bb.variables[name] = val
	}
}

func (bb *BB) updPhi(ancestor *BB) {
	// функция вызывается уже после передачи области видимости,
	// но до обработки тела блока
	// добавляет "занятые" версии переменных
	// просто собирает все возможные входящие фи
	fmt.Println("upd phi", bb.blockNum, "<-", ancestor.blockNum)
	for name, val := range ancestor.variables {
		for myname, myval := range bb.variables {
			if name == myname {
				fmt.Println(myval, val)
				if _, ok := bb.phiSet[name]; ok {
					bb.phiSet[name] = make([]int, 0)
				}
				bb.phiSet[name] = append(bb.phiSet[name], val.version)
				break
			}
		}
	}
}

func (bb *BB) updVarsVersion() {
	// функция вызывается после всех вызовов updPhi
	// но до обработки тела блока
	// обновляет версии переменных
	// обновляет номер переменн
	for name, val := range bb.phiSet {
		if len(val) == 1 {
			continue
		}

		max := -1
		for _, x := range val {
			if x > max {
				max = x
			}
		}

		bb.variables[name].version = max+1
	}
}

func (bb *BB) makePhi() {
	fmt.Println("block", bb.blockNum, "making phi", bb.phiSet)
	for name, val := range bb.phiSet {
		if len(val) == 1 {
			continue
		}

		max := -1
		for _, x := range val {
			if x > max {
				max = x
			}
		}

		bb.variables[name].version = max

		arr := []string{}
		arr = append(arr, fmt.Sprintf("%s(%d)", name, max))
		for _, x := range val {
			arr = append(arr, fmt.Sprintf("%s(%d)", name, x))
		}
		instr := Instruction{"phi", arr}
		bb.instructions = append([]*Instruction{&instr}, bb.instructions...)
	}
}

func (bb *BB) phiWalker() {

}

func (bb *BB) String() string {
	ret := ""
	ret += fmt.Sprintf("block %d {\n", bb.blockNum)
	for _, x := range bb.instructions {
		ret += "    " + x.String() + "\n"
	}
	ret += "}\n"
	return ret
}
