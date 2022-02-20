assume CS:code, DS: data

data segment
a db 20
b db 10
c db 50
d db 4
res db 0
dec_ans db "000000$"
hex_ans db "00000h$"
data ends

sseg segment stack
db 256 dup(0)
sseg ends

code segment
start:

mov AX, data
mov DS, AX
xor ax, ax

;математика происходит
mov al, a
mov bl, b
add al, bl
shr al, 1
mov bl, c
sub bl, al
mov al, d
add al, bl
mov res, al


mov bl, 10
mov si, 4
dec_label:
    div bl
    add ah, 48
    mov dec_ans[si], ah
    xor ah, ah
    dec si
    cmp al, 0
    jg dec_label
mov si, 5
mov dec_ans[si], 10

xor ax, ax
mov al, res
mov bl, 10h
mov si, 4
hex_label:
    div bl
    cmp ah, 10
    ; add a, 48
    ; jmp hex_label2
    jl add_48
    jge add_55
add_48:
    add ah, 48
    jmp hex_label2
add_55:
    add ah, 55
    jmp hex_label2
hex_label2:
    mov hex_ans[si], ah
    xor ah, ah
    dec si
    cmp al, 0
    jg hex_label



mov ah, 09h
mov dx, offset dec_ans
int 21h
mov dx, offset hex_ans
int 21h

mov AX, 4C00h
int 21h

code ends
end start