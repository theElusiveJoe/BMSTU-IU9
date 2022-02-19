; 8. Каждому элементу массива, начиная со второго, присвоить значение
;максимального элемента из числа ему предшествующих и его самого. 

assume CS:code, DS: data

data segment

mas dw 1,1,2,1,1,1,4,13,1
; mas dw 9 dup(0)
len dw 8

a dw 75
c dw 74
m dw 5786
base = 2
; lol db "lol$"
; kek db "kek$"
num db "000000$"
s1 db "was:$"
s2 db "now:$"

data ends

sseg segment stack
db 256 dup(0)
sseg ends

code segment

; линейный конгруэнтный метод 
; генерации случайных чисел
fillarr proc 
    push ax cx dx
    mov ax, 5
    xor cx, cx
    fill:
        mul a
        add ax, c
        div m
        mov ax, dx

        push ax
        mov ax, cx
        mov dx, base
        mul dx
        mov si, ax
        pop ax

        mov mas[si], ax
        inc cx
        cmp cx, len
        jbe fill

    pop dx cx ax
    ret
fillarr endp

;печатает число в ax
print_ax proc   
    push bx dx

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

    pop dx bx
    
    ret
print_ax endp

start:
mov ax, data
mov ds, ax
xor ax, ax

; дописывает перенос строки в конец
mov si, 5
mov num[si], 10

;заполняем массив рандомными числами
call fillarr

mov ah, 09h
mov dx, offset s1
int 21h
; выводим каждый эл-т массива
xor cx,cx
lop0:
    mov ax, cx
    mov dx, base
    mul dx
    mov si, ax

    mov ax, mas[si]
    call print_ax

    cmp cx, len
    inc cx
    jb lop0

; сейчас буду искать самый большой эл-т слева
xor cx, cx
xor si, si
mov bx, mas[si]
lop1:
    mov ax, cx
    mov dx, base
    mul dx
    mov si, ax

    cmp bx, mas[si]
    jle bx_bigger
    jmp masi_bigger

    bx_bigger:
    mov bx, mas[si]
    jmp main

    masi_bigger:
    mov mas[si], bx

    main:
    inc cx
    cmp cx, len
    jle lop1

mov ah, 09h
mov dx, offset s2
int 21h
; выводим каждый эл-т массива
xor cx,cx
lop2:
    mov ax, cx
    mov dx, base
    mul dx
    mov si, ax

    mov ax, mas[si]
    call print_ax

    cmp cx, len
    inc cx
    jb lop2


mov ax, 4C00h
int 21h

code ends
end start