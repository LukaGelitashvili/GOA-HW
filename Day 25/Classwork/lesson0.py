text = input("შეიყვანეთ ტექსტი: ")

lower_case = text.lower()
print("პატარა ასოებით:", lower_case)

upper_case = text.upper()
print("დიდი ასოებით:", upper_case)

capitalize_case = text.capitalize()
print("მხოლოდ პირველი დიდი ასო:", capitalize_case)

word = input("შეიყვანეთ სიტყვა, რომელიც უნდა მოძებნოთ: ")
index = text.find(word)

if index != -1:
    print(f"სიტყვა '{word}' მოიძებნა ინდექსზე {index}")
else:
    print(f"სიტყვა '{word}' არ მოიძებნა ტექსტში.")
