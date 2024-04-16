n = float(input())

hundreds = int(n // 100)
n %= 100
fifties = int(n // 50)
n %= 50
twenties = int(n // 20)
n %= 20
tens = int(n // 10)
n %= 10
fives = int(n // 5)
n %= 5
twos = int(n // 2)
n %= 2
ones = int(n // 1)
n %= 1

n_cents = n * 100
fifty_cents = int(n_cents // 50)
n_cents %= 50
twenty_five_cents = int(n_cents // 25)
n_cents %= 25
ten_cents = int(n_cents // 10)
n_cents %= 10
five_cents = int(n_cents // 5)
n_cents %= 5
one_cent = int(n_cents)

print("NOTAS:")
print(str(hundreds) + " nota(s) de R$ 100.00")
print(str(fifties) + " nota(s) de R$ 50.00")
print(str(twenties) + " nota(s) de R$ 20.00")
print(str(tens) + " nota(s) de R$ 10.00")
print(str(fives) + " nota(s) de R$ 5.00")
print(str(twos) + " nota(s) de R$ 2.00")
print("MOEDAS:")
print(str(ones) + " moeda(s) de R$ 1.00")
print(str(fifty_cents) + " moeda(s) de R$ 0.50")
print(str(twenty_five_cents) + " moeda(s) de R$ 0.25")
print(str(ten_cents) + " moeda(s) de R$ 0.10")
print(str(five_cents) + " moeda(s) de R$ 0.05")
print(str(one_cent) + " moeda(s) de R$ 0.01")
