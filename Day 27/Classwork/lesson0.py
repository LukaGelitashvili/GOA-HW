# https://www.codewars.com/kata/50654ddff44f800200000004/train/python
def multiply(a, b):
    return a * b
# https://www.codewars.com/kata/583710ccaa6717322c000105/train/python
def simple_multiplication(number) :
    if number % 2 == 0:
        return number * 8
    else:
        return number * 9
# https://www.codewars.com/kata/55cbd4ba903825f7970000f5/train/python
def get_grade(s1, s2, s3):
    n = (s1 + s2 + s3) / 3
    if 90 <= n <= 100:
        return "A"
    elif 80 <= n < 90:
        return "B"
    elif 70 <= n < 80:
        return "C"
    elif 60 <= n < 70:
        return "D"
    elif 0<= n < 60:
        return "F" 