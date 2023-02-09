number = eval(input("Enter your number"))
if number < 0:
    print ("Your number is invalid")
else:
    if number > 50:
        result = number/2
        print(result)
    else:
        print ("Your number is less than 50")
    