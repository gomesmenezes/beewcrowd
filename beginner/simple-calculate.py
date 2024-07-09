# In this problem, the task is to read a code of a product 1, the number of units of product 1, the price for one 
# unit of product 1, the code of a product 2, the number of units of product 2 and the price for one unit of product 
# 2. After this, calculate and show the amount to be paid.

# Input
# The input file contains two lines of data. In each line there will be 3 values: two integers and a floating 
# value with 2 digits after the decimal point.

# Output
# The output file must be a message like the following example where "Valor a pagar" means Value to Pay.
# Remember the space after ":" and after "R$" symbol. The value must be presented with 2 digits after the point.

product1 = input().strip()
product2 = input().strip()

code1, units1, price1 = product1.split()
code2, units2, price2 = product2.split()

code1 = int(code1)
units1 = int(units1)
price1 = float(price1)

code2 = int(code2)
units2 = int(units2)
price2 = float(price2)


value = (units1 * price1) + (units2 * price2)
print(f"VALOR A PAGAR: R$ {value:.2f}")