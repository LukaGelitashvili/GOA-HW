# ასაკის შეყვანა
age = int(input("შეიყვანეთ თქვენი ასაკი: "))

# ასაკის კატეგორიის განსაზღვრა
if age < 13:
    category = "მცირეწლოვანი"
elif age <= 19:
    category = "მოზარდი"
else:
    category = "ზრდასრული"

# შედეგის დაბეჭვდა
print("თქვენ ხართ:", category)
