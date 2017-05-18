#Ver. 1.1a
import sys, os, random, string, time, shutil, termcolor
	
class Property():
	pos_first_symbol = 0
	size_string = 1
	speed = 1
	
	def __init__(self, rows, cols, min_lenth_string, max_lenth_string, min_speed_symbol, max_speed_symbol):
		Property.rows = rows
		Property.cols = cols 
		Property.min_lenth_string = min_lenth_string
		Property.max_lenth_string = max_lenth_string
		Property.min_speed_symbol = min_speed_symbol
		Property.max_speed_symbol = max_speed_symbol
		
		self.pos_first_symbol = random.randint(0, rows)
		self.size_string = random.randint(min_lenth_string, max_lenth_string)
		self.speed = random.randint(min_speed_symbol, max_speed_symbol)
	
	@staticmethod
	def generate(rows, cols, min_lenth_string, max_lenth_string, min_speed_symbol, max_speed_symbol):
		Property.properties = []
		for i in range(cols):
			Property.properties.append(Property(rows, cols, min_lenth_string, max_lenth_string, min_speed_symbol, max_speed_symbol))
	
	@staticmethod		
	def update():
		for property in Property.properties:
			if (property.pos_first_symbol - property.size_string > Property.rows):
				property.pos_first_symbol = 0
				property.size_string = random.randint(Property.min_lenth_string, Property.max_lenth_string)
				property.speed = random.randint(Property.min_speed_symbol, Property.max_speed_symbol)
			else:
				property.pos_first_symbol += property.speed
				
MIN_LENTH_STRING = 3
MAX_LENTH_STRING = 20
MAX_SPEED_SYMBOL = 3
MIN_SPEED_SYMBOL = 1
DELAY = 0

cols, rows = shutil.get_terminal_size()
matrix = []

def clear():
	if sys.platform=='win32':								
		os.system('cls')
	else:
		os.system('clear')
		
def render():		
	for row in range(rows):
		for col in range(cols): 													
			if (row == Property.properties[col].pos_first_symbol):
				sys.stdout.write(termcolor.colored(matrix[row][col], 'green', attrs=['bold', 'underline']))
			elif (row < Property.properties[col].pos_first_symbol and row > Property.properties[col].pos_first_symbol - Property.properties[col].size_string):
				sys.stdout.write(termcolor.colored(matrix[row][col], 'green'))
			else:
				sys.stdout.write(" ")

	sys.stdout.flush() #При дбавлении перестает быть сильно заметен курсор)))
	sys.stdout.write('\b' * rows * cols)

def generateMatrix():	
	global matrix
	matrix = []
	for row in range(rows): 								
		matrix.append([]) 									
		for col in range(cols): 							
			matrix[row].append(random.choice(string.digits + string.ascii_letters + string.punctuation))

def checkResize():
	new_cols, new_rows = shutil.get_terminal_size()	
	if (rows == new_rows and cols == new_cols):
		return False
	else:
		return True
			
def loop():
	global rows
	global cols
	while(rows > 5 and cols > 15):
		if checkResize():
			clear()
			cols, rows = shutil.get_terminal_size()
			matrix = generateMatrix()
			Property.generate(rows, cols, MIN_LENTH_STRING, MAX_LENTH_STRING, MIN_SPEED_SYMBOL, MAX_SPEED_SYMBOL)
		else:
			render()	
			Property.update()
			time.sleep(DELAY)
	clear()

clear()
generateMatrix()
Property.generate(rows, cols, MIN_LENTH_STRING, MAX_LENTH_STRING, MIN_SPEED_SYMBOL, MAX_SPEED_SYMBOL)
loop()




	