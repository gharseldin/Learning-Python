input_line = input().split()
a = float(input_line[0])
b = float(input_line[1])
c = float(input_line[2])

root = b ** 2 - 4 * a * c

if a == 0 or root < 0:
    print("Impossivel calcular")
else:
    denominator = 2 * a
    square_root = root ** 0.5
    r1 = (-1 * b - square_root)/denominator
    r2 = (-1 * b + square_root)/denominator
    print("R1 = " + "{:.5f}".format(r2))
    print("R2 = " + "{:.5f}".format(r1))
