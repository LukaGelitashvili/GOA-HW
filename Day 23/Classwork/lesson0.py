def calculate_operations(x, y):
    print(f"ჯამი (x + y): {x + y}")
    print(f"გამოკლება (x - y): {x - y}")
    print(f"გამრავლება (x * y): {x * y}")
    if y != 0:
        print(f"განაყოფი მთელი გაყოფით (x // y): {x // y}")
    else:
        print("განაყოფი მთელი გაყოფით (x // y): y არ შეიძლება იყოს 0")
        
calculate_operations(10, 5)
