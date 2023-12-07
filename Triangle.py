print("----Triangle----")

import math

a = float(input("Enter 1st side : "))

b = float(input("Enter 2nd side : "))

c = float(input("Enter 3rd side : "))

if a>0 and b>0 and c>0:

    if (a+b)>c and (b+c)>a and (c+a)>b:
        print(f"Triangle with side : [{a},{b},{c}] can be formed.")

        Angle_a = math.acos(((b**2)+(c**2)-(a**2))/(2*b*c))*(180/math.pi)
        Angle_b = math.acos(((a**2)+(c**2)-(b**2))/(2*a*c))*(180/math.pi)
        Angle_c = math.acos(((b**2)+(a**2)-(c**2))/(2*b*a))*(180/math.pi)
        
        if a==b or b==c or c==a:
            print("This is an Isoceles Triangle.")
        elif a==b==c:
            print("This is an Equilateral Triangle.")
        elif Angle_a<90 and Angle_b<90 and Angle_c<90:
            print("This is an Acute Angle Triangle.")
        elif Angle_a==90 or Angle_b==90 or Angle_c==90:
            print("This is a Right Angle Triangle.")
        elif Angle_a>90 or Angle_b>90 or Angle_c>90:
            print("This is a Right Angle Triangle.")
        else:
            print("This is a Scalene Triangle.")

        Semiperi = (a+b+c)/2
        Area = (Semiperi*(Semiperi-a)*(Semiperi-b)*(Semiperi-c))**0.5
        print(f"The area of triangle is : {Area}.")
        print(f'''
                  The angle between side a and b : {Angle_c}
                  The angle between side b and c : {Angle_a}
                  The angle between side c and a : {Angle_b} ''')

    else:
        print("With these sides triangle, cannot be formed.")

else:
    print("Please enter positive integer.")


