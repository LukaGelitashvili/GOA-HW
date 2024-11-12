# პროდუქტის ფასის შეყვანა
price = float(input("შეიყვანეთ პროდუქტის ფასი: "))

# ფასდაკლების განსაზღვრა და საბოლოო ფასის გამოთვლა
if price > 50:
    discount = price * 0.10
    final_price = price - discount
elif price >= 20:
    discount = price * 0.05
    final_price = price - discount
else:
    discount = 0
    final_price = price

# საბოლოო ფასის დაბეჭვდა
print("ფასდაკლება:", discount)
print("საბოლოო ფასი:", final_price)
