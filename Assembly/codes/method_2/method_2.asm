.include "/home/gokulkumar/assembly/codes/method_2/m328Pdef.inc"
ldi r16,0b11000111
out DDRD,r16
ldi r16,0b00100000
out DDRB,r16            ;declaring 8th pin as output
loop:                   ;loop for reading the input from pins 3,4,5 continously
        ldi r17, 0b00001000 ;
        ldi r24,0b00001000
        mov r18,r17
        and r18,r24
        ldi r25,0b00000011
        loop1:  lsr r18  ;X
        dec r25
        brne    loop1
        mov r19,r17
        ldi r24,0b00010000
        and r19,r24
        ldi r25,0b00000100
        loop2:  lsr r19   ;Y
        dec r25
        brne    loop2
        ldi r24,0b00100000
        mov r20,r17
        and r20,r24
        ldi r25,0b00000101
        loop3:  lsr r20  ;Z
        dec r25
        brne    loop3
        ldi r21,0x00
        mov r21,r18
        com r21
        or r21,r19
        ldi r26,0b00000101
        loop4:  lsl r21  
        dec r26
        brne    loop4
     out PORTB,r21
    rjmp loop

