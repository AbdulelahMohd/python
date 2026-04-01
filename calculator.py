num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))
operation = input("Enter operation + - / * : ")

if operation == "+":
    result = num1 + num2
    print("The result is ",result)
elif operation == "-":
    result = num1 - num2
    print("The result is ",result)
elif operation == "*":
    result = num1 * num2
    print("The result is ",result)
elif operation == "/":
    if num2!=0:
        result = num1 / num2
        print("The result is ",result)
    else :
        print ("The inputs is not right")
else :
    print ("The operation is invalid")