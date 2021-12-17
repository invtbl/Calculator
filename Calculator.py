def calculator():
    num_1 = int(input("Enter first number: "))
    operator_1 = input("Enter operator: ")
    num_2 = int(input("Enter first number: "))

    if operator_1 == "+":
        print(num_1 + num_2)
    elif operator_1 == "-":
        print(num_1 - num_2)
    elif operator_1 == "/":
        print(num_1 / num_2)
    elif operator_1 == "*":
        print(num_1 * num_2)


calculator()
