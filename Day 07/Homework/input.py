
name = input("შეიყვანეთ თქვენი სახელი: ")
surname = input("შეიყვანეთ თქვენი გვარი: ")
age = input("შეიყვანეთ თქვენი ასაკი: ")
country = input("შეიყვანეთ თქვენი ქვეყანა: ")
city = input("შეიყვანეთ თქვენი ქალაქი: ")
favorite_car = input("შეიყვანეთ თქვენი საყვარელი მანქანა: ")
favorite_color = input("შეიყვანეთ თქვენი საყვარელი ფერი: ")


sentence = f"{name} {surname} არის {age} წლის, ცხოვრობს {country}-ში, {city}-ში. მისი საყვარელი მანქანა არის {favorite_car}, ხოლო საყვარელი ფერი - {favorite_color}."
print(sentence)


num1 = int(input("შეიყვანეთ პირველი რიცხვი: "))  
num2 = int(input("შეიყვანეთ მეორე რიცხვი: "))  

print(f"Addition (+): {num1} + {num2} = {num1 + num2}") 
print(f"Subtraction (-): {num1} - {num2} = {num1 - num2}") 
print(f"Multiplication (*): {num1} * {num2} = {num1 * num2}")  
print(f"Division (//): {num1} // {num2} = {num1 // num2}")  
print(f"Addition example 2: {num1 + 2} + {num2 + 2} = {num1 + num2 + 4}")
print(f"Subtraction example 2: {num1 - 3} - {num2 - 3} = {num1 - 3 - num2 + 3}")
print(f"Multiplication example 2: {num1 * 2} * {num2 * 2} = {(num1 * 2) * (num2 * 2)}")
print(f"Division example 2: {num1 + 8} // {num2 + 1} = {(num1 + 8) // (num2 + 1)}")
print(f"Addition example 3: {num1 + 5} + {num2 + 5} = {num1 + 5 + num2 + 5}")
print(f"Subtraction example 3: {num1 - 10} - {num2 - 2} = {num1 - 10 - num2 + 2}")
