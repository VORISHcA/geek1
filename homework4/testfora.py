from sys import argv

script_name, hour, rate, prize = argv
salary = int(hour) * int(rate) + int(prize)
print("Ваша Зп + премия ", salary)

# python testfora.py 1000 5 2000
