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
	def add(a,b):
		result = a + b
		return result
	def subtract(a,b):
		result = a - b
		return result
	def multiplication(a,b):
		result = a * b
		return result
	def division(a,b):
		result = a / b
		return result
	def percent(a,b):
		result = a / 100 * b
		return result
	def pi():
		result = math.pi
		return result
	def compare(a,b):
		if a > b:
			return 1
		if b > a:
			return -1
		if a == b:
			return 0
	def absolute(a):
		a = str(a)
		if a.startswith("-") == True:
			result = a.replace("-","")
			return int(result)
		else:
			return int(a)
	def power(a,b):
		result = a ** b
		return result
	def square(a):
		result = math.pow(a,1/2)
		return result
	def PositiveOrNegative(a):
		if int(a) == 0:
			return "Sayı Sıfır."
		if int(a) > 0:
			return "Sayı Pozitif."
		if int(a) < 0:
			return "Sayı Negatif."
except:
	print("Hata")

if __name__ == '__main__':
	pass