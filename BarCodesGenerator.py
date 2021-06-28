import turtle

Screen = turtle.Screen()

def CreateWindow(x_setup, y_setup, _color):
	Screen.setup(x_setup, y_setup)
	Screen.bgcolor(_color)

LeftGuard = "101"

ZeroL = 	"0001101"
OneL = 		"0011001"
TwoL = 		"0010011"
ThreeL = 	"0111101"
FourL = 	"0100011"
FiveL = 	"0110001"
SixL = 		"0101111"
SevenL = 	"0111011"
EightL = 	"0110111"
NineL = 	"0001011"

CenterGuard = "01010"

ZeroR = 	"1110010"
OneR = 		"1100110"
TwoR = 		"1101100"
ThreeR = 	"1000010"
FourR = 	"1011100"
FiveR = 	"1001110"
SixR = 		"1010000"
SevenR = 	"1000100"
EightR = 	"1001000"
NineR = 	"1110100"

RightGuard = "101"

Code = ""
Left_Code = []
Right_Code = []

def CreateCode():
	global Code

	Country_Code = input("COUNTRY CODE (WITHOUT [-]): ")
	Manufacturer_Code = input("MANUFACTURER CODE: ")
	Product_Code = input("PRODUCT CODE: ")

	Code += LeftGuard

	LeftSideBars(Left_Code, Country_Code + Manufacturer_Code)

	for binary in Left_Code:
		for bit in binary:
			Code += bit

	Code += CenterGuard

	RightSideBars(Right_Code, Product_Code)

	for binary in Right_Code:
		for bit in binary:
			Code += bit

	Code += RightGuard

def LeftSideBars(Binary_CodeL, TheCode):
	for cipher in TheCode:
		if cipher == "0":
			Binary_CodeL.append(ZeroL)
		elif cipher == "1":
			Binary_CodeL.append(OneL)
		elif cipher == "2":
			Binary_CodeL.append(TwoL)
		elif cipher == "3":
			Binary_CodeL.append(ThreeL)
		elif cipher == "4":
			Binary_CodeL.append(FourL)
		elif cipher == "5":
			Binary_CodeL.append(FiveL)
		elif cipher == "6":
			Binary_CodeL.append(SixL)
		elif cipher == "7":
			Binary_CodeL.append(SevenL)
		elif cipher == "8":
			Binary_CodeL.append(EightL)
		elif cipher == "9":
			Binary_CodeL.append(NineL)

def RightSideBars(Binary_CodeR, TheCode):
	for cipher in TheCode:
		if cipher == "0":
			Binary_CodeR.append(ZeroR)
		elif cipher == "1":
			Binary_CodeR.append(OneR)
		elif cipher == "2":
			Binary_CodeR.append(TwoR)
		elif cipher == "3":
			Binary_CodeR.append(ThreeR)
		elif cipher == "4":
			Binary_CodeR.append(FourR)
		elif cipher == "5":
			Binary_CodeR.append(FiveR)
		elif cipher == "6":
			Binary_CodeR.append(SixR)
		elif cipher == "7":
			Binary_CodeR.append(SevenR)
		elif cipher == "8":
			Binary_CodeR.append(EightR)
		elif cipher == "9":
			Binary_CodeR.append(NineR)

List_Of_Lines = []

def CreateLines():
	for i in range(len(Code)):
		try:
			PreviousLine = List_Of_Lines[len(List_Of_Lines) - 1]
		except Exception:
			pass
		line = turtle.Turtle()
		List_Of_Lines.append(line)
		print(List_Of_Lines)
		line.hideturtle()
		line.penup()
		line.shape("square")
		line.shapesize(0.2, 0.2)
		line.color("red")
		try:
			line.goto(PreviousLine.xcor() + 5, 100)
		except Exception:
			line.goto(-250, 100)
		line.showturtle()

def ColorLinesWB():
	x = 0

	for line in List_Of_Lines:
		if(x % 2 == 0):
			line.color("black")
		elif(x % 2 == 1):
			line.color("white")
		x += 1

def ColorLines(Code):
	x = 0
	for number in Code:
		if(number == "1"):
			List_Of_Lines[x].color("black")
		elif(number == "0"):
			List_Of_Lines[x].color("white")
		else:
			pass
		x += 1

def DrawLinesDown():
	for line in List_Of_Lines:
		while line.ycor() >= -100:
			line.stamp()
			line.goto(line.xcor(), line.ycor() - 1)

def main():
	CreateCode()
	CreateWindow(500, 500, "blue")
	CreateLines()
	ColorLines(Code)
	DrawLinesDown()

if __name__ == "__main__":
	main()
	while True:
		Screen.update()