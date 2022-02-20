assume cs: code, ds: data

data segment
dummy db 10 ; чтобы strrchr могла вернуть нулевой указатель
string db 100, 100 dup('$')
mychar db 2, 0, 0, '$'

num db '00000',10,'$'

fnd db 10, 'found! ', 10, 36
nochar db 10, 'not found.', 10, 36
retrn db 'ret = ', 36

instr1 db 'input your string', 10, 36
instr2 db 10,'input your char', 10, 36

data ends

sseg segment stack
db 256 dup(0)
sseg ends

code segment
;печатает число в ax
print_ax proc   
    push bx dx si ax

    mov bx, 10
    mov si, 4
    xor dx, dx

    dec_label:
        div bx
        add dx, 48
        mov num[si], dl

        xor dx, dx
        dec si
        cmp ax, 0

        jg dec_label


    mov ah, 09h
    mov dx, offset num
    int 21h

    mov si, 0
    mov num[si], 48
    mov si, 1
    mov num[si], 48
    mov si, 2
    mov num[si], 48
    mov si, 3
    mov num[si], 48
    mov si, 4
    mov num[si], 48

    pop ax si dx bx
    
    ret
print_ax endp

printNewLine proc
	push dx 
	push ax
	mov dx, offset dummy
	mov ah, 09h
	int 21h
	pop ax
	pop dx
	ret
printNewLine endp

strrchr proc
	push bp
	mov bp, sp

	; di указывает на начало строки
	mov	di, [bp+4] 
	add di, 1 ; di указывает на байт, в котором длинна строки
	mov cl, [di] ; запишем в cx длинну строки для дальнейших действий с ней
	xor ch, ch ; но старший байт надо занулить, ведь работаем с байтами, а не словами
	add di, cx ; добавляем длинну строки к di
	mov ax, di
	; теперь di указывает на конец строки 

	; в al помещаю значение искомого символа
	mov al, [bp + 6] 

	std ; ставим флаг df в единицу, чтобы строка обрабатывалась с конца
	
	repne scasb
	je	found   ; если равны (а то мало-ли до начала дошли и закончили)
	failed: 
		mov di, 0   
		jmp     endd  
	found:       
		inc di 	; приходится свигать на 1 вперед
				; из-за особенностей работы scas
	endd:
	pop bp
	pop bx ; снял retaddr в bx 
	push di ; закинул возвращаемое значение
	push bx ; сверху положил retaddr

	ret
strrchr endp

start:	
	; начальные настройки
	mov ax, data
	mov ds, ax
	mov es, ax
	xor ax, ax
	
	;ввод строки
	mov ah, 09h
	lea dx, instr1
	int 21h
	mov ah, 0ah
	lea dx, string
	int 21h

	; ввод символа (функция ввода символа 01h почему-то не работает)
	mov ah, 09h
	lea dx, instr2
	int 21h
	mov ah, 0ah
	lea dx, mychar
	int 21h

	; закидываю символ 
	lea si, mychar
	add si, 2
	mov ax, [si]
	push ax
	; закидываю строку
	mov  ax, offset string
	push ax
	; вызов функции
	call strrchr


	; проверяем результат работы процедуры
	pop si ; снимем результат со стека
	cmp si, 0
	jne	found2  
	failed2: 
		mov     ah,09h
		lea     dx, nochar
		int     21h     
		jmp endd2
	found2:       
		mov     ah,09h
		lea     dx, fnd
		int     21h
		mov dx, si
		int     21h
		
	endd2:
	; mov ah, 09h
	; lea dx, retrn
	; int 21h
	; mov ax, si
	; call print_ax

	mov ah, 4ch
	int 21h
	code ends
	end start