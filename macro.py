import sys
from collections import defaultdict
import re

#dict having details related to macros
macro_dict = defaultdict(list)

#list containing names of macros
macro_list=[]

#list containing number of arguments of corresponding macros
arg_list=[]


#function to remove empty lines
def rempty():
	i=0
	while(i<len(prog)):
		#removing whitespaces from both sides
		temp=prog[i].strip()
		#if line is still empty
		if(temp==''):
		#remove line from program list
			prog.remove(prog[i])
			#since length of program list is now changed so making i 0 again
			i=0
			continue
		else:
		#if line is not empty continue
			i+=1

#function to remove multi line comments of c program
def rmulti():
	i=0
	while(i<len(prog)):
	#removing whitespaces from both sides
		temp=prog[i].strip()
		#searching for comment starting in same line with a program line
		temp2=re.search("\/\*.*",prog[i])
		#if line starts with /* or temp2 found a search
		if(temp[0:2]=="/*" or temp2!=None):
			#if condition entered due to temp2!=None
			if(temp[0:2]!="/*" and temp2!=None):
			#removing only comment part from the line
				prog[i]=re.sub("\/\*.*","",prog[i])
				l=i+1
			else:
				l=i
			#temporary variables 
			k=i
			j=i
			#finding ending of this comment
			while(j<len(prog)):
				temp2=prog[j]
				#if line ends with */
				if(temp2[-2:]=="*/"):
				#getting line number
					k=j
					break
				else:
					j+=1
			#counting number of lines of comment
			n=k-l+1
			count=0
			while(count<n):
			#removing all lines of comment
				prog.remove(prog[l])
				count+=1
		i+=1

#function to remove multi line macro comments		
def macromulti():
	i=0
	while(i<len(prog)):
		temp=prog[i]
		#searching for comment starting in same line with a program line
		temp2=re.search("\^.*",prog[i])
		#if line starts with ^ symbol or temp2 found a search
		if(temp[0:1]=="^" or temp2!=None):
			#if condition is true due to temp2!=None
			if(temp[0:1]!="^" and temp2!=None):
			#remove only comment part from the line
				prog[i]=re.sub("\^.*","",prog[i])
				l=i+1
			else:
				l=i
		#temporary variables
			k=i
			j=i
			while(j<len(prog)):
				temp2=prog[j]
				#if line ends with ^
				if(temp2[-1:]=="^"):
					k=j
					break
				else:
					j+=1
			#getting number of lines of comment
			n=k-l+1
			count=0
			while(count<n):
			#removing all comment lines
				prog.remove(prog[l])
				count+=1
		i+=1
			
#function to remove multi line comments of python program	
def pymulti():
	i=0
	while(i<len(prog)):
	#removing whitespaces from both end
		temp=prog[i].strip()
		#searching for comment starting in same line with a program line
		temp2=re.search("\'\'\'.*",prog[i])
		#if line starts with ''' symbol or temp2 found a search
		if(temp[0:3]=="\'\'\'" or temp2!=None):
			if(temp[0:3]!="\'\'\'" and temp2!=None):
				prog[i]=re.sub("\'\'\'.*","",prog[i])
				l=i+1
			else:
				l=i
			#temporary variables("\'\'\'.*",prog[i])
			k=i
			j=i
			while(j<len(prog)):
				temp2=prog[j].strip()
				#if line ends with ''' symbol
				if(temp2[-3:]=="\'\'\'"):
					k=j
					break
				else:
					j+=1
			#getting number of lines of comment
			n=k-l+1
			count=0
			while(count<n):
				#removing all lines of comment
				prog.remove(prog[l])
				count+=1
		i+=1
	
