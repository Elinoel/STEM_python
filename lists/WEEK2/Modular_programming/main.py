# import functions
# x = functions.add(12,34)
# print(x)
# y= functions.subtract(20,5)
# print(y)
# from operators import add
# from operators import subtract
import operators
import others
import trigonometry
# x = others.cube(3)
# print(x)

# y = operators.divide(9,3)
# print(y)

#get numbers
operator = input("Enter operator: ")

if operator == "cube":
    num = eval(input("Enter number: "))
    x = others.cube(num)
    print(x)
elif operator == "sin":
    angle = eval(input("Enter angle in degrees: "))
    sin_of_angle = trigonometry.get_sin(angle)
    print(sin_of_angle)
elif operator == "tan":
    angle = eval(input("Enter angle in degrees: "))
    print(trigonometry.get_tan(angle))
elif operator == "cos":
    angle = eval(input("Enter angle in degrees: "))
    print(trigonometry.get_cos(angle))
else:
    num1 = eval(input("Enter number 1: "))
    num2 = eval(input("Enter number 2: "))


    if operator == "+":
        x = operators.add(num1 , num2)
        print(x)

    elif operator == "-":
        x = operators.substract(num1,num2)
        print(x)

    elif operator == "*" or "x" or "X":
        x = operators.multiply(num1,num2)
        print(x)

    elif operator == "/":
        x = operators.divide(num1,num2)
        print(x)
    

