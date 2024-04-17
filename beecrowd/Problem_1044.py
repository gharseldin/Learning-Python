line = input().split(' ')
a = int(line[0])
b = int(line[1])

if (a > b and a%b == 0) or (a < b and b%a == 0):
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")