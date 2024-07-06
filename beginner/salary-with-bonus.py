sellerName = input()
salary = float(input())
productsSold = float(input())

salary += (0.15 * productsSold)

print(f'TOTAL = R$ {salary:.2f}')