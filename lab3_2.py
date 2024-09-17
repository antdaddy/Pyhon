def average(*args):
    return sum(args) / len(args) if len(args) > 0 else 0

print(average(1, 5, 8, 4, 5))
print(average(10, 60, 90))
print(average())