num_1 = int(input("Enter the first number:"))
op = input("Enter the operator:")
num_2 = int(input("Enter the second number:"))
if op == "+":
    result = num_1 + num_2
    print("result :",num_1 ,"+",num_2,"=", result)
elif op == "-":
    result = num_1 - num_2
    print("result :", num_1, "-", num_2, "=", result)
elif op == "*":
    result = num_1 * num_2
    print("result :", num_1, "*", num_2, "=", result)
elif op == "/":
    try:
        result = num_1 / num_2
        print("result :", num_1, "/", num_2, "=", result)
    except ZeroDivisionError:
        print("Error: You cannot divide by zero") 
else :
    print("Error :Invalid operation!")


