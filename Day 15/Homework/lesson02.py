year = int(input("შეიყვანეთ წელი: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} წელი ნაკიანია (თებერვალში 29 დღეა).")
else:
    print(f"{year} წელი არ არის ნაკიანი.")
