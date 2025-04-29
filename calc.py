# def name_function(f_name, l_name):
#     return f_name.title(), l_name.title()


# print(name_function('bisMArk', 'wIREko'))


# leap year function 

# def leap_year(year):
#     if year % 4 ==0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False



# def days_in_month(year, month):
#     """TAKES A YEAR AND MONTH AS INPUT AND CHECK OUTPUT THE NUMBER OF
#     DAYS IN THAT MONTH OF THE YEAR"""
#     days = [31,28,31,30,31,30,31,31,30,31,30,31]
#     if leap_year(year) == True:
#         days[1] = 29
#         return days[month -1]
#     else:
#         return days[month -1]



# year = int(input("Enter year to check: "))
# month = int(input("Enter month to check: "))
# days = days_in_month(year, month)
# print(days)


#  calculator Application 

def add(n1, n2):
    return n1 + n2


def subtract (n1, n2):
    return n1 - n2


def divide(n1, n2):
    return n1 / n2


def multiply(n1, n2):
    return n1 * n2


# Operations

Operands = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply
}

""" ONE TIME MODE"""
# def one_time():
#     num1 = int(input("Enter first number:"))

#     for i in Operands:
#         print(i)

#     operation_symbol = input("Pick an operation symbol above: ")
#     num2 = int(input("Enter the next number: "))

#     Compute =Operands[operation_symbol]
#     print(f"{num1} {operation_symbol} {num2} = {Compute(num1,num2)}")
#     return Compute(num1,num2)
      

# one_time()

""" RECURSIVE MODE"""

def recursive_calc():
    num1 = float(input("Enter first number:"))

    for i in Operands:
        print(i)

    should_continue = True

    while  should_continue:
        operation_symbol = input("Pick an operation symbol above: ")
        num2 = float(input("Enter the next number: "))
        Compute =Operands[operation_symbol]
        answer1 = Compute(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {Compute(num1,num2)}") 

        if input(f"Type 'y' to continue calculating with {answer1} or 'n' to exit: ")== 'y':
            num1 = answer1
        else:
            should_continue = False
            recursive_calc()


recursive_calc()
