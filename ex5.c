// conditional macro definition

ifmacro 10>12
	int a=10;
endifmacro
elifmacro 10<12
	int a=20;
endelifmacro
elsemacro
	int a=0;
endelsemacro

int main()
{
	int b=-5;
	int s=a+b;
	printf("%d\n",s);
}
