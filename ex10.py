#conditional macro definition

ifmacro 10<8
	print("condition is true")
	ifmacro 10<5
	print(-2)
	endifmacro
endifmacro
elifmacro 10>8
print("in 2nd level macro")
endelifmacro

print("it is conditional macro")
