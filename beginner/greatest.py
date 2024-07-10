numbersABC = input().strip()
a, b, c = numbersABC.split()

a = int(a)
b = int(b)
c = int(c)

highAB = (a + b + abs(a - b)) / 2
highABC = (highAB + c + abs(highAB - c)) / 2

print(f"{highABC:.0f} eh o maior")