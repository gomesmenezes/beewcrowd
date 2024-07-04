valueR = float(input("Digite o valor de R para saber a area do circulo: "))

def areaOfCircle(valueR):
    n = 3.14159
    valueCircle = n * (valueR ** 2)
    print(f"A={valueCircle:.4f}")

areaOfCircle(valueR)