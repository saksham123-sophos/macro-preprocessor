	print(1)
	print(-2)
SECTION .text
extern printf
global main
main:
mov eax,0
mov ebx,10
mov ecx,ebx