#function for c macros	
def cmacro():
	#removing \n from each line of input program present in prog list
	for i in range(len(prog)):
		prog[i]=prog[i].replace('\n','')
		prog[i]=prog[i].strip()
	#removing comments which are in line of a program line
	for i in range(len(prog)):
		prog[i]=re.sub("@.*","",prog[i])
		prog[i]=re.sub("\/\/.*","",prog[i])
	i=0
	#calling rempty function
	rempty()
	while(i<len(prog)):
	#if line is a single line comment of c language or macro
		if(prog[i][0:2]=="//" or prog[i][0:1]=="@"):
		#removing single line comments
			prog.remove(prog[i])
			i=0
			continue
		else:
			i+=1
	#calling rmulti function
	rmulti()
	#calling macromulti function
	macromulti()
	#calling replace function
	replace()
	#handling conditional macros
	conditional_macros(0)
	#calling rempty function
	rempty()
						
#function for python macros
def pymacro():
	#removing \n from each line of input program present in prog list
	for i in range(len(prog)):
		prog[i]=prog[i].replace('\n','')
	#removing comments which are in line of a program line
	for i in range(len(prog)):
		prog[i]=re.sub("@.*","",prog[i])
		prog[i]=re.sub("\#.*","",prog[i])
	i=0
	#calling rempty function
	rempty()
	while(i<len(prog)):
		temp=prog[i].strip()
		#if line is a single line comment of python language or macro
		if(temp[0:1]=="#" or temp[0:1]=="@"):
			#removing single line comments
			prog.remove(prog[i])
			i=0
			continue
		else:
			i+=1
	#calling pymulti function
	pymulti()
	#calling macromulti function
	macromulti()
	#calling replace function
	replace()
	#handling conditional macros
	conditional_macros(0)
	#calling rempty function
	rempty()

#function for nasm macros	
def asmmacro():
	for i in range(len(prog)):
	#removing \n from each line of input program present in prog list
		prog[i]=prog[i].replace('\n','')
	#removing comments which are in line of a program line
	for i in range(len(prog)):
		prog[i]=re.sub("@.*","",prog[i])
		prog[i]=re.sub("\;.*","",prog[i])
	i=0
	#calling rempty function
	rempty()
	while(i<len(prog)):
		temp=prog[i].strip()
		#if line is a single line comment of python language or macro
		if(temp[0:1]==";" or prog[i][0:1]=="@"):
			#removing single line comments
			prog.remove(prog[i])
			i=0
			continue
		else:
			i+=1
	#calling macromulti function
	macromulti()
	#calling replace function
	replace()
	#handling conditional macros
	conditional_macros(0)
	#calling rempty function
	rempty()

#function to store macro details and replacing macros in the program
def replace():
#calling function store_macro starting from starting of input program
	store_macro(0)
	#appending argument count of all macros in arg_list list
	for i in range(len(macro_list)):
		arg_list.append(macro_dict[macro_list[i]][0])
	#iterating through list having names of all macros to find macros to replace them
	for count in range(len(arg_list)):
	#iterating through each line of program to find if a macro has been called or not
		for i in range(len(prog)):
		#iterating through each macro name
			for j in range(len(macro_list)):
			#if macro currently being checked has 0 number of arguments
				if(arg_list[j]==0):
				#joining all lines of macro definition by \n
					x='\n'.join(macro_dict[macro_list[j]][1])
				#substituting macro name with its definition if name is present in current program line
					prog[i]=re.sub(macro_list[j],x,prog[i])
					#if it is conditional macro then don't expand the macro
					if("ifmacro" in prog[i] or "elifmacro" in prog[i] or "elsemacro" in prog[i]):
						prog[i]=re.sub(x,macro_list[j],prog[i])
				#if macro has non-zero argument count
				elif(arg_list[j]!=0):
					#searching for part containing macro name and arguments passed from the current line if macro has been called
					temp=re.search(macro_list[j]+"\([\w,&-\[\]]*\)",prog[i])
					#if result of search is not None
					if(temp!=None):
						#splitting match found first by (
						tt=(temp.group()).split('(')
						#removing tt[0] which is nothing but macro name
						tt.remove(tt[0])
						k=0
						#iterating through every character of remaining portion of match , which contains names of arguments passed to macro
						while(k<len(tt[0])):
						#if ending bracket not found keep iterating
							if(tt[0][k]!=')'):
								k+=1
							#if ending bracket found
							else:
							#getting arguments list
								tt=tt[0][0:k]
								break
						#splitting tt by , to get names of all aruments separately
						args=tt.split(',')
						#temporary dictionary to map argument name used in macro definition with actual argument passed 
						temp_dict={}
						k=1
						#iterating to all arguments passed
						while(k<=arg_list[j]):
						#taking argument name from macro definition as key and assigning actual argument passed as value
							temp_dict[macro_dict[macro_list[j]][k]]=args[k-1]
							k+=1
						#joining macro definition by \n
						x='\n'.join(macro_dict[macro_list[j]][k])
						#substituting macro call with its complete definiton
						prog[i]=re.sub(macro_list[j]+"\([\w,&-\[\]]*\)",x,prog[i])
						#if it is conditional macro then don't expand the macro
						if("ifmacro" in prog[i] or "elifmacro" in prog[i] or "elsemacro" in prog[i]):
							prog[i]=re.sub(x,macro_list[j],prog[i])
						k=1
						#iterating to replace each macro argument name in definiton with actual argument passed
						while(k<=arg_list[j]):
						#substituting each macro name used in macro definition with actual parameter passed to macro in call
							prog[i]=re.sub(macro_dict[macro_list[j]][k],temp_dict[macro_dict[macro_list[j]][k]],prog[i])
							k+=1
						

