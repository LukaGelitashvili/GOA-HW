# 1️⃣ დავალება — რიცხვების ანალიზი (10 ქულა)

# მომხმარებელმა უნდა შეიყვანოს 5 რიცხვი input() გამოყენებით.

# პროგრამამ უნდა:

# შეინახოს რიცხვები list-ში

# for loop გამოყენებით:

# დაითვალოს რამდენი ლუწი რიცხვია

# დაითვალოს რამდენი კენტი რიცხვია

# ბოლოს დაბეჭდოს:

# Even numbers: X
# Odd numbers: X
# 2️⃣ დავალება — საშუალო ქულის გამოთვლა (10 ქულა)

# შექმენი პროგრამა, რომელიც:

# მომხმარებელს სთხოვს 5 ქულის შეყვანას

# შეინახავს მათ list-ში

# for loop გამოყენებით დაითვლის ჯამს

# გამოითვლის საშუალო ქულას

# შემდეგ if/else გამოყენებით უნდა დაბეჭდოს:

# თუ საშუალო ≥ 90 → "Excellent"

# თუ საშუალო ≥ 70 → "Good"

# თუ საშუალო ≥ 50 → "Pass"

# სხვა შემთხვევაში → "Fail"

# 3️⃣ დავალება — უდიდესი რიცხვის პოვნა (10 ქულა)

# მომხმარებელმა უნდა შეიყვანოს 5 რიცხვი.

# პროგრამამ უნდა:

# შეინახოს ისინი list-ში

# for loop გამოყენებით იპოვოს ყველაზე დიდი რიცხვი

# დაბეჭდოს:

# Largest number is: X

# ⚠️ არ გამოიყენო max() ფუნქცია

# Answers:

# 1) B) იღებს მონაცემს მომხმარებლისგან
# 2) B) Hello
# 3) B) კოდის განმეორება
# 4) C) მონაცემების სია
# 5) B) 2
# 6) 1,2,3 დაიბეჭდება
# 7) Adult
# 8)
# 9) პროგრამა ჯერ მოგთხოვს სახელს და მერე უკვე დაპრინტავს hello, "შენი სახელი"
# 10) B
# 11) 
# name = input("Enter Your Name: ")
# print("hello", name)

#12)
# age = int(input("Enter Your Age: "))
# if age >= 18:
#     print("Adult")
# else:
#     print("Minor")

#13)
# for i in range(10):
#     print(i)

#14)
# numbers = [3,5,7,9]
# for num in numbers:
#     print(num)

#1)
# numbers = []
# even = 0
# odd = 0

# for i in range(5):
#     n = int(input("numbers: "))
#     numbers.append(n)

# for num in numbers:
#     if num % 2 == 0:
#         even += 1
#     else:
#         odd += 1

# print("Even: ", even)
# print("Odd: ", odd)
#2)

#3)
numbers = []

for i in range(5):
    n = int(input("Numbers: "))
    numbers.append(n)

largest_num = numbers[0]

for num in numbers:
    if num >= largest_num:
        largest_num = num

print("The Largest Number is: ", largest_num)