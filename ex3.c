// comments in macro
// single comment starts with @
//multi-line comments starts with ^ and ends with ^

mstart fun
int a=0; 		@single line comment
int b=10;		^ multi line
			 comment ^
mend

int main()
{
	fun 
	int s=a+b;
	printf("%d\n",s);
}
