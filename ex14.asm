;nested macro example

mstart pi 3.14

mstart area(rad) imul eax,rad

mstart fun1			
mov eax,0
mov ebx,pi
mstart expo 2.73
mend

SECTION .text
extern printf
global main
main:
fun1
area(pi)
mov ecx,expo
