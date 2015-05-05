from maze import matrix
import random

class Person(object):
	def __init__(self,positionY,positionX):
		self.positionY=positionY
		self.positionX=positionX

	def checkWall(self,positionY,positionX):
		self.positionY=positionY
		self.positionX=positionX
		if(matrix[positionY][positionX]=="X"):
			return True
		else:
			return False
	
class Pacman(Person):
	def __init__(self,Y,X):
		self.Y=Y
		self.X=X		

	def collectCoin(self,positionY,positionX):
		self.positionY=positionY
		self.positionX=positionX
		if(matrix[positionY][positionX]=="C"):
			return True
		else:
			return False

class Ghost(Person):
	def __init__(self,Y,X):
		self.Y=Y
		self.X=X

	def checkGhost(self,Y,X,y,x):
		self.Y=Y
		self.X=X
		self.y=y
		self.x=x
		if (Y==y and X==x): 
			return True
		else:
			return False

	def ghostPosition(self,y,x):
		self.y=y
		self.x=x
		choicex=random.randint(-1,1)
		choicey=random.randint(-1,1)
		while(matrix[y+choicey][x+choicex]=="X" or matrix[y+choicey][x+choicex]=="C"):
			choicex=random.randint(-1,1)
			choicey=random.randint(-1,1)
		x=x+choicex
		y=y+choicey
		return [y,x]

		

