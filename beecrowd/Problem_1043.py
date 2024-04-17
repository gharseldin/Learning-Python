line = input().split(' ')
a = float(line[0])
b = float(line[1])
c = float(line[2])

if a >= b + c or b >=a + c or c >= a + b:
    area_of_trapezium = c * (a + b) / 2
    print("Area = " + "{:.1f}".format(area_of_trapezium))
else:
    triangle_perimeter = a + b + c
    print("Perimetro = " + "{:.1f}".format(triangle_perimeter))
