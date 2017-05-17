#Ver. 2.0a

import sys, os, random, string, time, shutil, termcolor

class Matrix():
	min_lenth_string = 1
	max_speed_string = 1
	delay = 0
	rows = 0
	cols = 0
	matrix = []
	array_current_column = []	#Массив с текущими настроками для каждой строки матрицы

	
	def __init__(self, min_lenth_string, max_speed_string, delay):
		self.cols, self.rows = shutil.get_terminal_size()	
		self.createArrCurCol()
		
	
	def createRndMatrix(self):
		for row in range(self.rows): 								#ROW строк
			self.matrix.append([]) 									#создаем пустую строку
			for col in range(self.cols): 							#в каждой строке - cols элементов
				self.matrix[row].append(random.choice(string.digits + string.ascii_letters + string.punctuation)) # добавляем очередной элемент в строку	
				
	def checkResize(self):
		new_cols, new_rows = shutil.get_terminal_size()
		if (new_rows == self.rows and new_cols == self.cols):
			return False
		else:
			return True
		
	def createArrCurCol(self):
		for row in range(self.cols):
			self.array_current_column.append([])
			for col in range(3):
				self.array_current_column[row].append([])

			self.array_current_column[row][0] = random.randint(0, self.rows) 		#Случайное расположение светлого символа
			self.array_current_column[row][1] = random.randint(self.min_lenth_string, self.rows) 	#Минимальная длина полоски
			self.array_current_column[row][2] = random.randint(1, self.max_speed_string)	#Максимальная скорость
		
	def updateOutMatrix(self):
		j = 0
		matrix_out = []
		for r in range(self.rows): 									#Перебираем все строки по номерам
			for c in range(self.cols): 								#В каждой строке перебираем все столбцы по номерам
				if (j == self.array_current_column[c][0]):
					self.array_current_column.append(termcolor.colored(self.matrix[r][c], 'green', attrs=['bold']))
				elif (j < self.array_current_column[c][0] and j > self.array_current_column[c][0] - self.array_current_column[c][1]):
					matrix_out.append(termcolor.colored(self.matrix[r][c], 'green'))
				else:
					matrix_out.append(" ")
			j += 1
		return matrix_out
	
	def render(self):
		out_string = ''
		for row in self.updateOutMatrix():
			out_string +=''.join([str(elem) for elem in row])

		sys.stdout.write(out_string)
		sys.stdout.write('\b' * self.rows * self.cols)
			
	def loop(self):
		self.createRndMatrix()
		while(True):
			if(self.checkResize()):
				
				pass
			else:
				self.render()
				pass
			

	
	def clear(self):			#Очиска экрана в зависимости от ОС
		if sys.platform=='win32':								
			os.system('cls')
		else:
			os.system('clear')
		
MIN_LENTH_STRING = 0
MAX_SPEED_STRING = 3
DELAY = 0

matrix = Matrix(MIN_LENTH_STRING, MAX_SPEED_STRING, DELAY)
matrix.loop()




