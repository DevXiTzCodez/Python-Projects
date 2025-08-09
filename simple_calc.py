operator = input("Enter an operator: (+,-,*,/,%) ")
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if operator == "+":
    results = num1 + num2
    print(f"The addition of two numbers is {results}")
elif operator == "-":
    results = num1 - num2
    print(f"The subtraction of two numbers is {results}")
elif operator == "*":
    results = num1 * num2
    print(f"The multiple of two numbers is {results}")
elif operator == "/":
    results = num1 / num2
    print(f"The division of two numbers is {results}")
elif operator == "%":
    results = num1 % num2
    print(f"The modulus of two numbers is {results}")
else:
    print(f"'{operator}' is an invalid operator")            