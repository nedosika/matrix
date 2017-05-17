#Ver. 1.1a
import sys, os, random, string, time, shutil, termcolor
	
MIN_LENTH_STRING = 3
MAX_LENTH_STRING = 20
MAX_SPEED_SYMBOL = 3
MIN_SPEED_SYMBOL = 1
DELAY = 0

cols, rows = shutil.get_terminal_size()
array_current_column = []

def clear():
	if sys.platform=='win32':								#Очиска экрана в зависимости от ОС
		os.system('cls')
	else:
		os.system('clear')
		
def render(out_string):
	sys.stdout.write(out_string)
	sys.stdout.write('\b' * rows * cols)

def generateMatrix():
	matrix = []
	for row in range(rows): 								#ROW строк
		matrix.append([]) 									#создаем пустую строку
		for col in range(cols): 							#в каждой строке - cols элементов
			matrix[row].append(random.choice(string.digits + string.ascii_letters + string.punctuation)) # добавляем очередной элемент в строку	
	return matrix

def generateRndPosLS():
	global array_current_column
	array_current_column = []
	for i in range(cols):
		array_current_column.append([])
		for j in range(3):
			array_current_column[i].append([])
		array_current_column[i][0] = random.randint(0, rows) 									#Случайное расположение светлого символа
		array_current_column[i][1] = random.randint(MIN_LENTH_STRING, MAX_LENTH_STRING) 		#Размер полосы символов
		array_current_column[i][2] = random.randint(MIN_SPEED_SYMBOL, MAX_SPEED_SYMBOL)		#Максимальная скорость
	
def generateOutString(matrix):
	j = 0
	out_str = ""
	
	for row in range(rows): 														#Перебираем все строки по номерам
		for col in range(cols): 													#В каждой строке перебираем все столбцы по номерам
			if (j == array_current_column[col][0]):
				out_str += termcolor.colored(matrix[row][col], 'green', attrs=['bold'])
			elif (j < array_current_column[col][0] and j > array_current_column[col][0] - array_current_column[col][1]):
				out_str += termcolor.colored(matrix[row][col], 'green')
			else:
				out_str += " "
		j += 1
		
	return out_str
	
def updateArrCurCol():
	for i in range(cols):
		if (array_current_column[i][0] - array_current_column[i][1] > rows):
			array_current_column[i][0] = 0
			array_current_column[i][1] = random.randint(MIN_LENTH_STRING, MAX_LENTH_STRING)
			array_current_column[i][2] = random.randint(MIN_SPEED_SYMBOL, MAX_SPEED_SYMBOL)
		else:
			array_current_column[i][0] += array_current_column[i][2]

def loop(matrix):
	global rows
	global cols
	while(1):
		new_cols, new_rows = shutil.get_terminal_size()	
		if (rows == new_rows and cols == new_cols):								#Проверяем не изменился ли размер консоли
			render(generateOutString(matrix))	
			array_current_column = updateArrCurCol()
			time.sleep(DELAY)
		else:
			clear()
			cols, rows = shutil.get_terminal_size()
			matrix = generateMatrix()
			array_current_column = generateRndPosLS()

clear()
generateRndPosLS()
loop(generateMatrix())




	