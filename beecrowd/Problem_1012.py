string = "Amr, 2014147043, Las Veags, NV, 89144"
splitString = string.split(',')
splitString_length = len(splitString)
for i in range(splitString_length):
    print(splitString[i].strip())
