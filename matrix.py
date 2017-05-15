import random, os, sys, termcolor
import msvcrt
import string
import time

def clear():
	if sys.platform=='win32':							#Очиска экрана в зависимости от ОС
		os.system('cls')
	else:
		os.system('clear')
	
ROWS = 20
COLS = 60	
	
clear()
#print(termcolor.colored("a", 'green'), end = ' ')
#print(termcolor.colored("f", 'red', attrs=['bold']), end = ' ')
#print(termcolor.colored("sd", 'blue', attrs=['bold']), end = ' ')
a = []
for r in range(ROWS): 				# ROW строк
    a.append([]) 					# создаем пустую строку
    for c in range(COLS): 			# в каждой строке - 10 элементов
        a[r].append("".join(random.choice(string.digits + string.ascii_letters + string.punctuation) for x in range(1))) # добавляем очередной элемент в строку	
	
array = [COLS]	
	
while (1):
	for r in range(ROWS): 				# перебираем все строки по номерам
		for c in range(COLS): 			# в каждой строке перебираем все столбцы по номерам
			print(termcolor.colored(a[r][c], 'green', attrs=['bold']), end = ' ')
		print()
	time.sleep(1)
	clear()



