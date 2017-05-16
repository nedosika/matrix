import sys, os, random, string, time, shutil, termcolor

def clear():
	if sys.platform=='win32':			#Очиска экрана в зависимости от ОС
		os.system('cls')
	else:
		os.system('clear')
	
COLS, ROWS = shutil.get_terminal_size()	

matrix = []
for r in range(ROWS): 					# ROW строк
    matrix.append([]) 					# создаем пустую строку
    for c in range(COLS): 				# в каждой строке - 10 элементов
        matrix[r].append("".join(random.choice(string.digits + string.ascii_letters + string.punctuation) for x in range(1))) # добавляем очередной элемент в строку	

clear()

current_col = []
for r in range(COLS):
	current_col.append([])
	for c in range(2):
		current_col[r].append([])

	current_col[r][0] = random.randint(0, ROWS) 	#Расположение светлого символа
	current_col[r][1] = random.randint(10, ROWS) 	#Длина полоски

while(1):
	j = 0
	matrix_out = []
	for r in range(ROWS): 							# перебираем все строки по номерам
		for c in range(COLS): 						# в каждой строке перебираем все столбцы по номерам
			if (j == current_col[c][0]):
				matrix_out.append(termcolor.colored(matrix[r][c], 'green', attrs=['bold']))
			else:
				if (j < current_col[c][0] and j > current_col[c][0] - current_col[c][1]):
					matrix_out.append(termcolor.colored(matrix[r][c], 'green'))
				else:
					matrix_out.append(" ")
		j += 1

	matrixString = ''
	for row in matrix_out:
		matrixString +=''.join([str(elem) for elem in row])
		
	sys.stdout.write(matrixString)
	sys.stdout.flush()
	sys.stdout.write('\b' * (ROWS)*COLS)
	sys.stdout.flush()
	
	for i in range(COLS):
		if (current_col[i][0] - current_col[i][1] > ROWS):
			current_col[i][0] = 0
			current_col[i][1] = random.randint(10, ROWS)
		else:
			current_col[i][0] += 1
	
	time.sleep(0.1)
	
	
	
	