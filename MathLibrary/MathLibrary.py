import math
try:
	def fact(a):
		number_list = []
		y = 1
		for i in range(1,int(a) + 1):
			number_list.append(i)
		for x in number_list:
			y = y * x
		return y
	add = lambda number_1, number_2: number_1 + number_2
	subtract = lambda number_1, number_2: number_1 - number_2
	multiplication = lambda number_1, number_2: number_1 * number_2	
	division = lambda number_1, number_2: number_1 / number_2
	percent = lambda a,b: a / 100 * b
	pi = lambda:math.pi
	def compare(number_1,number_2):
		if number_1 > number_2:
			return 1
		if number_2 > number_1:
			return -1
		if number_1 == number_2:
			return 0
	def absolute(a):
		a = str(a)
		if a.startswith("-") == True:
			result = a.replace("-","")
			return int(result)
		else:
			return int(a)
	power = lambda number_1, number_2: number_1 ** number_2
	square = lambda number: math.pow(number, 1/2)
	def PositiveOrNegative(number:int):
		if number == 0:
			return "Sayı Sıfır."
		if number > 0:
			return "Sayı Pozitif."
		if number < 0:
			return "Sayı Negatif."
except:
	print("Bir hata meydana geldi.")

if __name__ == '__main__':
	pass