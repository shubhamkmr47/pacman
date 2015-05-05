from maze import matrix,density
from classes import Person,Pacman,Ghost
import random,time

class bcolors:
    HEADER = '\033[95m'
    blue = '\033[94m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    end= '\033[0m'

class _Getch:
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()


class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()


getch = _Getch()

x=10
y=14
score=0
pacman=Pacman(y,x)
matrix[y][x]="P"

x1=2
y1=2
ghost1=Ghost(y1,x1)
matrix[y1][x1]="G"

x2=20
y2=9
ghost2=Ghost(y2,x2)
matrix[y2][x2]="G"

x3=20
y3=21
ghost3=Ghost(y3,x3)
matrix[y3][x3]="G"

y4=18
x4=10
ghost4=Ghost(y4,x4)
matrix[y4][x4]="G"

for p in range(0,25):
	for q in range(0,37):
		if matrix[p][q]=="C":
			print bcolors.yellow+matrix[p][q]+bcolors.end,
		elif matrix[p][q]=="G":
			print bcolors.red+matrix[p][q]+bcolors.end,
		elif matrix[p][q]=="P":
			print bcolors.blue+matrix[p][q]+bcolors.end,
		else:
			print matrix[p][q],
	

	print "\n",
print "score:"+str(score)

#command=raw_input("move:")
command=getch()
print "move:",
command=command[0]
print command

while command!="q":
	if command=="w":
		if pacman.checkWall(y-1,x)==True:
			print "Cannot move!!!"
		else:
			matrix[y][x]="."
			y=y-1
	elif command=="s":
		if pacman.checkWall(y+1,x)==True:
			print "Cannot move!!!"
		else:
			matrix[y][x]="."
			y=y+1
	elif command=="a":
		if pacman.checkWall(y,x-1)==True:
			print "Cannot move!!!"
		else:				
			matrix[y][x]="."
			x=x-1
	elif command=="d":
		if pacman.checkWall(y,x+1)==True:
			print "Cannot move!!!"
		else:
			matrix[y][x]="."
			x=x+1
	if pacman.collectCoin(y,x)==True:
		score=score+1
	
	
	T=ghost1.ghostPosition(y1,x1)
	b=T[0]
	a=T[1]
	if matrix[y1][x1]!="P" or matrix[y1][x1]!="G":
		matrix[y1][x1]="."
	y1=b
	x1=a
	matrix[y1][x1]="G"

	T=ghost2.ghostPosition(y2,x2)
	b=T[0]
	a=T[1]
	if matrix[y2][x2]!="P" or matrix[y2][x2]!="G":
		matrix[y2][x2]="."
	y2=b
	x2=a
	matrix[y2][x2]="G"
	
	T=ghost3.ghostPosition(y3,x3)
	b=T[0]
	a=T[1]
	if matrix[y3][x3]!="P" or matrix[y3][x3]!="G":
		matrix[y3][x3]="."
	y3=b
	x3=a
	matrix[y3][x3]="G"

	T=ghost4.ghostPosition(y4,x4)
	b=T[0]
	a=T[1]
	if matrix[y4][x4]!="P" or matrix[y4][x4]!="G":
		matrix[y4][x4]="."
	y4=b
	x4=a
	matrix[y4][x4]="G"
	
	matrix[y][x]="P"

	for p in range(0,25):
		for q in range(0,37):
			if matrix[p][q]=="C":
				print bcolors.yellow+matrix[p][q]+bcolors.end,
			elif matrix[p][q]=="G":
				print bcolors.red+matrix[p][q]+bcolors.end,
			elif matrix[p][q]=="P":
				print bcolors.blue+matrix[p][q]+bcolors.end,
			else:
				print matrix[p][q],
		print "\n",

	print "score:"+str(score)
	if (ghost1.checkGhost(y,x,y1,x1)==True or ghost2.checkGhost(y,x,y2,x2)==True or
	 ghost3.checkGhost(y,x,y3,x3)==True or ghost4.checkGhost(y,x,y4,x4)==True):
		matrix[y][x]="G"
		print "You Lose!!!"
		break
	if density==score:
		print "You Win!!!"
		break
	#command=raw_input("move:")
	print "move:",
	command=getch()
	command=command[0]
	print command

for p in range(0,25):
		for q in range(0,37):
			if matrix[p][q]=="C":
				print bcolors.yellow+matrix[p][q]+bcolors.end,
			elif matrix[p][q]=="G":
				print bcolors.red+matrix[p][q]+bcolors.end,
			elif matrix[p][q]=="P":
				print bcolors.blue+matrix[p][q]+bcolors.end,
			else:
				print matrix[p][q],
		print "\n",
print "Total score:"+str(score)
