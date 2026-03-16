# Python if-else Assignment Solutions

# Q1 Electricity Bill
units = int(input("Q1 - Enter electricity units: "))

if units <= 100:
    bill = 0
else:
    if units <= 200:
        bill = (units - 100) * 5
    else:
        bill = (100 * 5) + ((units - 200) * 10)

print("Total Bill =", bill)


# Q2 Percentage to Grade
marks = int(input("\nQ2 - Enter percentage: "))

if marks > 90:
    print("Grade A")
else:
    if marks > 80:
        print("Grade B")
    else:
        if marks >= 60:
            print("Grade C")
        else:
            print("Grade D")


# Q3 Youngest of 4 People
a = int(input("\nQ3 - Enter age of person 1: "))
b = int(input("Enter age of person 2: "))
c = int(input("Enter age of person 3: "))
d = int(input("Enter age of person 4: "))

youngest = a

if b < youngest:
    youngest = b
else:
    youngest = youngest

if c < youngest:
    youngest = c
else:
    youngest = youngest

if d < youngest:
    youngest = d
else:
    youngest = youngest

print("Youngest age =", youngest)


# Q4 Employee Bonus
salary = int(input("\nQ4 - Enter salary: "))
years = int(input("Enter years of service: "))

if years > 10:
    bonus = salary * 10 / 100
else:
    if years >= 6:
        bonus = salary * 8 / 100
    else:
        bonus = salary * 5 / 100

print("Bonus Amount =", bonus)


# Q5 Second Largest Number
x = int(input("\nQ5 - Enter number 1: "))
y = int(input("Enter number 2: "))
z = int(input("Enter number 3: "))

if x > y:
    if x < z:
        second = x
    else:
        if y > z:
            second = y
        else:
            second = z
else:
    if y < z:
        second = y
    else:
        if x > z:
            second = x
        else:
            second = z

print("Second Largest Number =", second)


# Q6 Discount Calculation
price = int(input("\nQ6 - Enter marked price: "))

if price > 10000:
    discount = price * 20 / 100
else:
    if price > 7000:
        discount = price * 15 / 100
    else:
        discount = price * 10 / 100

net_amount = price - discount
print("Net Amount to Pay =", net_amount)


# Q7 Stream Allotment
eng = int(input("\nQ7 - English marks: "))
math = int(input("Math marks: "))
sci = int(input("Science marks: "))
sst = int(input("Social Studies marks: "))

if eng > 80 and math > 80 and sci > 80 and sst > 80:
    print("Science Stream")
else:
    if eng > 80 and math > 50 and sci > 50:
        print("Commerce Stream")
    else:
        if eng > 80 and sst > 80:
            print("Humanities")
        else:
            print("No Stream Allotted")


# Q8 Multiple of Five
num = int(input("\nQ8 - Enter number: "))

if num % 5 == 0:
    print("Hello")
else:
    print("Bye")


# Q9 Last Digit Divisible by 3
num2 = int(input("\nQ9 - Enter number: "))
last_digit = num2 % 10

if last_digit % 3 == 0:
    print("Last digit divisible by 3")
else:
    print("Last digit not divisible by 3")


# Q10 Three Digit Number Check
num3 = int(input("\nQ10 - Enter number: "))

if num3 >= 100:
    if num3 <= 999:
        print("It is a three digit number")
    else:
        print("Not a three digit number")
else:
    print("Not a three digit number")
