import math
try:
	class MathLibrary():
		def __init__(self,a,b,c):
			self.a = a 
			self.b = b
		def fact(a):
			number_list = []
			y = 1
			for i in range(1,int(a) + 1):
				number_list.append(i)
			for x in number_list:
				y = y * x
			print(y)
		def add(a,b):
			result = a + b
			print(result)
		def subtract(a,b):
			result = a - b
			print(result)
		def multiplication(a,b):
			result = a * b 
			print(result)
		def division(a,b):
			result = a / b
			print(result)
		def percent(a,b):
			result = a / 100 * b
			print(result)
		def pi():
			result = math.pi
			print(result)
		def compare(a,b):
			if a > b:
				print(1)
			if b > a:
				print(-1)
			if a == b:
				print(0)
		def absolute(a):
			a = str(a)
			if a.startswith("-") == True:
				result = a.replace("-","")
				print(int(result))
			else:
				print(int(a))
		def power(a,b):
			result = a ** b
			print(result)
		def square(a):
			result = math.pow(a,1/2)
			print(result)
		def PositiveOrNegative(a):
			if int(a) == 0:
				print("Sayı Sıfır.")
			if int(a) > 0:
				print("Sayı Pozitif.")
			if int(a) < 0:
				print("Sayı Negatif.")
except:
	print("Hata")

if __name__ == '__main__':
	pass