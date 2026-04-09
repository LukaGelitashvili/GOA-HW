# დავალება 1 — Indexing

# მოცემულია სტრინგი:

# word = "Georgia"

# დაბეჭდე:

# პირველი ასო
# ბოლო ასო
# მესამე ასო
# დავალება 2 — Negative indexing

# მოცემულია სია:

# numbers = [10, 20, 30, 40, 50]

# დაბეჭდე:

# ბოლო ელემენტი
# ბოლოს წინა ელემენტი
# შუა ელემენტი
# დავალება 3 — Basic slicing

# მოცემულია სტრინგი:

# text = "Programming"

# დაბეჭდე:

# პირველი 4 ასო
# ბოლო 3 ასო
# შუიდან ნაწილი "gram"
# დავალება 4 — List slicing

# მოცემულია სია:

# colors = ["red", "blue", "green", "yellow", "black", "white"]

# დაბეჭდე:

# პირველი 3 ფერი
# ბოლო 2 ფერი
# შუაში არსებული 2 ფერი
# დავალება 5 — Mixed practice

# მოცემულია სტრინგი:

# name = "Shiolik"

# დაბეჭდე:

# მხოლოდ პირველი 2 ასო
# მხოლოდ ბოლო 2 ასო
# სტრინგი შებრუნებულად slicing-ით


#1
word = "Georgia"
print(word[0])
print(word[-1])
print(word[2])

#2
numbers = [10, 20, 30, 40, 50]
print(numbers[-1])
print(numbers[-2])
print(numbers[2])

#3
text = "Programming"
print(text[:4])
print(text[-3])
print(text[3:7])

#4
colors = ["red", "blue", "green", "yellow", "black", "white"]
print(colors[:3])
print(colors[-2:])
print(colors[2:4])

#5
name = "Shiolik"
print(name[:2])
print(name[-2:])
print(name[-1:-2:-3:-4:-5:-6:-7])