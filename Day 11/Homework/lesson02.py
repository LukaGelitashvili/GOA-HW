# რიცხვის შეყვანა
number = float(input("შეიყვანეთ რიცხვი: "))

# რიცხვის სტატუსის განსაზღვრა
if number == 0:
    result = "ნულია"
elif number > 0:
    result = "დადებითი რიცხვია"
else:
    result = "უარყოფითი რიცხვია"

# შედეგის დაბეჭვდა
print("შედეგი:", result)
