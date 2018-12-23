
class Display(object):
	def __init__(self, rows:int, cols:int):
		self.size = {"x":cols, "y":rows}
		self.point_map = []
		
		# Fill the point map
		for i in range(0, cols - 1):
			self.point_map.append(0)
	
	def fill(self, char:str):
		for row in range(1, self.size["y"]):
			for col in range(1, self.size["x"]):
				print(char, end="")
			print("\n", end="")
	
	def setCol(self, col:int,height:int):
		# clear last point, draw new point
		if height > self.size["y"]:
			height = self.size["y"]
		
		# clear last point
		self.__putChar(col, self.point_map[col - 1], "\u001b[0m ")
		
		# put new char
		self.__putChar(col, self.size["y"] - height, "\u001b[44m@")
		
		# add point to point map
		self.point_map[col - 1] = self.size["y"] - height
		
		# # move to bottom, work up
		# for i in range(0, height+1):
		# 	self.__putChar(col, self.size["y"] - i, "@")
	
	
	def clear(self):
		print("\033[2J", end="")
	
	def fillCorners(self):
		self.__putChar(0,0,"^")
		self.__putChar(0,self.size["y"],"^")
		self.__putChar(self.size["x"],0,"^")
		self.__putChar(self.size["x"],self.size["y"],"^")
	
	def toolTip(self, text):
		# a text box, but less effort
		self.__moveTo(5,3)
		print(text, end="")
	
	# Private
	def __putChar(self, x,y,char):
		self.__moveTo(x,y)
		print(char, end="")
	
	def __moveTo(self, x,y):
		print(f"\033[{y};{x}f", end="")