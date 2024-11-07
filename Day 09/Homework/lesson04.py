correct_name = "Luka"
correct_password = "1234"

name = input("გთხოვთ, შეიყვანეთ თქვენი სახელი: ")
password = input("გთხოვთ, შეიყვანეთ თქვენი პაროლი: ")

if name == correct_name and password == correct_password:
    print("შესვლა წარმატებით შესრულდა!")
else:
    print("შეცდომა: სახელი ან პაროლი არასწორია.")
