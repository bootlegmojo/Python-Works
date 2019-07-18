temp = (int(input("Please enter the temperature: ")))

isSummer = (input("Is it summer? Type True or False: "))

withinrange = None

if isSummer == "True":
    if 60 <= temp <= 100:
        withinrange = True
    else:
        withinrange = False

else:
    if 60 <= temp <= 90:
        withinrange = True
    else:
        withinrange = False

print("Temperature is within range", withinrange)
