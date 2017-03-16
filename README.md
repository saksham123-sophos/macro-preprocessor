The macro preprocessor is compatible with c , python and nasm.
Must be used on a linux system.

>>>>>>>>>>>>>>Features Available:

1.) Single line definition Macros

	Syntax: 	mstart <macro_name><(argument1,argument2...)>(brackets may be avoided too in case of no arguments)	<macro_definition>
	
2.) Multi line definition macros
	
	Syntax:	mstart <macro_name><(argument1,argument2...)>(brackets may be avoided too in case of no arguments)
				definition line 1
				...
				...
				...
				definition last line
				mend
				
3.) Comments for macros

	Single line comments start with '@'.
	Multi line comments are enclosed within '^' at beginning and end.
	
4.) Nested Macro Definitions

	Syntax: 	mstart <macro_name><(argument1,argument2...)>(brackets may be avoided too in case of no arguments)
				definition line 1
				...
				...
				mstart <macro_name2>><(argument1,argument2...)>(brackets may be avoided too in case of no arguments)
				definition line 1
				...
				...
				definition last line
				mend
				...
				...
				definition last line
				mend
				
		Preprocessor is not restricted by number of nested definitions and number of arguments passed.
		
5.) Conditional Macros

	Syntax: 	ifmacro <expression of integer constants>/<identifier_name>
				...
				...
				endifmacro
				elifmacro <expression of integer constants>/<identifier_name>
				...
				...
				endelifmacro
				elifmacro <expression of integer constants>/<identifier_name>
				...
				...
				endelifmacro
				elsemacro
				...
				...
				endelsemacro
				
		elifmacro and elsemacro may be dropped as per requirement. Nested conditional macros also allowed.
	
	
>>>>>>>>>>>>>>Preprocessor Usage(must be used through command line terminal):

											python3 macro.py <input_filename>
								Ex:		python3 macro.py ex1.c
											
								* input file must be present in the same directory as the macro.py
								
Output:a file with .i extension having same name as input file in the same directory.
