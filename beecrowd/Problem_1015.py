line1 = input().split(' ')
line2 = input().split(' ')

x1 = float(line1[0])
y1 = float(line1[1])

x2 = float(line2[0])
y2 = float(line2[1])

result = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

print("{:.4f}".format(result))
