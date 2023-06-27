num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

print("Arithmetic Operations:+,-,*,/,**,//")
opr = input("Select operations to be performed: ")

if opr == "+":
    print(num1, "+", num2, "=", num1+num2)

elif opr == "-":
    print(num1, "-", num2, "=", num1-num2)


elif opr == "*":
    print(num1, "*", num2, "=", num1*num2)


elif opr == "/":
    print(num1, "/", num2, "=", num1/num2)

elif opr == "//":
    print(num1, "//", num2, "=", num1//num2)

elif opr == "**":
    print(num1, "**", num2, "=", num1**num2)

else:
    print("Invalid input")