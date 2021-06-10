#Author Przemysław Guzek
import random
from math import gcd, log, ceil, sqrt
from random import randint, choice
import sys

class RabinMiller:

    def miller_rabin(n, k, uni_exp):
        r, s = 0, uni_exp
        while s % 2 == 0:
            r += 1
            s //= 2
        if n < k:
            k = n
        for _ in range(2, k):
            a = randint(2, n)
            x = pow(a, s, n)
            print(x)
            if x == 1 or x == n - 1:
                continue
            for _ in range(r - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return RabinMiller.prime_factors(n)
        return True

    def prime_factors(n):
        x = ceil(sqrt(n))
        y = pow(x, 2) - n
        while not sqrt(y).is_integer():
            x += 1
            y = pow(x, 2) - n
        return x + sqrt(y), x - sqrt(y)

    @staticmethod
    def fermat(n):
        numbers = []
        for _ in range(40):
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
            if 1 in result:
                open("wyjscie.txt", "w").write("Prawdopodobnie pierwsza")
            else:
                open("wyjscie.txt", "w").write(str(int(choice(result))))
