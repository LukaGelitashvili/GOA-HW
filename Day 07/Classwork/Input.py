
name = input("სახელი: ")
surname = input("გვარი: ")
age = int(input("ასაკი: "))
country = input("ქვეყანა: ")
city = input("ქალაქი: ")
favorite_car = input("საყვარელი მანქანა: ")
favorite_color = input("საყვარელი ფერი: ")


sentence = f"{name} {surname}, რომელიც არის {age} წლის, ცხოვრობს {country} -ში, {city} -ში, მისი საყვარელი მანქანა არის {favorite_car}, ხოლო საყვარელი ფერი არის {favorite_color}."
print(sentence)


num1 = int(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = int(input("შეიყვანეთ მეორე რიცხვი: "))


print(f"{num1} + {num2} = {num1 + num2}")  
print(f"{num1} - {num2} = {num1 - num2}")  
print(f"{num1} * {num2} = {num1 * num2}")  
print(f"{num1} / {num2} = {num1 / num2}")  
print(f"{num1} // {num2} = {num1 // num2}")  