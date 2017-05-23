#Ver. 1.3a
import sys, os, random, string, time, shutil, termcolor, argparse

version = "1.3a"
	
class Property():
	def __init__( self, rows, cols, min_lenth_string, max_lenth_string, min_speed_symbol, max_speed_symbol ):
		self.pos_first_symbol = random.randint( -(rows), -3)
		self.size_string = random.randint( min_lenth_string, max_lenth_string )
		self.speed = random.randint( min_speed_symbol, max_speed_symbol )
	
class PyMatrix():

	@staticmethod			
	def render():
		properties = PyMatrix.properties
		for row in range(PyMatrix.rows):
			for col in range(PyMatrix.cols): 													
				if row == properties[col].pos_first_symbol:
					sys.stdout.write( termcolor.colored( PyMatrix.matrix[row][col], PyMatrix.color, attrs = PyMatrix.attrs ) )
				elif row < properties[col].pos_first_symbol and row > properties[col].pos_first_symbol - properties[col].size_string:
					sys.stdout.write( termcolor.colored( PyMatrix.matrix[row][col], PyMatrix.color ) )
				else:
					sys.stdout.write( " " )
		sys.stdout.write('\b' * PyMatrix.rows * PyMatrix.cols)
	
	@staticmethod
	def clear():
		if sys.platform=='win32':								
			os.system('cls')
		else:
			os.system('clear')

	@staticmethod
	def checkResize():
		new_cols, new_rows = shutil.get_terminal_size()	
		if (PyMatrix.rows == new_rows and PyMatrix.cols == new_cols):
			return False
		else:
			return True
			
	@staticmethod		
	def update():
		for property in PyMatrix.properties:
			if property.pos_first_symbol - property.size_string > PyMatrix.rows:
				property.pos_first_symbol = 0
				property.size_string = random.randint( PyMatrix.min_lenth_string, PyMatrix.max_lenth_string )
				property.speed = random.randint( PyMatrix.min_speed_symbol, PyMatrix.max_speed_symbol )
			else:
				property.pos_first_symbol += property.speed		
			
	def __init__(self, min_lenth_string, max_lenth_string, min_speed_symbol, max_speed_symbol, delay, color, attrs):
		PyMatrix.cols, PyMatrix.rows = shutil.get_terminal_size()
		PyMatrix.min_lenth_string = min_lenth_string
		PyMatrix.max_lenth_string = max_lenth_string
		PyMatrix.min_speed_symbol = min_speed_symbol
		PyMatrix.max_speed_symbol = max_speed_symbol
		PyMatrix.delay = delay
		PyMatrix.color = color
		PyMatrix.attrs = attrs

		PyMatrix.matrix = []
		for row in range(PyMatrix.rows): 								
			PyMatrix.matrix.append([]) 									
			for col in range(PyMatrix.cols):
				PyMatrix.matrix[row].append(random.choice(string.digits + string.ascii_letters + string.punctuation))

		PyMatrix.properties = []
		for i in range( PyMatrix.cols ):
			PyMatrix.properties.append( Property( PyMatrix.rows, PyMatrix.cols, min_lenth_string, max_lenth_string, min_speed_symbol, max_speed_symbol ) )
			
		PyMatrix.clear()
	
	def loop(self):
		while(True):
			if PyMatrix.checkResize():
				self.__init__(PyMatrix.min_lenth_string, PyMatrix.max_lenth_string, PyMatrix.min_speed_symbol, PyMatrix.max_speed_symbol, PyMatrix.delay, PyMatrix.color, PyMatrix.attrs)
			else:
				PyMatrix.update()
				PyMatrix.render()	
				time.sleep(PyMatrix.delay)

def createParser ():
	parser = argparse.ArgumentParser(
		prog = 'pmatrix',
		description = '''Программа, которая создает эффект матрицы.''',
		epilog = '''(c) Pavel Nedosika 2017.''')
	parser.add_argument ('-d', '--delay', type = int, default = 4, choices = [0, 1, 2, 3, 4], help = 'Скорость обновления матрицы')
	parser.add_argument ('-c', '--color', type = str, default = 'green', choices = ['green', 'red', 'blue', 'white', 'yellow'], help = 'Цвет всей матрицы')
	parser.add_argument ('-C', type = str, default = 'green', choices = ['green', 'red', 'blue', 'white', 'yellow'], help = 'Цвет первой буквы в строках матрицы')
	parser.add_argument ('-u', '--underline', action = 'store_const', const = True, default = False, help = 'Подчеркивание первой буквы в строках матрицы')
	parser.add_argument ('-v', '--version', action='version', help = 'Вывести номер версии', version='%(prog)s {}'.format (version))
	return parser
	
def main():
	parser = createParser()
	namespace = parser.parse_args(sys.argv[1:])
	if namespace.underline:
		attrs = ['bold', 'underline']
	else:
		attrs = ['bold']
	PyMatrix(5, 20, 1, 3, namespace.delay * 0.1, namespace.color, attrs).loop()
		
if __name__ == "__main__":
	main()
	
	
	
	