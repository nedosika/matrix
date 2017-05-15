import random, os, sys, termcolor
import string
import time
import shutil

def clear():
	if sys.platform=='win32':			#Очиска экрана в зависимости от ОС
		os.system('cls')
	else:
		os.system('clear')
	
ROWS = 55
COLS = 78	

clear()

matrix = []
for r in range(ROWS): 					# ROW строк
    matrix.append([]) 					# создаем пустую строку
    for c in range(COLS): 				# в каждой строке - 10 элементов
        matrix[r].append("".join(random.choice(string.digits + string.ascii_letters + string.punctuation) for x in range(1))) # добавляем очередной элемент в строку	
	
current_col = []
for r in range(COLS):
	current_col.append([])
	for c in range(2):
		current_col[r].append([])

	current_col[r][0] = random.randint(0, ROWS + ROWS) 	#Расположение светлого символа
	current_col[r][1] = random.randint(10, ROWS) 		#Длина полоски
		
ROW, COLS = shutil.get_terminal_size((60, 40))

while (1):
	j = 0
	for r in range(ROWS): 				# перебираем все строки по номерам
		for c in range(COLS): 			# в каждой строке перебираем все столбцы по номерам
			if (j == current_col[c][0]):
				print(termcolor.colored(matrix[r][c], 'green', attrs=['bold']), end = ' ')
			else:
				if (j < current_col[c][0] and j > current_col[c][0] - current_col[c][1]):
					print(termcolor.colored(matrix[r][c], 'green'), end = ' ')
				else:
					print(" ", end = ' ')
		print()
		j += 1

	for i in range(COLS):
		if (current_col[i][0] - current_col[c][1] > ROWS):
			current_col[i][0] = 0
			current_col[i][1] = random.randint(7, ROWS)
		else:
			current_col[i][0] += 1
	
	ROW, COLS = shutil.get_terminal_size((60, 40))

	time.sleep(1)

	clear()
		



