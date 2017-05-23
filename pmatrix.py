#!/usr/bin/python3
#Ver. 1.3a
import sys, os, random, string, time, shutil, termcolor, argparse

version = "1.3a"
	
class Property():
	def __init__(self, rows, cols, min_lenth_string, max_lenth_string, min_speed_symbol, max_speed_symbol):
		self.pos_first_symbol = random.randint( -(rows), -3)
		self.size_string = random.randint( min_lenth_string, max_lenth_string )
		self.speed = random.randint( min_speed_symbol, max_speed_symbol )
	
class PyMatrix():
	def __init__(self, min_lenth_string, max_lenth_string, min_speed_symbol, max_speed_symbol, delay, color, first_symbol, attrs):
		self.cols, self.rows = shutil.get_terminal_size()
		self.min_lenth_string = min_lenth_string
		self.max_lenth_string = max_lenth_string
		self.min_speed_symbol = min_speed_symbol
		self.max_speed_symbol = max_speed_symbol
		self.delay = delay
		self.color = color
		self.first_symbol = first_symbol
		self.attrs = attrs

		self.matrix = []
		for row in range(self.rows): 								
			self.matrix.append([]) 									
			for col in range(self.cols):
				self.matrix[row].append(random.choice(string.digits + string.ascii_letters + string.punctuation))

		self.properties = []
		for i in range(self.cols):
			self.properties.append(Property( 
											self.rows, 
											self.cols, 
											self.min_lenth_string, 
											self.max_lenth_string, 
											self.min_speed_symbol, 
											self.max_speed_symbol))
		self.clear()

	def render(self):
		properties = self.properties
		for row in range(self.rows):
			for col in range(self.cols): 													
				if row == properties[col].pos_first_symbol:
					sys.stdout.write(
						termcolor.colored(
							self.matrix[row][col], 
							self.first_symbol, 
							attrs = self.attrs))
				elif row < properties[col].pos_first_symbol and row > properties[col].pos_first_symbol - properties[col].size_string:
					sys.stdout.write(
						termcolor.colored(
							self.matrix[row][col],
							self.color))
				else:
					sys.stdout.write(" ")
		sys.stdout.write('\b' * self.rows * self.cols)

	def update(self):
		if self.checkResize():
			self.__init__(
				self.min_lenth_string, 
				self.max_lenth_string, 
				self.min_speed_symbol, 
				self.max_speed_symbol, 
				self.delay, 
				self.color,
				self.first_symbol,
				self.attrs)
		else:
			for property in self.properties:
				if property.pos_first_symbol - property.size_string > self.rows:
					property.pos_first_symbol = 0
					property.size_string = random.randint(self.min_lenth_string, self.max_lenth_string)
					property.speed = random.randint(self.min_speed_symbol, self.max_speed_symbol)
				else:
					property.pos_first_symbol += property.speed		

	def loop(self):
		while(True):
			self.update()
			self.render()	
			time.sleep(self.delay)
			
	def clear(self):
		if sys.platform == 'win32':								
			os.system('cls')
		else:
			os.system('clear')

	def checkResize(self):
		new_cols, new_rows = shutil.get_terminal_size()	
		if (self.rows == new_rows and self.cols == new_cols):
			return False
		else:
			return True

def createParser ():
	parser = argparse.ArgumentParser(
		prog = 'pmatrix',
		description = '''Программа, которая создает эффект матрицы.''',
		epilog = '''(c) Pavel Nedosika 2017.''',
		add_help = False)
	
	parser.add_argument(
		'--help', '-h', 
		action = 'help', 
		help = 'Справка')
	
	parser.add_argument(
		'--delay', '-d', 
		type = int, 
		default = 4, 
		choices = [0, 1, 2, 3, 4], 
		help = 'Скорость обновления матрицы')
		
	parser.add_argument(
		'--color', '-c', 
		type = str, 
		default = 'green', 
		choices = ['green', 'red', 'blue', 'white', 'yellow'], 
		help = 'Цвет всей матрицы')
		
	parser.add_argument(
		'--first_symbol', '-C',
		type = str, 
		default = 'green', 
		choices = ['green', 'red', 'blue', 'white', 'yellow'], 
		help = 'Цвет первой буквы в строках матрицы')
		
	parser.add_argument(
		'--underline', '-u', 
		action = 'store_const', 
		const = True, 
		default = False, 
		help = 'Подчеркивание первой буквы в строках матрицы')
		
	parser.add_argument(
		'--version', '-v', 
		action='version', 
		help = 'Вывести номер версии', 
		version='%(prog)s {}'.format (version))
	return parser
	
def main():
	parser = createParser()
	namespace = parser.parse_args(sys.argv[1:])
	if namespace.underline:
		attrs = ['bold', 'underline']
	else:
		attrs = ['bold']

	PyMatrix(5, 20, 1, 3, namespace.delay * 0.1, namespace.color, namespace.first_symbol, attrs).loop()
		
if __name__ == "__main__":
	main()
	
	
	
	