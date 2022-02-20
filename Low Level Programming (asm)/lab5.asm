init macro 
    mov ax, data
	mov ds, ax
	mov es, ax
	xor ax, ax
endm

print macro strart
    push ax dx
	mov dx, offset strart
	mov ah, 09h
	int 21h
	pop dx ax
endm

input macro src 
    push ax dx
	mov ah, 0ah
	lea dx, src
	int 21h
    pop dx ax
endm

if_equal macro a, b, labl
    cmp a, b 
    je labl
endm

if_not_equal macro a, b, labl
    cmp a, b 
    jne labl
endm

simple_copy macro src, srci, dst, dsti, jmplbl
    mov al, src[srci]
    mov dst[dsti], al
    inc srci
    inc dsti
    ifnb <jmplbl>
        jmp jmplbl
    endif
endm

delete_spaces macro text
    mov si, 3
    mov di, 3

    compare:
        ; если конец строки, то заканчиваем
        if_equal text[si], 36, end_compare

        ; сравнили с пробелом 
        if_equal text[si], 32, found_space

        ;если не пробел, то просто копируем
        simple_copy text, si, text, di, compare

        found_space:
       
        ; если предыдуший был пробелом
        if_not_equal text[si-1], 32, copy_space

        inc si
        jmp compare

        copy_space:
        ; иначе, просто копируем этот пробел
        simple_copy text, si, text, di, compare
        
        
    end_compare:
    
    mov text[di], '$'
endm

mode equ 1 ; 0 - ввод с клавиатуры, 1 - уже готовая строка

def_mode macro
    ife mode
        create_text macro
            text db 100, 100, 102 dup('$')
        endm
        input_text macro
            print instr1
            input text
        endm
    else
        create_text macro
            text db 13, 13, 'a a     b   c$'
        endm
        input_text macro
        endm
    endif
endm

def_mode
assume cs: code, ds: data

data segment

create_text

instr1 db 'input your text', 10, 36

newline db 10, 36

data ends

sseg segment stack
db 256 dup(0)
sseg ends

code segment

start:
    ; в программе есть переменная mode 
    ; если mode == 0, то текст вводится с клавиатуры
    ; иначе, он - уже готовая строка
    ; (типа удобно для отладки)

	; начальные настройки
	init

    input_text

    delete_spaces text

    print newline

    print text+2

	mov ah, 4ch
	int 21h
	code ends
	end start