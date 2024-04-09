product1 = input()
product2 = input()

product1_split = product1.split(' ')
product2_split = product2.split(' ')

product1_code = product1_split[0]
product1_count = product1_split[1]
product1_price = product1_split[2]
product2_code = product2_split[0]
product2_count = product2_split[1]
product2_price = product2_split[2]

p1_count_int = int(product1_count)
p1_price_float = float(product1_price)

p2_count_int = int(product2_count)
p2_price_float = float(product2_price)

total = p1_count_int * p1_price_float + p2_count_int * p2_price_float
total_str = "{:.2f}".format(total)

print("VALOR A PAGAR: R$ " + total_str)
