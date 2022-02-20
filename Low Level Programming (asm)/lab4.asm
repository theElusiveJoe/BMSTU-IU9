assume cs: code, ds: data

data segment
; s1 db 0, 10 dup('$')
; s2 db 0, 10 dup('$')

; не более 10ти символов в строке
s1 db 11, 11 dup('$')
s2 db 11, 11  dup('$')

lenres equ 21
res db lenres, lenres, lenres dup ('$'), 10, '$'

unires db 11, 11 dup (0), "$"
temp db 11, 11 dup (0), "$"

dummy db 'here', 10, '$'

newline db 10, 36, 36

divider db 10

instr1 db 10, 'input first num', 10, 36
instr2 db 10, 'input second num', 10, 36

plus_str db 'summ: $'
minus_str db 'difference : $'
mult_str db 'product: $'

decmode_str db 10, 'in DEC mode', 10, '$'
hexmode_str db 10, 'in HEX mode', 10, '$'

errmsg db 10, 'invalid symbol$' 

num db "00000", 10, '$'

data ends

sseg segment stack
db 256 dup(0)
sseg ends

code segment

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
	push ax dx
	mov dx, offset newline
	mov ah, 09h
	int 21h
	pop dx ax
	ret
printNewLine endp

print_here proc
	push dx 
	push ax
	mov dx, offset dummy
	mov ah, 09h
	int 21h
	pop ax
	pop dx
	ret
print_here endp

put_zero_in_res_foo proc
    push cx bx

    mov cx, lenres
    mov bx, 2
    md_put_zero:
        mov res[bx], 0
        inc bx
        loop md_put_zero

    pop bx cx
    ret
put_zero_in_res_foo endp

; взвращает 1 в ax, если s1>s2, 
; 2, если s2>s1
; 0, если s1=s2 
; !!! нет поддержки строк с незначащими нулями  
s1_bigger_s2_foo proc  
    push bx cx dx si di

    mov si, 1
    ; сравниваем длинну строк
    mov al, s1[1]
    mov bl, s2[1]
    cmp al, bl
    jg s1_greater
    jl s2_greater
    xor ch, ch
    mov cl, s1[1]  ; положили в cx длинну строк
    inc cl         ;(они одинаковые по длинне)

    eq_len:
        inc si 
        mov al, s1[si]
        mov bl, s2[si]
        cmp al, bl
        jg s1_greater
        jl s2_greater
        loop eq_len
        mov ax, 0
    
    s1_greater:
        mov ax, 1
        jmp cmpend
    s2_greater:
        mov ax, 2
        jmp cmpend

    cmpend:

    pop di si dx cx bx
	ret

s1_bigger_s2_foo endp

