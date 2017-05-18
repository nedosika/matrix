#Ver. 1.1a
import sys, os, random, string, time, shutil, termcolor
	
class Property():
	properties = []
	rows = 0
	cols = 0 
	min_lenth_string = 1
	max_lenth_string = 1
	min_speed_symbol = 1
	max_speed_symbol = 1
	
	pos_first_symbol = 0
	size_string = 1
	speed = 1
	
	def __init__(self, rows, cols, min_lenth_string, max_lenth_string, min_speed_symbol, max_speed_symbol):
		__class__.rows = rows
		__class__.cols = cols 
		__class__.min_lenth_string = min_lenth_string
		__class__.max_lenth_string = max_lenth_string
		__class__.min_speed_symbol = min_speed_symbol
		__class__.max_speed_symbol = max_speed_symbol
		
		self.pos_first_symbol = random.randint(0, rows)
		self.size_string = random.randint(min_lenth_string, max_lenth_string)
		self.speed = random.randint(min_speed_symbol, max_speed_symbol)
	
	@staticmethod
	def generate(rows, cols, min_lenth_string, max_lenth_string, min_speed_symbol, max_speed_symbol):
		#__class__.properties = []
		for i in range(cols):
			__class__.properties.append(Property(rows, cols, min_lenth_string, max_lenth_string, min_speed_symbol, max_speed_symbol))
			#new = Property(rows, cols, min_lenth_string, max_lenth_string, min_speed_symbol, max_speed_symbol )
	
	@staticmethod		
	def update():
		for property in __class__.properties:
			if (property.pos_first_symbol - property.size_string > __class__.rows):
				property.pos_first_symbol = 0
				property.size_string = random.randint(__class__.min_lenth_string, __class__.max_lenth_string)
				property.speed = random.randint(__class__.min_speed_symbol, __class__.max_speed_symbol)
			else:
				property.pos_first_symbol += property.speed
				
MIN_LENTH_STRING = 3
MAX_LENTH_STRING = 20
MAX_SPEED_SYMBOL = 3
MIN_SPEED_SYMBOL = 1
DELAY = 0

cols, rows = shutil.get_terminal_size()
matrix = []
matrix_properties = []

def clear():
	if sys.platform=='win32':								
		os.system('cls')
	else:
		os.system('clear')
		
def render():		
	i = 0
	out_str = ""
	for row in range(rows):
		for col in range(cols): 													
			if (i == matrix_properties[col]['posFirstSymbol']):
				sys.stdout.write(termcolor.colored(matrix[row][col], 'green', attrs=['bold', 'underline']))
			elif (i < matrix_properties[col]['posFirstSymbol'] and i > matrix_properties[col]['posFirstSymbol'] - matrix_properties[col]['sizeString']):
				sys.stdout.write(termcolor.colored(matrix[row][col], 'green'))
			else:
				sys.stdout.write(" ")
		i += 1
	
	sys.stdout.flush() #При дбавлении перестает быть сильно заметен курсор)))
	sys.stdout.write('\b' * rows * cols)

def generateMatrix():	
	global matrix
	matrix = []
	for row in range(rows): 								
		matrix.append([]) 									
		for col in range(cols): 							
			matrix[row].append(random.choice(string.digits + string.ascii_letters + string.punctuation))

def generateProperties():
	global matrix_properties
	matrix_properties = []
	for i in range(cols):
		matrix_properties.append(dict())
		matrix_properties[i]['posFirstSymbol'] = random.randint(0, rows)
		matrix_properties[i]['sizeString'] = random.randint(MIN_LENTH_STRING, MAX_LENTH_STRING)
		matrix_properties[i]['speed'] = random.randint(MIN_SPEED_SYMBOL, MAX_SPEED_SYMBOL)
	
def updateProperties():
	for i in range(cols):
		if (matrix_properties[i]['posFirstSymbol'] - matrix_properties[i]['sizeString'] > rows):
			matrix_properties[i]['posFirstSymbol'] = 0
			matrix_properties[i]['sizeString'] = random.randint(MIN_LENTH_STRING, MAX_LENTH_STRING)
			matrix_properties[i]['speed'] = random.randint(MIN_SPEED_SYMBOL, MAX_SPEED_SYMBOL)
		else:
			matrix_properties[i]['posFirstSymbol'] += matrix_properties[i]['speed']

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
			matrix_properties = generateProperties()
		else:
			render()	
			matrix_properties = updateProperties()
			time.sleep(DELAY)
	clear()

clear()
generateMatrix()
generateProperties()
Property.generate(rows, cols, MIN_LENTH_STRING, MAX_LENTH_STRING, MAX_SPEED_SYMBOL, MIN_SPEED_SYMBOL)
loop()




	