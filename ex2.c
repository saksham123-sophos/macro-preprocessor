//multi-line macro definition

mstart fun
int a=0;
int b=10;
mend

int main()
{
	fun 
	int s = a+b;
	printf("%d\n",s);
}
