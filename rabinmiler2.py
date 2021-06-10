#Author Przemysław Guzek
import random
from math import gcd, log, ceil, sqrt
from random import randint, choice
import sys

class RabinMiller:

    def maxPrimeFactor(n):
        x = ceil(sqrt(n))
        y = pow(x, 2) - n
        while not sqrt(y).is_integer():
            x += 1
            y = pow(x, 2) - n
        return x + sqrt(y), x - sqrt(y)

    def miller_rabin(n, k, uni_exp):
        r, s = 0, uni_exp
        while s % 2 == 0:
            r += 1
            s //= 2
        if n < k:
            k = n;
        a_list = list(range(2,n))
        random.shuffle(a_list)
        for a in a_list:
            x = pow(a, s, n)
            if x == 1 or x == n - 1:
                continue
            for _ in range(r - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                if 1 in RabinMiller.maxPrimeFactor(n):
                    return True
                else:
                    return str(int(choice(RabinMiller.maxPrimeFactor(n))))
        return True



			# r, s = 0, uni_exp
			# while s % 2 == 0:
			# 		r += 1
			# 		s //= 2
			# for _ in range(k):
			# 		a = randrange(2, n - 1)
			# 		x = pow(a, s, n)
			# 		if x == 1 or x == n - 1:
			# 		    continue
			# 		for _ in range(r - 1):
			# 			x = pow(x, 2, n)
            #             if x == n - 1:
			# 				break
            #
			# if 1 in RabinMiller.maxPrimeFactor(n):
			# 	return "Prawdopodobnie pierwsza"
			# return str(int(choice(RabinMiller.maxPrimeFactor(n))))

    @staticmethod
    def fermat(n):
        numbers = []
        for i in range(40):
            a = randint(2, n - 1)
            b = pow(a, n - 1, n)
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
        probability = pow(2, 40)
        result = RabinMiller.miller_rabin(n, probability, uni_exponent)
        if result == True:
            open("wyjscie.txt", "w").write("Prawdopodobnie pierwsza")
        else:
            open("wyjscie.txt", "w").write(result)
