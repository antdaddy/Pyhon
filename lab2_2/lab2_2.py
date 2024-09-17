with open('input.txt', 'r') as f:
    numbers = list(map(int, f.readline().split()))

result = 1
for num in numbers:
    result *= num
print(result)
with open('output.txt', 'w') as f:
    f.write(str(result))