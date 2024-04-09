line = input()
line = line.split(' ')
a = float(line[0])
b = float(line[1])
c = float(line[2])
TRIANGULO = 0.5 * a * c
CIRCULO = 3.14159 * c ** 2
TRAPEZIO = c * (a + b) / 2
QUADRADO = b * b
RETANGULO = a * b

print("TRIANGULO: " + "{:.3f}".format(TRIANGULO))
print("CIRCULO: " + "{:.3f}".format(CIRCULO))
print("TRAPEZIO: " + "{:.3f}".format(TRAPEZIO))
print("QUADRADO: " + "{:.3f}".format(QUADRADO))
print("RETANGULO: " + "{:.3f}".format(RETANGULO))
