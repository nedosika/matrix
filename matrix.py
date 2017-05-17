#Ver. 1.1a
import sys, os, random, string, time, shutil, termcolor
	
MIN_LENTH_STRING = 3
MAX_LENTH_STRING = 20
MAX_SPEED_SYMBOL = 3
MIN_SPEED_SYMBOL = 1
DELAY = 0

cols, rows = shutil.get_terminal_size()
array_positions = []

def clear():
	if sys.platform=='win32':								
		os.system('cls')
	else:
		os.system('clear')
		
def render(matrix):		
	i = 0
	out_str = ""
	for row in range(rows):
		for col in range(cols): 													
			if (i == array_positions[col]['rndLightSymbol']):
				sys.stdout.write(termcolor.colored(matrix[row][col], 'green', attrs=['bold', 'underline']))
			elif (i < array_positions[col]['rndLightSymbol'] and i > array_positions[col]['rndLightSymbol'] - array_positions[col]['sizeString']):
				sys.stdout.write(termcolor.colored(matrix[row][col], 'green'))
			else:
				sys.stdout.write(" ")
		i += 1
	
	sys.stdout.flush() #При дбавлении перестает быть сильно заметен курсор)))
	sys.stdout.write('\b' * rows * cols)
	

def generateMatrix():	
	matrix = []
	for row in range(rows): 								
		matrix.append([]) 									
		for col in range(cols): 							
			matrix[row].append(random.choice(string.digits + string.ascii_letters + string.punctuation))
	return matrix

def generatePositions():
	global array_positions
	array_positions = []
	for i in range(cols):
		array_positions.append(dict())
		array_positions[i]['rndLightSymbol'] = random.randint(0, rows)
		array_positions[i]['sizeString'] = random.randint(MIN_LENTH_STRING, MAX_LENTH_STRING)
		array_positions[i]['speed'] = random.randint(MIN_SPEED_SYMBOL, MAX_SPEED_SYMBOL)
	
def updatePositions():
	for i in range(cols):
		if (array_positions[i]['rndLightSymbol'] - array_positions[i]['sizeString'] > rows):
			array_positions[i]['rndLightSymbol'] = 0
			array_positions[i]['sizeString'] = random.randint(MIN_LENTH_STRING, MAX_LENTH_STRING)
			array_positions[i]['speed'] = random.randint(MIN_SPEED_SYMBOL, MAX_SPEED_SYMBOL)
		else:
			array_positions[i]['rndLightSymbol'] += array_positions[i]['speed']

def checkResize():
	new_cols, new_rows = shutil.get_terminal_size()	
	if (rows == new_rows and cols == new_cols):
		return False
	else:
		return True
			
def loop(matrix):
	global rows
	global cols
	while(1):
		if checkResize():
			clear()
			cols, rows = shutil.get_terminal_size()
			matrix = generateMatrix()
			array_positions = generatePositions()
		else:
			render(matrix)	
			array_positions = updatePositions()
			time.sleep(DELAY)

clear()
generatePositions()
loop(generateMatrix())




	