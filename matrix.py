import random, os, sys, termcolor

def clear():
	if sys.platform=='win32':							#Очиска экрана в зависимости от ОС
		os.system('cls')
	else:
		os.system('clear')
	
clear()
print(termcolor.colored("a", 'red', attrs=['bold']), end = ' ')
print(termcolor.colored("f", 'red', attrs=['bold']), end = ' ')
print(termcolor.colored("sd", 'blue', attrs=['bold']), end = ' ')
