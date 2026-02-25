# # Class Work

# 1) შექმენით კალკულატორი ინფუთებით.

# 2) ააწყე სარეგისტრაციო ფორმას მსგავსი ინფუთების დახმარებით.

#1
# a = int(input("Enter The First Number: "))
# b = int(input("Enter The Second Number: "))
# symbol = input("Enter The Operation: ")

# if symbol == "+":
#     print(a + b)
# elif symbol == "-":
#     print(a - b)
# elif symbol == "*":
#     print(a * b)
# elif symbol == "/":
#     print(a / b)
# else:
#     print("Invalid Operation")


# #2

# Email = input("Enter Your Email: ")
# Password = input("Enter The Password: ")

# if Email != "abcdefg@gmail.com":
#     print("Invalid Email")
# elif Password != "beako":
#     print("Invalid Password")
# else:
#     print("Welcome, Luka")

age = int(input("Enter Your Age: "))

if age >= 18:
    print("You're an adult")
elif age >= 80:
    print("you're a grandma/grandpa")
elif age <= 18:
    print("You're a teenager")
else:
    print("unknown age category")