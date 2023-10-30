selection = int(input("Enter 1 or 2 : "))

if selection == 1:
    value = int(input("Enter the temperature : "))
    f=(value * 1.8)+32
    print (f)
    
elif selection ==2:
    value = int(input("Enter the temperature : "))
    c=(value - 32)/1.8
    print (c)
    
else:
    print("Invalid operation entered")
