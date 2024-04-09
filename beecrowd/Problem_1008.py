number = input()  # this is an int value
hours = input()  # this is an int value
rate_per_hour = input()  # this is a float
hours_int = int(hours)
rate_per_hour_float = float(rate_per_hour)

salary = hours_int * rate_per_hour_float
salary_str = "{:.2f}".format(salary)
print("NUMBER = " + number)
print("SALARY = U$ " + salary_str)