; непонятные inc`и индексных регистров связаны
; с тем, что в начале строки хранятся 2 
; байта: с массимальной и реальной длинной

mul_foo proc
    push ax bx cx dx si di

    ; зануляем строку res
    call put_zero_in_res_foo

    ; di - на конец s2
    xor ax, ax
    mov al, s2[1]
    inc al
    mov di, ax

    dm_multing:
     
        ; подготавливаем помножение на разряд

        ; переводим si в конец s1
        xor ax, ax
        mov al, s1[1]
        inc al
        mov si, ax

        ; 0 в уме
        xor dl, dl

        ; помножаем на разряд
        mov dh, s2[di] ; в dh кладем разряд s2, на который будем помножать s1
        dm_multing_digit: 
            mov al, [si] ; записали в al тот разряд s1, который будем помножать
            mul dh  ; теперь в ax результат перемножения 
                    ; но на самом деле в al - потому что число маленькое
            add al, dl ; прибавили то, что в уме
            xor dl, dl ; и сразу же забыли
            div divider ; теперь в ah искомый разряд

            mov dl, al ; результат  держим в уме (в dl)
            
            ; теперь добавим к res результат перемножения из ah
            xor cx, cx ; в cx запишем сумму длинн строк
            add cl, s1[1]
            add cl, s2[1]
            sub cx, si ; и вычтем длинну остатка строк
            inc cx
            sub cx, di ; тем самым, получим разряд res,
                        ; в который надо добавить ah
            inc cx 
            mov bl, res[1]  ; в bx записали дилинну res
            inc bl
            sub bl, cl      ; и вычитаем из нее длинну остатка
            mov cl, res[bx]
            add cl, ah
            mov al, cl
            xor ah, ah

            div divider
            add dl, al
            ; в al результат деления (т.е. 1, если был переход через разряд)
            ; а в ah - цифра, которую надо записать
            
            mov res[bx], ah
            xor ax, ax
            mov al, res[bx]

            dec si ; сдвинулись влево по первой строчке
            cmp si, 1 ; если совпадает с началом, заканчиваем
            jg dm_multing_digit ; если не дошли до конца si
        
        ; если в уме что-то осталось, запишем это
        ; в самы старший разряд
        ; причем, он гарантированно нулевой, поэтому просто записываем
        dec bx ; - вот это разряд в res 
        mov res[bx], dl
        
        dec di ; сдинулись вправо по второму множителю
        cmp di , 1
        je dm_end
        jmp dm_multing

    dm_end:
        
    pop di si dx cx bx ax
    ret
mul_foo endp

; res = s1 + s2
plus_foo proc
    push ax bx cx dx si di

    ; зануляем строку res
    call put_zero_in_res_foo

    xor ax, ax
    ; переводим si на конец s1
    mov al, s1[1]
    inc al
    mov si, ax
    ; di - на конец s2
    mov al, s2[1]
    inc al
    mov di, ax
    ; bx - на конец res
    mov al, res[1]
    inc al
    mov bx, ax

    xor dl, dl
    dp_adding:
        mov al, s1[si]
        mov ah, s2[di]
         
        add al, ah
        add al, dl

        xor ah,ah
        div divider
        
        mov dl, al  ; в al результат деления
                    ; запоминаем его в уме
        ; а в ah - цифра, которую надо записать
        mov res[bx], ah        

        dec si
        dec di
        dec bx

        ; по умолчанию, первой должна закончиться s2
        cmp si, 1 ; если кончилась si
        je dp_s1_ended
        cmp di, 1 ; если конилась di
        je dp_s2_ended


        jmp dp_adding

    dp_s1_ended: ; если закончислась s1
        mov cx, di  ; записываем в cx,
        ; записываем в si указатель на текущий байт в s2
        lea si, s2
        add si, cx
        dec cx      ; сколько раз осталось "копировать" из s2 в res
        jmp pre_dp_end_adding

    dp_s2_ended: ; если закончислась s2
        mov cx, si  ; записываем в cx,
        ; записываем в si указатель на текущий байт в s1
        lea si, s1
        add si, cx
        dec cx      ; сколько раз осталось "копировать" из s1 в res
    pre_dp_end_adding:
        cmp cx, 0
        je dp_end
    dp_end_adding:        
        mov al, [si]
        add al, dl

        xor ah,ah
        div divider
        mov dl, al  ; в al результат деления
                    ; запоминаем его в уме
        ; а в ah - цифра, которую надо записать
        mov res[bx], ah 

        dec bx
        dec si
        
        loop dp_end_adding
    
    dp_end:
    mov res[bx], dl ; не забываем перенести все из ума
        
    pop di si dx cx bx ax
    ret
plus_foo endp

minus_foo proc
    push ax bx cx dx si di

    ; зануляем строки для ответов
    call put_zero_in_res_foo
    
    xor ax, ax
    ; переводим si на конец s1
    lea si, s1
    mov al, s1[1]
    inc al
    add si, ax
    ; di - на конец s2
    lea di, s2
    mov al, s2[1]
    inc al
    add di, ax
    ; bx - на конец res
    mov al, res[1]
    inc al
    mov bx, ax                                    
                                                        
    xor dl, dl ; занулили dl                         
    ; - в нем будем запоминать единичку                                               
    
    ; сравниваем уменьшаемое и вычитаемое
    call s1_bigger_s2_foo
    cmp ax, 1
     
    je dm_s1_greater ; если уменьшаемое больше
    jg dm_s2_greater ; если вычитаемое больше
    
    ; если числа равны, сразу печатем нули
    pop di si dx cx bx ax
    ret
    ; иначе вычитаем

    xor dx, dx

    ; по умолчанию вычитаем di из si
    dm_s1_greater: ; s1 больше s2
        ; кладем начало длинной строки на стек
        lea cx, s1
        inc cx
        push cx
        ; в cx запоминаем указатель на начало короткой строки
        lea cx, s2
        inc cx
        jmp dm_subbing1
    dm_s2_greater: ; s2 больше s1
        ; поэтому тут меняем их местами 
        xchg si, di
        ; кладем начало длинной строки на стек
        lea cx, s2
        inc cx
        push cx
        ; в cx запоминаем указатель на начало короткой строки
        lea cx, s1
        inc cx
        mov res[2], '-'
    
    dm_subbing1:
        mov al, [si] ; al - уменьшаемое
        mov ah, [di] ; ah - вычитаемое
        add ah, dl  ; то, что было в уме, прибавили к вычитаемому
        
            ; cmp ah, al  ; теперь сравниваем, чтобы понять,
            ;             ; запоминать ли единичку в уме

            ; jg dm_one_in_mind1 ; если вычитаемая цифра больше
            ; jle dm_no_one_in_mind1 ; если уменьшаемая цифра больше
            
            ; dm_one_in_mind1:
            ;     mov dl, 1   ; единичку заняли у старшего разряда
            ;     add al, 10  ; прибавили десяточку к текущему разряду
            ;     jmp dm_final_mind1
            
            ; dm_no_one_in_mind1:
            ;     xor dl, dl
            
            ; dm_final_mind1:
         
        add al, divider ; заняли единичку (в любом случае)
         
        sub al, ah          ; в al результат вычитания
         
        xor ah, ah ; чтобы делить al, а не ax
        
        div divider     ; и поделим результат на 10
        ; в al результат деления - количество десятков
        ; в ah остаток - нужный нам разряд
        mov dl, al      
        xor dl, 1       
        ; если нам не понадобится то,
        ; что мы занимали, оно окажется в dl
        ; т.е. если не понадобилось, зн в dl 1,
        ; значит мы не занимали, 
        ; значит в dl должен быть 0
        ; поэтому xor`им
        ; аналогично с 0
        ; решил сделать без сравнения - эксперимента ради
        mov res[bx], ah ; записали результат в res
        
        ; сдвинулись на единичку влево 
        dec si
        dec di
        dec bx
        
        ; если вычитаемое не закончилось
        cmp di, cx
        jne dm_subbing1

    pop cx ; сняли указатель на начало уменьшаемого
    
    dm_subbing2:
        ; если уменьшаемое закончилось
        cmp si, cx
        je dmm_end

        mov al, [si] ; al - уменьшаемое
        mov ah, dl
        
        add al, divider ; заняли единичку (в любом случае)
        sub al, ah          ; в al результат вычитания
        xor ah, ah
        div divider     ; и поделим результат на 10
        ; в al результат деления - количество десятков
        ; в ah остаток - нужный нам разряд
        mov dl, al      
        xor dl, 1       
        mov res[bx], ah ; записали результат в res
        
        ; сдвинулись на единичку влево 
        dec si
        dec bx
        
        jmp dm_subbing2
        

    ; уменьшаемое гарантированно больше вычитаемого
    ; поэтому в конце dl точно равен 0 
    dmm_end:
    pop di si dx cx bx ax

	ret
