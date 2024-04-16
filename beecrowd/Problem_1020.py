days = int(input())

years = days // 365
remaining_days = days % 365

months = remaining_days // 30
remaining_days %= 30

print(str(years) + " ano(s)")
print(str(months) + " mes(es)")
print(str(remaining_days) + " dia(s)")
