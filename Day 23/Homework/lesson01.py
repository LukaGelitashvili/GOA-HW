def simple_calculator(num1, num2, operation):
    if operation == "მიმატება":
        return num1 + num2
    elif operation == "გამოკლება":
        return num1 - num2
    elif operation == "გამრავლება":
        return num1 * num2
    elif operation == "გაყოფა":
        if num2 == 0:
            return "შეცდომა: ნულზე გაყოფა შეუძლებელია"
        else:
            return num1 / num2
    else:
        return "შეცდომა: უცნობი ოპერაცია"

result1 = simple_calculator(10, 5, "მიმატება")
result2 = simple_calculator(15, 3, "გამოკლება")
result3 = simple_calculator(7, 6, "გამრავლება")
result4 = simple_calculator(20, 0, "გაყოფა")
result5 = simple_calculator(20, 4, "გაყოფა")

print("მიმატება:", result1)
print("გამოკლება:", result2)
print("გამრავლება:", result3)
print("ნულზე გაყოფა:", result4)
print("გაყოფა:", result5)
