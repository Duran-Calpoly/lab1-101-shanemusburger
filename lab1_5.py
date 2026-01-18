def check_multiple(number):
    return number % 5 == 0 and number % 3 == 0
print(check_multiple(2))

def check_password(input_string):
    if input_string == "Python123":
        return("access granted")
    else:
        return("access denied")

check_password("Python123")

def calculate_federal_tax(salary):
    if salary < 11000:
        return salary*0.10
    elif (salary >= 11000) and (salary < 44725):
        return salary*0.12
    elif (salary >= 44725) and (salary < 95375):
        return salary*0.22
    else:
        return salary*0.24
    
print(calculate_federal_tax(50000))
# test