score = int(input("შეიყვანეთ თქვენი ქულა (1-დან 100-მდე): "))

if 1 <= score <= 100:

    if 90 <= score <= 100:
        print("Your grade is A")
    elif 80 <= score < 90:
        print("Your grade is B")
    elif 70 <= score < 80:
        print("Your grade is C")
    else:
        print("Your grade is D")
else:

    print("გთხოვთ, შეიყვანეთ ქულა 1-დან 100-მდე.")
