#Ver. 1.1a
import sys, os, random, string, time, shutil, termcolor
	
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
loop()




	