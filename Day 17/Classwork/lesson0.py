data_list = [42, "Hello", 3.14, True, None, {"key": "value"}, [1, 2, 3], (4, 5), {9, 8}, bytes("ABC", "utf-8")]

print(data_list[0])
print(data_list[1])
print(data_list[2])

data_list[3] = "Python"
data_list[4] = "JavaScript"
data_list[5] = "C++"

data_list.extend(["Java", "Ruby", "Go", "Kotlin", "Swift"])

print(data_list)
