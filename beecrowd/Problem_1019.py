seconds = int(input())
hours = seconds // 3600
remainder = seconds % 3600
minutes = remainder // 60
remainder = seconds % 60

print(str(hours) + ":" + str(minutes) + ":" + str(remainder))
