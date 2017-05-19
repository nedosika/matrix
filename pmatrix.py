#Ver. 1.3a
import sys, os, random, string, time, shutil, termcolor
	
class Property():
	def __init__( self, rows, cols, min_lenth_string, max_lenth_string, min_speed_symbol, max_speed_symbol ):
		self.pos_first_symbol = random.randint( -(rows), 0)
		self.size_string = random.randint( min_lenth_string, max_lenth_string )
		self.speed = random.randint( min_speed_symbol, max_speed_symbol )
	
class PyMatrix():
	rows = 0
	cols = 0
	min_lenth_string = 4 
	max_lenth_string = 20
	min_speed_symbol = 1
	max_speed_symbol = 3
	delay = 0
	infliction = [['*','#','#','#','#'],['#','#','#','#','#'],['#','#','#','#','#'],['#','#','#','#','#'],['#','#','#','#','#']]

	@staticmethod			
	def render():
		properties = PyMatrix.properties
		for row in range(PyMatrix.rows):
			for col in range(PyMatrix.cols): 													
				if row == properties[col].pos_first_symbol:
					sys.stdout.write( termcolor.colored( PyMatrix.matrix[row][col], 'green', attrs=['bold', 'underline'] ) )
				elif row < properties[col].pos_first_symbol and row > properties[col].pos_first_symbol - properties[col].size_string:
					sys.stdout.write( termcolor.colored( PyMatrix.matrix[row][col], 'green' ) )
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
			
			
	def _init_(self, min_lenth_string, max_lenth_string, min_speed_symbol, max_speed_symbol, delay ):
		PyMatrix.cols, PyMatrix.rows = shutil.get_terminal_size()
		PyMatrix.min_lenth_string = min_lenth_string
		PyMatrix.max_lenth_string = max_lenth_string
		PyMatrix.min_speed_symbol = min_speed_symbol
		PyMatrix.max_speed_symbol = max_speed_symbol
		PyMatrix.delay = delay

		PyMatrix.matrix = []
		for row in range(PyMatrix.rows): 								
			PyMatrix.matrix.append([]) 									
			for col in range(PyMatrix.cols):
				if row < 5 and col < 5:
					if PyMatrix.infliction[row][col] != " ":
						PyMatrix.matrix[row].append(PyMatrix.infliction[row][col])
					else:
						PyMatrix.matrix[row].append(random.choice(string.digits + string.ascii_letters + string.punctuation))
				else:
					PyMatrix.matrix[row].append(random.choice(string.digits + string.ascii_letters + string.punctuation))

		PyMatrix.properties = []
		for i in range( PyMatrix.cols ):
			PyMatrix.properties.append( Property( PyMatrix.rows, PyMatrix.cols, min_lenth_string, max_lenth_string, min_speed_symbol, max_speed_symbol ) )
			
		PyMatrix.clear()
	
	def loop(self):
		while(True):
			if PyMatrix.checkResize():
				self._init_(PyMatrix.min_lenth_string, PyMatrix.max_lenth_string, PyMatrix.min_speed_symbol, PyMatrix.max_speed_symbol,  PyMatrix.delay)
			else:
				PyMatrix.render()	
				PyMatrix.update()
				time.sleep(PyMatrix.delay)
	