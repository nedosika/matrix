import sys, os, random, string, time, shutil, termcolor

def clear():
	if sys.platform=='win32':			#Очиска экрана в зависимости от ОС
		os.system('cls')
	else:
		os.system('clear')
		
def render(matrix, rows, cols):
	out_string = ''
	for row in matrix:
		out_string +=''.join([str(elem) for elem in row])
		
	sys.stdout.write(out_string)
	sys.stdout.flush()
	sys.stdout.write('\b' * rows * cols)
	sys.stdout.flush()

def createRndMatrix(rows, cols):
	matrix = []
	for row in range(rows): 					# ROW строк
		matrix.append([]) 					# создаем пустую строку
		for col in range(cols): 				# в каждой строке - 10 элементов
			matrix[row].append("".join(random.choice(string.digits + string.ascii_letters + string.punctuation) for x in range(1))) # добавляем очередной элемент в строку	
	return matrix

def createRndPosLS():
	current_col = []

	for r in range(COLS):
		current_col.append([])
		for c in range(2):
			current_col[r].append([])

		current_col[r][0] = random.randint(0, ROWS) 	#Расположение светлого символа
		current_col[r][1] = random.randint(10, ROWS) 	#Длина полоски
	return current_col
	
clear()
	
COLS, ROWS = shutil.get_terminal_size()	

matrix = createRndMatrix(ROWS, COLS)

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

	render(matrix_out, ROWS, COLS)	
	
	for i in range(COLS):
		if (current_col[i][0] - current_col[i][1] > ROWS):
			current_col[i][0] = 0
			current_col[i][1] = random.randint(10, ROWS)
		else:
			current_col[i][0] += 1
	
	time.sleep(0.1)
	
	
	
	