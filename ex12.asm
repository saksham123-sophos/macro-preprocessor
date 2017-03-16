;multi-line macro example

mstart pi 3.14

mstart fun1			
mov eax,0
mov ebx,10
mend

SECTION .text
extern printf
global main
main:
fun1
mov ecx,pi
