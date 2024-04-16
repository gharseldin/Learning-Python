n = int(input())
hundreds = n // 100
remainder = n % 100
fifties = remainder // 50
remainder %= 50
twenties = remainder // 20
remainder %= 20
tens = remainder // 10
remainder %= 10
fives = remainder // 5
remainder %= 5
twos = remainder // 2
remainder %= 2
ones = remainder

print(n)
print(str(hundreds) + " nota(s) de R$ 100,00")
print(str(fifties) + " nota(s) de R$ 50,00")
print(str(twenties) + " nota(s) de R$ 20,00")
print(str(tens) + " nota(s) de R$ 10,00")
print(str(fives) + " nota(s) de R$ 5,00")
print(str(twos) + " nota(s) de R$ 2,00")
print(str(ones) + " nota(s) de R$ 1,00")
