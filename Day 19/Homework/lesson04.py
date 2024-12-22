my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

number_to_check = int(input("შეიყვანეთ რიცხვი, რომლის მოძებნაც გსურთ სიაში: "))

if number_to_check in my_list:
    print(f"რიცხვი {number_to_check} მოიძებნა სიაში.")
else:
    print(f"რიცხვი {number_to_check} არ მოიძებნა სიაში.")
