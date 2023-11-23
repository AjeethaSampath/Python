
def addition(a, b):
    print("inside add")
    return a + b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b

def calculator(operation, a, b):
    return operation(a, b)

operations = {
    "addition": addition,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide
}

operation1 = input("Please type one operation from (addition,subtract,multiply,divide) :")
number_a = float(input("Type the first number :"))
number_b = float(input("Type the second number :"))

if(operation1 in operations):
    result = calculator(operations[operation1], number_a, number_b)
print(result)
