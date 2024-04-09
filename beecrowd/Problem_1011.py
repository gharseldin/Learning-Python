pi = 3.14159
R = input()
r_float = float(R)
result = (4 / 3) * pi * r_float ** 3
result_str = "{:.3f}".format(result)
print("VOLUME = " + result_str)
