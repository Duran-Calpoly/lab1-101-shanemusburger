def calculate_average(num1, num2, num3):
    total = num1 + num2 + num3 
    average= total/3
    return average


print(calculate_average (3,5,7))


def add_tax(bill_total):
    add_tax=bill_total*1.1
    return add_tax

print(add_tax(22))


def greet_user(name):
    greet_user="Hello " + name
    return(greet_user)

print(greet_user("bob")) 