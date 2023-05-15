def square(num):
    x = num ** 2
    return x
lambda num: num ** 2

def sum_two_numbers(num1, num2):
    return num1+num2

lambda num1, num2: num1+num2


my_list = [9, 99, 999, lambda a:a+a]
print(my_list[3](10))
