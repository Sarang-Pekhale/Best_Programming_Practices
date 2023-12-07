
a = input("Enter 1st number to find GCD: ")
b = input("Enter 2st number to find GCD: ")
if a.isdigit()==True and b.isdigit()==True:
    a = int(a)
    b = int(b)
    if a>b:
        while b != 0:
            c = a % b
            a = b
            b = c
        print(f"The GCD is {a}")
    else:
        while a != 0:
            c = b % a
            b = a
            a = c
        print(f"The GCD is {b}")
        
else:
    print("Please enter integer number only.")


