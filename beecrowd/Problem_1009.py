name = input()
salary = input()
sales = input()

sales_float = float(sales)
sales_bonus = sales_float * 0.15

total_salary = float(salary) + sales_bonus
total_str = "{:.2f}".format(total_salary)

print("TOTAL = R$ " + total_str)
