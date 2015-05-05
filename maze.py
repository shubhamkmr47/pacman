import random

height=25
width=37

matrix=[]
for p in range(0,height):
	matrix.append([]) 

for p in range(0,height):
	for q in range(0,width):
		matrix[p].append(".")
		if p==0 or q==0 or p==height-1 or q==width-1:
			matrix[p][q]="X"

for i in range(0,30):
	matrix[12][i]="X"
for i in range(0,10):
	matrix[i][12]="X"
for i in range(0,16):
	matrix[i+5][24]="X"

def line1(p,q):
	for i in range(0,8):
		matrix[p+i][q]="X"

def line2(p,q):
	for i in range(0,4):
		matrix[p][q+i]="X"

def line3(p,q):
	for i in range(0,3):
		matrix[p+5][q+i]="X"

def line4(p,q):
	for i in range(0,7):
		matrix[p+i][q+5]="X"
		matrix[p+i][q+6]="X"

def line5(p,q):
	for i in range(0,5):
		matrix[p+3][q+i]="X"

def line6(p,q):
	for i in range(0,2):
		matrix[p+i][q+3]="X"

def position(c):
	if(c==1):
		return [3,3]
	elif(c==2):
		return [3,15]
	elif(c==3):
		return [3,27]
	elif(c==4):
		return [15,3]
	elif(c==5):
		return [15,15]
	elif(c==6):
		return [15,27]
	
chance=30

for i in range(0,chance):
	case=random.randint(1,6)
	if case==1:
		t=random.randint(1,6)
		pos=position(t)
		line1(pos[0],pos[1])
	elif case==2:
		t=random.randint(1,6)
		pos=position(t)
		line2(pos[0],pos[1])
	elif case==3:
		t=random.randint(1,6)
		pos=position(t)
		line3(pos[0],pos[1])
	elif case==5:
		t=random.randint(1,6)
		pos=position(t)
		line5(pos[0],pos[1])

density=20
i=0
while i<density:
	x=random.randint(1,36)
	y=random.randint(1,24)
	if matrix[y][x]!="X":
		matrix[y][x]="C"
		i=i+1
		  
#for p in range(0,height):
#	for q in range(0,width):
#		print matrix[p][q],
#	print "\n",