#functions to store macros internally
def store_macro(line):
#line is from where iteration needs to be started
	ite=line
	while(ite<len(prog)):
	#splitting each line of code in tokens
		temp=prog[ite].split()
	#if temp[3] exists it means it is a single line definition macro
		if(len(temp)>=3 and temp[0]=="mstart"):
			temp[2]=' '.join(temp[2:])
		#if macro has no arguments
			if("(" not in temp[1]):
			#appeind number of arguments in macro_dict with macro name as key
				macro_dict[temp[1]].append(0)
				#temporary list for storing macro definition
				def_list=[]
				#append macro definition to def_list list
				def_list.append(temp[2])
				#appending macro name to macro_list list
				macro_list.append(temp[1])
				#appending def_list in macro_dict with macro name as key
				macro_dict[temp[1]].append(def_list)
				j=ite
				#removing the single line definition macro line
				prog.remove(prog[ite])
				#continue iteration
				ite=j
				continue
			#if macro have some arguments
			elif("(" in temp[1]):
				#temporary variable to store name of macro
				t=""
				j=0
				#iterating till ( not found
				while(temp[1][j]!="("):
					t+=temp[1][j]
					j+=1
				j+=1
				k=j
				#count will store number of arguments passed
				count=0
				while(k<len(temp[1])):
				#if a comma(,) found the increment count by 1
					if(temp[1][k]==','):
						count+=1
					k+=1
				count+=1
				#appending count in macro_dict with macro name as key
				macro_dict[t].append(count)
				#appeding macro name into macro_list list
				macro_list.append(t)
				#temporary variable to store argument name
				ss=""
				while(j<len(temp[1])):
				#if character is neither comma(,) nor )
					if(temp[1][j]!="," and temp[1][j]!=")"):
					#append character to ss
						ss+=temp[1][j]
					else:
					#ss have a argument name . So, append it into macro_dict dictionary with macro name as key
						macro_dict[t].append(ss)
					#emptying the ss to store new argument name
						ss=""
					j+=1
				#temporary list for storing macro definition
				def_list=[]
				#append macro definition to def_list list
				def_list.append(temp[2])
				#appending def_list in macro_dict with macro name as key
				macro_dict[t].append(def_list)
				j=ite
				#removing the single line definition macro line
				prog.remove(prog[ite])
				#continue iteration
				ite=j
				continue
				
		#if line starts with mstart it means a macro needs to be defined
		elif(len(temp)!=0 and temp[0]=="mstart"):
			s="mstart"
			#if line has ( means macro have arguments
			if("(" in temp[1]):
			#t will eventually have macro name
				t=""
				j=0
				#iterating till starting of bracket found
				while(temp[1][j]!="("):
					t+=temp[1][j]
					j+=1
				j+=1
				k=j
				#count will save number of arguments 
				count=0
				while(k<len(temp[1])):
					if(temp[1][k]==','):
						count+=1
					k+=1
				count+=1
				#taking macro name as key and adding to its value count of arguments 
				macro_dict[t].append(count)
				#adding count of arguments in arg_list
				ss=""
				while(j<len(temp[1])):
					#if character found is valid for a argument name
					if(temp[1][j]!="," and temp[1][j]!=")"):
						ss+=temp[1][j]
					else:
					#appending argument name to value in dict which has macro name as key
						macro_dict[t].append(ss)
						ss=""
					j+=1
			#if no bracket it means macro is without any arguments
			else:
			#appending 0 as count of arguments to key macro name
				macro_dict[temp[1]].append(0)
				t=temp[1]
			ite+=1
			temp=prog[ite].split()
			#temporary list to store arguments name of macro
			def_list=[]
			#iterating till end of macro definition not found
			while(temp[0]!="mend"):
			#if mstart found between a macro it means it is a nested macro
				if(temp[0]=="mstart"):
				#recursively calling store_macro function
					store_macro(ite)
					ite=-1
					break
				#getting each line of macro definition
				tt=prog[ite]
				#appending each line to temporary list
				def_list.append(tt)
				ite+=1
				#splitting each line in tokens
				temp=prog[ite].split()
			#appending complete list of macro definition in macro_dict dictionary
			macro_dict[t].append(def_list)
			#appeding macro name to macro_list list
			macro_list.append(t)
			#to reset ite and start from beginning
			if(ite==-1):
				ite=0
				continue
		ite+=1	
	i=line
	#removing macro definition from program
	while(i<len(prog)):
	#splitting each line into its tokens
		temp=prog[i].split()
		#if line starts with mstart
		if(len(temp)!=0 and temp[0]=="mstart"):
			#temporary variables
			l=i
			k=i
			j=i
			while(j<len(prog)):
			#if end of macro definition found
				temp=prog[j].split()
				if(temp[0]=="mend" and temp[0]!="mstart"):
					k=j
					break
				else:
					j+=1
			#counting number of lines to be removed
			n=k-l+1
			count=0
			while(count<n):
			#removing all lines of macro definition
				prog.remove(prog[l])
				count+=1
			i=0
			continue
		i+=1
		
