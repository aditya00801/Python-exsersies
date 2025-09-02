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
    if num_2 == 0:
        print("Error! : devide by 0")
    else:
        result = num_1 / num_2
        print("result :", num_1, "/", num_2, "=", result)
else :
    print("Error :Invalid operation!")