minus_foo endp

; переводит строку цифр в массив цифр
; работает с аргументом из регистра si
string_to_num proc
    push ax bx cx dx

    xor ch, ch
    xor ah, ah

    inc si
    mov cl, [si]

    stn_label:
        inc si
        mov al, [si]
        xor ah, ah
        
        cmp divider, 10
        je dec_only

        cmp al, 104 ; h
        jg stn_label_err
        cmp al, 97 ; a
        jge stn_laz

        cmp al, 72 ; H
        jg stn_label_err
        cmp al, 65 ; A
        jge stn_uAZ

        dec_only:
        cmp al, 57 ; 9
        jg stn_label_err
        cmp al, 48 ; 0
        jge stn_09

        stn_laz:
            sub al, 87
            jmp stn_label_end
        stn_uAZ:
            sub al, 55
            jmp stn_label_end
        stn_09:
            sub al, 48
            jmp stn_label_end

        stn_label_err:
            mov ah, 09h
            lea dx, errmsg
            int 21h
            mov ah, 4ch
            int 21h
        stn_label_end:
            mov [si], al
        
        loop stn_label

    pop dx cx bx ax
    ret 
string_to_num endp

; переводит массив цифр в строку  
; работает с аргументом из регистра si
num_to_string proc
    push ax bx cx dx

    xor ch, ch
    xor ah,ah

    inc si
    mov cl, [si]

    nts_label:
        inc si

        mov al, [si]
        
        cmp al, '-'
        je nts_label_end

        cmp al, 10
        jge nts_uAZ

        add al, 48
        jmp nts_label_end

        nts_uAZ:
            add al, 55
           
        nts_label_end:
            mov [si], al
        loop nts_label

    pop dx cx bx ax
    ret 
num_to_string endp

test_all proc
    ;ввод строк
    mov ah, 09h
    lea dx, instr1
    int 21h

    mov ah, 0ah
    lea dx, s1
    int 21h

    mov ah, 09h
    lea dx, instr2
    int 21h

    mov ah, 0ah
    lea dx, s2
    int 21h

    ; преобразуем строки к числам 
    lea si, s1
    call string_to_num
    lea si, s2
    call string_to_num
    call printNewLine

    ; сложение
    mov ah, 09h
    lea dx, plus_str
    int 21h

    call plus_foo

    lea si, res
    call num_to_string

    mov ah, 09h
    lea dx, res[2]
    int 21h
    ; вычитание
    mov ah, 09h
    lea dx, minus_str
    int 21h

    call minus_foo

    lea si, res
    call num_to_string
    mov ah, 09h
    lea dx, res[2]
    int 21h

    ; произведение
    mov ah, 09h
    lea dx, mult_str
    int 21h

    call mul_foo

    lea si, res
    call num_to_string
    mov ah, 09h
    lea dx, res[2]
    int 21h

    ret
test_all endp

start:	
;начальные настройки
	mov ax, data
	mov ds, ax
	mov es, ax
	xor ax, ax

    mov ah, 09h
    lea dx, decmode_str
    int 21h
    call test_all

    mov divider[0], 16

    mov ah, 09h
    lea dx, hexmode_str
    int 21h
    call test_all

    mov ah, 4ch
    int 21h
    code ends
end start