#function to handle conditional macros
def conditional_macros(line):
	i=line
	#function starts from ith line
	while(i<len(prog)):
	#splitting each program line into tokens
		temp=prog[i].split()
	#if nested macro has been completely checked
		if(temp[0]=="endifmacro" or temp[0]=="endelifmacro" or temp[0]=="endelsemacro"):
			return
		#if line starts with ifmacro keyword
		if(temp[0]=="ifmacro"):
			#if condition is a macro name which is defined
			if(temp[1] in macro_list):
				j=i+1
				#iterating through program lines
				while(j<len(prog)):
				#splitting each program line into tokens
					temp=prog[j].split()
				#if endifmacro found it means conditional macro statement is finished
					if(temp[0]=="endifmacro" and temp[0]!="ifmacro"):
						break
					#if a conditional macro contains another conditional macro nested
					if(temp[0]=="ifmacro"):
					#recursive call to conditional_macro to starting from this line
						conditional_macros(j)
						i=-1
						break
					j+=1
				#if another conditional nested macro found
				if(i==-1):
					i=line
					continue
				#removing ifmacro and endifmacro lines
				prog.remove(prog[j])
				prog.remove(prog[i])
				remove()
				i=0
				continue
			#if condition is not a macro name
			elif(temp[1] not in macro_list):
				#catching an exception
				try:
				#trying to evaluate condition
					x=eval(temp[1])
				#if condition is a name only then nameerror occurs
				except NameError:
					j=i+1
					#iterating through program
					while(j<len(prog)):
						temp=prog[j].split()
					#if end of macro has been found
						if(temp[0]=="endifmacro" and temp[0]!="ifmacro"):
							break
						#if another macro inside macro is present
						if(temp[0]=="ifmacro"):
						#recursive call to conditional_macros function
							conditional_macros(j)
							i=-1
							break
					j+=1
					#starting iteration again
					if(i==-1):
						i=line
						continue
					#counting number of lines to be removed
					n=j-i+1
					count=0
					while(count<n):
					#removing all lines of macro definition
						prog.remove(prog[i])
						count+=1
					i=line
					continue
				#if name error does not occur and eval returns True or False
				else:
				#if eval returned True
					if(x==True):
					#next line
						j=i+1
						while(j<len(prog)):
						#splitting line into its tokens
							temp=prog[j].split()
							#if end of macro found
							if(temp[0]=="endifmacro" and temp[0]!="ifmacro"):
								break
							#if another macro is present inside the macro
							if(temp[0]=="ifmacro"):
								conditional_macros(j)
								i=-1
								break
							j+=1
						#starting iteration again
						if(i==-1):
							i=line
							continue
						#removing macro identify lines
						prog.remove(prog[j])
						prog.remove(prog[i])
						remove()
						i=0
						continue
					#if eval returned False
					elif(x==False):
					#next line
						j=i+1
						while(j<len(prog)):
						#splitting line into its tokens
							temp=prog[j].split()
							#if end of macro found
							if(temp[0]=="endifmacro" and temp[0]!="ifmacro"):
								break
							#if another macro is present inside the macro
							if(temp[0]=="ifmacro"):
								conditional_macros(j)
								i=-1
								break
							j+=1
						#starting iteration again
						if(i==-1):
							i=line
							continue
						#counting number of lines to be removed
						n=j-i+1
						count=0
						while(count<n):
						#removing all lines of macro definition
							prog.remove(prog[i])
							count+=1
						i=line
						continue
		#if elifmacro found
		elif(temp[0]=="elifmacro"):
		#if condition is a macro name which exists
			if(temp[1] in macro_list):
				j=i+1
				while(j<len(prog)):
				#splitting line into its tokens
					temp=prog[j].split()
					#if end of macro found
					if(temp[0]=="endelifmacro" and temp[0]!="ifmacro"):
						break
					#if another macro is present inside the macro
					if(temp[0]=="ifmacro"):
						conditional_macros(j)
						i=-1
						break
					j+=1
					#starting iteration again
					if(i==-1):
						i=line
						continue
				#removing macro identify lines
				prog.remove(prog[j])
				prog.remove(prog[i])
				remove()
				i=0
				continue
			#if condition is expression or a macro name which does not exist
			elif(temp[1] not in macro_list):
				#if not an expression given eval will give nameerror
				try:
					x=eval(temp[1])
				#if nameerror occured
				except NameError:
					j=i+1
					while(j<len(prog)):
					#splitting line into its tokens
						temp=prog[j].split()
						#if end of macro found
						if(temp[0]=="endelifmacro" and temp[0]!="ifmacro"):
							break
						#if another macro present inside the macro
						if(temp[0]=="ifmacro"):
							conditional_macros(j)
							i=-1
							break
						j+=1
					#starting iteration again
					if(i==-1):
						i=line
						continue
					#counting number of lines to be removed	
					n=j-i+1
					count=0
					while(count<n):
					#removing all lines of macro definition
						prog.remove(prog[i])
						count+=1
					i=line
					continue
				#if eval returned True or False
				else:
					#if eval returned True
					if(x==True):
						j=i+1
						while(j<len(prog)):
						#splitting line into its tokens
							temp=prog[j].split()
							#if end of macro found
							if(temp[0]=="endelifmacro" and temp[0]!="ifmacro"):
								break
							#if another macro inside macro is present
							if(temp[0]=="ifmacro"):
								conditional_macros(j)
								i=-1
								break
							j+=1
						#starting iteration again
						if(i==-1):
							i=line
							continue
						#removing macro identify lines
						prog.remove(prog[j])
						prog.remove(prog[i])
						#calling remove function
						remove()
						i=0
						continue
					#if eval returned False
					elif(x==False):
						j=i+1
						while(j<len(prog)):
						#splitting line into its tokens
							temp=prog[j].split()
							#if end of macro found
							if(temp[0]=="endelifmacro" and temp[0]!="ifmacro"):
								break
							#if another macro present inside the macro
							if(temp[0]=="ifmacro"):
								conditional_macros(j)
								i=-1
								break
							j+=1
						#starting iteration again
						if(i==-1):
							i=line
							continue
						#counting number of lines to be removed
						n=j-i+1
						count=0
						while(count<n):
						#removing all lines of macro definition
							prog.remove(prog[i])
							count+=1
						i=line
						continue
		#if elsemacro found
		elif(temp[0]=="elsemacro"):
			j=i+1
			while(j<len(prog)):
				#splitting the line into its tokens
				temp=prog[j].split()
				#if end of macro found
				if(temp[0]=="endelsemacro" and temp[0]!="ifmacro"):
					break
				#if another macro present inside the macro
				if(temp[0]=="ifmacro"):
					conditional_macros(j)
					i=-1
					break
				j+=1
			#starting iteration again
			if(i==-1):
				i=line
				continue
			#removing macro identification lines
			prog.remove(prog[j])
			prog.remove(prog[i])
			remove()
			i=0
			continue	
		#iterating to next line of input program
		i+=1
	

