# Taking a rational number input from user.

Num = float(input("Enter any rational number : "))

# Converting the rational number into string.

num = str(Num)

# Identifying the index of decimal.

for i in range(len(num)):
    if num[i]=='.':
        index = i

# Saving float number as string from decimal onwards.

num_deci = num[index:]

# Saving float number after decimal as integer.

int_deci = num[index+1:]

# Saving float number as float from decimal onwards.

Num_deci = float(num_deci)

denominator = 10**len(int_deci)
numerator = int(num[index+1:])
a = denominator
b = numerator
while b != 0:
    c = a % b
    a = b
    b = c
GCD = a
# Printing the result in compact rational form.

print(f"{round(Num-Num_deci)} + {numerator/GCD}/{denominator/GCD}")

