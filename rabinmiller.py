#Author Przemysław Guzek
from math import gcd, log, ceil, sqrt
from random import randrange, choice
import sys

class RabinMiller:

	def maxPrimeFactor(n):
		x = ceil(sqrt(n))
		y = x**2 - n
		while not sqrt(y).is_integer():
			x += 1
			y = x**2 - n
		return x + sqrt(y), x - sqrt(y)

	def miller_rabin(n, k, uni_exp):

			r, s = 0, uni_exp
			while s % 2 == 0:
					r += 1
					s //= 2
			for _ in range(k):
					a = randrange(2, n - 1)
					x = pow(a, s, n)
					if x == 1 or x == n - 1:
							continue
					for _ in range(r - 1):
							x = pow(x, 2, n)
							if x == n - 1:
									break

			if 1 in RabinMiller.maxPrimeFactor(n):
				return "Prawdopodobnie pierwsza"
			return str(int(choice(RabinMiller.maxPrimeFactor(n))))

	@staticmethod
	def fermat(n):
		numbers = []
		for i in range(40):
			a = randrange(2, n-2)
			b = pow(a, n-1, n)
			if b == 1:
				print(b)
			numbers.append(b)

		if 1 in numbers:
			open("wyjscie.txt", "w").write("Prawdopodobnie pierwsza")
		else:
			open("wyjscie.txt", "w").write("Na pewno złożona")

		print(numbers)




if __name__ == '__main__':
	with open("wejscie.txt", "r") as file:
		lines = [int(x.rstrip()) for x in file.readlines()]
		try:
			n, m, l = lines
			uni_exponent = m * l
		except ValueError:
			try:
				n, uni_exponent = lines
				uni_exponent -= 1
			except ValueError:
				n = lines
	opt = sys.argv[1:]
	if '-f' in opt:
		RabinMiller.fermat(n)

	else:
		probability = 1 - pow(2, -40)
		a = randrange(2, n)
		range_ = int(log(-probability+1, (1/4)))
		open("wyjscie.txt", "w").write(RabinMiller.miller_rabin(n, range_,uni_exponent))

