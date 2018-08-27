firstnum = input()
operator = input()
secondnum = input()

def calculator(firstnum, operator, secondnum):
	if operator == "+":
		print(int(firstnum) + int(secondnum))
	if operator == "-":
		print(int(firstnum) - int(secondnum))
	if operator == "x" or operator == "*":
		print(int(firstnum) * int(secondnum))
	if operator == "/":
		print(int(firstnum) / int(secondnum))			

calculator(firstnum, operator, secondnum)		