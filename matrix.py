#Ver. 1.0

import sys, os, random, string, time, shutil, termcolor

def clear():
	if sys.platform=='win32':								#Очиска экрана в зависимости от ОС
		os.system('cls')
	else:
		os.system('clear')
		
def render(matrix, rows, cols):
	out_string = ''
	for row in matrix:
		out_string +=''.join([str(elem) for elem in row])
		
	sys.stdout.write(out_string)
	#sys.stdout.flush()
	sys.stdout.write('\b' * rows * cols)

def createRndMatrix(rows, cols):
	matrix = []
	for row in range(rows): 								#ROW строк
		matrix.append([]) 									#создаем пустую строку
		for col in range(cols): 							#в каждой строке - cols элементов
			matrix[row].append(random.choice(string.digits + string.ascii_letters + string.punctuation)) # добавляем очередной элемент в строку	
	return matrix

def createRndPosLS(rows, cols, lenth, max_speed):
	current_col = []

	for row in range(cols):
		current_col.append([])
		for col in range(3):
			current_col[row].append([])

		current_col[row][0] = random.randint(0, rows) 		#Случайное расположение светлого символа
		current_col[row][1] = random.randint(lenth, rows) 	#Минимальная длина полоски
		current_col[row][2] = random.randint(1, max_speed)	#Максимальная скорость
	return current_col
	
def updateOutMatrix(matrix, rows, cols, current_col):
	j = 0
	matrix_out = []
	for r in range(rows): 									#Перебираем все строки по номерам
		for c in range(cols): 								#В каждой строке перебираем все столбцы по номерам
			if (j == current_col[c][0]):
				matrix_out.append(termcolor.colored(matrix[r][c], 'green', attrs=['bold']))
			elif (j < current_col[c][0] and j > current_col[c][0] - current_col[c][1]):
				matrix_out.append(termcolor.colored(matrix[r][c], 'green'))
			else:
				matrix_out.append(" ")
		j += 1
	return matrix_out
	
def updateCurCol(current_col, rows, cols, lenth, max_speed):
	for i in range(cols):
		if (current_col[i][0] - current_col[i][1] > rows):
			current_col[i][0] = 0
			current_col[i][1] = random.randint(lenth, rows)
			current_col[i][2] = random.randint(1, max_speed)
		else:
			current_col[i][0] += current_col[i][2]
	return current_col

def loop(matrix, rows, cols, min_lenth_string, max_speed_symbol, current_col):
	while(1):
		new_cols, new_rows = shutil.get_terminal_size()	
		if (rows == new_rows and cols == new_cols):								#Проверяем не изменился ли размер консоли
			matrix_out = updateOutMatrix(matrix, rows, cols, current_col)
			render(matrix_out, rows, cols)	
			current_col = updateCurCol(current_col, rows, cols, min_lenth_string, max_speed_symbol)
			time.sleep(DELAY)
		else:
			clear()
			cols, rows = shutil.get_terminal_size()
			matrix = createRndMatrix(rows, cols)
			current_col = createRndPosLS(rows, cols, min_lenth_string, max_speed_symbol)
	
COLS, ROWS = shutil.get_terminal_size()	
MIN_LENTH_STRING = 0
MAX_SPEED_SYMBOL = 3
DELAY = 0

clear()
matrix = createRndMatrix(ROWS, COLS)
current_col = createRndPosLS(ROWS, COLS, MIN_LENTH_STRING, MAX_SPEED_SYMBOL)
loop(matrix, ROWS, COLS, MIN_LENTH_STRING, MAX_SPEED_SYMBOL, current_col)

	