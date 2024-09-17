with open('numbers.txt', 'r') as file:
    numbers = list(map(int, file.readlines()))

max_num = max(numbers)
min_num = min(numbers)

with open('result.txt', 'w') as file:
    file.write(f"Max number: {max_num}\n")
    file.write(f"Min number: {min_num}\n")