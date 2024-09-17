sum_pol = 0
sum_otr = 0

while True:
    num = int(input("Введите число: "))
    if num == 0:
        break
    elif num > 0:
        sum_pol += num
    else:
        sum_otr += num

print("Сумма положительных чисел:", sum_pol)
print("Сумма отрицательных чисел:", sum_otr)