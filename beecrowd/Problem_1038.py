line = input().split(' ')
code = line[0]
amount = int(line[1])
if code == "1":
    print("Total: R$ " + "{:.2f}".format(amount * 4.00))
elif code == "2":
    print("Total: R$ " + "{:.2f}".format(amount * 4.50))
elif code == "3":
    print("Total: R$ " + "{:.2f}".format(amount * 5.00))
elif code == "4":
    print("Total: R$ " + "{:.2f}".format(amount * 2.00))
else:
    print("Total: R$ " + "{:.2f}".format(amount * 1.50))
