#Author Przemysław Guzek
from math import gcd, log, ceil, sqrt
from random import randint,randrange, choice
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
        # k = n - 1
        # r = k
        # guwno = True
        # iterations = 0
        #
        # while guwno:
        #     r = r/2
        #     print(r)
        #     iterations += 1
        #     print(iterations)
        #     if r % 2 != 0:
        #         guwno = False
        # q = k / pow(2, iterations)
        # print(q)

        r, s = 0, n - 1
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
            else:
                return False
        return True

    # def is_prime(p, r=10):
    #     for i in range(r):
    #         if not milrab(p):
    #             return False
    #     return True





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
        probability = pow(2, 40)
        a = randint(2, n - 1)
        # range_ = int(log(-probability+1, (1/4)))
        # open("wyjscie.txt", "w").write(RabinMiller.miller_rabin(n, range_, uni_exponent))
        t = 0
        f = 0
            # if RabinMiller.miller_rabin(n, probability, uni_exponent) == False:
        if (RabinMiller.miller_rabin(n, probability, uni_exponent)) == True:
                t += 1
        else:
                f += 1
        print(t, f)