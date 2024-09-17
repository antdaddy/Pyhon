def even_numbers(lst):
    even_lst = []
    for num in lst:
        if num % 2 == 0:
            even_lst.append(num)
    return tuple(even_lst)

# Пример использования
print(even_numbers([1, 2, 3, 4, 5, 6])) # Вывод: (2, 4, 6)