user_numbers = []

while True:
    number = input("შეიყვანეთ რიცხვი (Enter დასასრულებლად): ")
    if number == "":
        break
    try:
        user_numbers.append(float(number))
    except ValueError:
        print("გთხოვთ შეიყვანოთ მხოლოდ რიცხვი!")

if any(num > 10 for num in user_numbers):
    print("სიაში არის 10-ზე მეტი რიცხვი")
else:
    print("სიაში 10-ზე მეტი რიცხვი არ არის")

print("შექმნილი სია:", user_numbers)
print("სიის ელემენტების ჯამი:", sum(user_numbers))
