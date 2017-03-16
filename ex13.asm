;comments in macro
;single comment starts with @
;multi-line comments starts with ^ and ends with ^

mstart fun1			
mov eax,0			@ single line comment example

^ 
multi line 
comment example ^

mov ebx,12
mend

SECTION .text
extern printf
global main
main:
fun1
