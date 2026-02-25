#1
name = input("Enter Your Name: ")
color = input("Enter Your Favorite Color: ")

print(name + " favorite color is..." + color)

#2
number = int(input("enter a number: "))

if number > 0:
    print("The Number Is True")
elif number < 0:
    print("The Number Is False")
else:
    print(0)

#3

#4
password = ""
while password != "admin":
    password = input("enter a password")
print("the password is correct, welcome User.")

#5
words = []

word_1 = input("Enter The First Word: ")
word_2 = input("Enter The Second Word: ")
word_3 =  input("Enter The Third Word: ")
word_4 = input("Enter The Fourth Word: ")
word_5 = input("Enter The Fifth Word: ")

words.append(word_1)
words.append(word_2)
words.append(word_3)
words.append(word_4)
words.append(word_5)

print(words)
print(words[0],words[4])