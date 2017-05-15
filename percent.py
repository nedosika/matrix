import sys
from time import sleep
import shutil

def clear():
	if sys.platform=='win32':			#Очиска экрана в зависимости от ОС
		os.system('cls')
	else:
		os.system('clear')
	


BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)

#following from Python cookbook, #475186
def has_colours(stream):
    if not hasattr(stream, "isatty"):
        return False
    if not stream.isatty():
        return False # auto color only on TTYs
    try:
        import curses
        curses.setupterm()
        return curses.tigetnum("colors") > 2
    except:
        # guess false in case of error
        return False
has_colours = has_colours(sys.stdout)


def printout(text, colour=WHITE):
        if has_colours:
                seq = "\x1b[1;%dm" % (30+colour) + text + "\x1b[0m"
                sys.stdout.write(seq)
        else:
                sys.stdout.write(text)
	
COLS, ROWS = shutil.get_terminal_size()	
while(1):
    #sys.stdout.write('%2s%%' % i) 
    #sys.stdout.flush()
    #sleep(0.1)
    #sys.stdout.write('\b' * 3)
	#sys.stdout.write("#" * i + "-" * (40 - i) + "]" + chr(8) * 41)
	sys.stdout.write("#" * COLS * ROWS )
	#sys.stdout.flush()
	sys.stdout.write('\b' * 30)
	sys.stdout.write("p" * 3)
	
	sleep(5)
	
	
	
	
	
	