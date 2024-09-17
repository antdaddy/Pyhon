n = int(input("Введите количество чисел: "))
numbers = []
for i in range(n):
    num = int(input("Введите число: "))
    numbers.append(num)

unique_numbers = list(set(numbers))
print("Уникальные числа:", unique_numbers)