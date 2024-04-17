line = input().split(' ')
a = int(line[0])
b = int(line[1])
c = int(line[2])

if a < b < c:
    print(str(a) + "\n" + str(b) + "\n" + str(c))

elif a < c < b:
    print(str(a) + "\n" + str(c) + "\n" + str(b))
elif b < a < c:
    print(str(b) + "\n" + str(a) + "\n" + str(c))
elif b < c < a:
    print(str(b) + "\n" + str(c) + "\n" + str(a))
elif c < a < b:
    print(str(c) + "\n" + str(a) + "\n" + str(b))
else:
    print(str(c) + "\n" + str(b) + "\n" + str(a))
print()
print(str(a) + "\n" + str(b) + "\n" + str(c))
