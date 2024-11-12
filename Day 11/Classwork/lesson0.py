def check_drivers_license_eligibility():
    try:
        age = int(input("შეიყვანეთ თქვენი ასაკი: "))
        experience = int(input("შეიყვანეთ მანქანის მართვის გამოცდილება (წლები): "))

        if age < 0 or experience < 0:
            print("გთხოვთ შეიყვანოთ დადებითი მთელი რიცხვები ასაკისა და გამოცდილებისთვის.")
            return

        if age < 18:
            print("თქვენ არ შეგიძლიათ მართვის მოწმობის აღება, რადგან თქვენი ასაკი 18 წელზე ნაკლებია.")
        elif age >= 18 and experience >= 1:
            print("თქვენ გაქვთ მართვის მოწმობის აღების უფლება.")
        else:
            print("მართვის მოწმობის მისაღებად უნდა გქონდეთ მინიმუმ 1 წლიანი გამოცდილება.")
    
    except ValueError:
        print("გთხოვთ შეიყვანოთ სწორი მთელი რიცხვები.")

check_drivers_license_eligibility()
