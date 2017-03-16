;conditional macro example

mstart fun1
mov eax,0
mov ebx,10
mend

ifmacro 10>2		
	print(1)
	ifmacro 10>11
	print(2)
	endifmacro
	elifmacro fun1
	print(-2)
	endelifmacro
endifmacro

SECTION .text
extern printf
global main
main:
fun1
mov ecx,ebx