#function to remove other conditions of a conditional macro when one of the condition is find to be true
def remove():
	i=0
	#if program is not empty
	if(len(prog)!=0):
	#splitting line into tokens
		temp=prog[i].split()
	#if another ifmacro is not present
	while(i<len(prog) and temp[0]!="ifmacro"):
		#splitting line into its tokens
		temp=prog[i].split()
		#if elifmacro needs to be removed
		if(temp[0]=="elifmacro"):
			j=i+1
			while(j<len(prog)):
			#splitting line into its tokens
				temp=prog[j].split()
				#if endelifmacro found
				if(temp[0]=="endelifmacro"):
					break
				j+=1
			#counting number of lines to be removed
			n=j-i+1
			count=0
			while(count<n):
			#removing all lines of macro definition
				prog.remove(prog[i])
				count+=1
			i=0
			continue
		#if elsemacro needs to be removed
		elif(temp[0]=="elsemacro"):
			j=i+1
			while(j<len(prog)):
			#splitting line into its tokens
				temp=prog[j].split()
				#if endelsemacro found
				if(temp[0]=="endelsemacro"):
					break
				j+=1
			#counting number of lines to be removed
			n=j-i+1
			count=0
			while(count<n):
			#removing all lines of macro definition
				prog.remove(prog[i])
				count+=1
			i=0
			continue
		i+=1


#main program starts from here

#checking whether user typed corrent command or not
if(len(sys.argv)<2):
	print("Usage: python3 macro.py <filename>")
	exit()
#getting file name , which is given as command line argument
filename=sys.argv[1]
#trying to open the  file
try:
	file=open(filename,"r")
#if try failed it means file opening failed.
except:
	print("Invalid / Non-existing file.Try Again...")
	exit()
#reading file in a list
prog=file.readlines()
#variable to store extension of program
ext=""
i=0
#variable to store name of program
name=""
#iterating till dot(.) found
while(i<len(filename) and filename[i]!='.'):
	name+=filename[i]
	i+=1
i+=1
#appending everything after dot(.) in ext string
while(i<len(filename)):
	ext+=filename[i]
	i+=1
					
#if extension is c , call cmacro function
if(ext=="c"):
	cmacro()
#if extension is py , call pymacro function
elif(ext=="py"):
	pymacro()
#if extension in asm , call asmmacro function
elif(ext=="asm"):
	asmmacro()

#writing output program into a output file of .i extension
file2=open(name+".i","w")
file2.write('\n'.join(prog))
