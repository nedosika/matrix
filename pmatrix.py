#Ver. 1.2a
import sys, os, random, string, time, shutil, termcolor
	
class Property():
	pos_first_symbol = 0
	size_string = 1
	speed = 1
	
	def __init__( self, rows, cols, min_lenth_string, max_lenth_string, min_speed_symbol, max_speed_symbol ):
		Property.rows = rows
		Property.cols = cols 
		Property.min_lenth_string = min_lenth_string
		Property.max_lenth_string = max_lenth_string
		Property.min_speed_symbol = min_speed_symbol
		Property.max_speed_symbol = max_speed_symbol
		
		self.pos_first_symbol = random.randint( -(rows), -10)
		self.size_string = random.randint( min_lenth_string, max_lenth_string )
		self.speed = random.randint( min_speed_symbol, max_speed_symbol )
	
	@staticmethod
	def generate( rows, cols, min_lenth_string, max_lenth_string, min_speed_symbol, max_speed_symbol ):
		Property.properties = []
		for i in range( cols ):
			Property.properties.append( Property( rows, cols, min_lenth_string, max_lenth_string, min_speed_symbol, max_speed_symbol ) )
	
	@staticmethod		
	def update():
		for property in Property.properties:
			if property.pos_first_symbol - property.size_string > Property.rows:
				property.pos_first_symbol = 0
				property.size_string = random.randint( Property.min_lenth_string, Property.max_lenth_string )
				property.speed = random.randint( Property.min_speed_symbol, Property.max_speed_symbol )
			else:
				property.pos_first_symbol += property.speed

class PyMatrix():
	rows = 0
	cols = 0
	min_lenth_string = 4 
	max_lenth_string = 20
	min_speed_symbol = 1
	max_speed_symbol = 3
	delay = 0.4 

	@staticmethod			
	def render():
		properties = Property.properties
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
				PyMatrix.matrix[row].append(random.choice(string.digits + string.ascii_letters + string.punctuation))
		
		Property.generate( PyMatrix.rows,  PyMatrix.cols, min_lenth_string, max_lenth_string, min_speed_symbol, max_speed_symbol)
		PyMatrix.clear()
	
	def loop(self):
		while(True):
			if PyMatrix.checkResize():
				self._init_(PyMatrix.min_lenth_string, PyMatrix.max_lenth_string, PyMatrix.min_speed_symbol, PyMatrix.max_speed_symbol,  PyMatrix.delay)
			else:
				PyMatrix.render()	
				Property.update()
				time.sleep(PyMatrix.delay)
		PyMatrix.clear()
	