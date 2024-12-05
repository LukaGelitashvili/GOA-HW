import random


correct_number = random.randint(1, 10)

print("გამოცადე შენი იღბალი! გამოიცანით რიცხვი 1-დან 10-მდე.")


while True:
    try:
        user_guess = int(input("შეიყვანეთ თქვენი რიცხვი: "))
        
        if user_guess < 1 or user_guess > 10:
            print("გთხოვთ, შეიყვანეთ რიცხვი 1-დან 10-მდე!")
        elif user_guess < correct_number:
            print("შეცდომაა! რიცხვი მეტია.")
        elif user_guess > correct_number:
            print("შეცდომაა! რიცხვი ნაკლებია.")
        else:
            print(f"გილოცავთ! სწორად გამოიცანით, ეს რიცხვი იყო {correct_number}.")
            break
    except ValueError:
        print("გთხოვთ, შეიყვანეთ რიცხვი!")

