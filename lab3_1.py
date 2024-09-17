def reverse_words(message):
    words = message.split()
    reversed_words = words[::-1]
    reversed_message = " ".join(reversed_words)
    return reversed_message

message = input("Введите строку: ")
reversed_message = reverse_words(message)
print(reversed_message)