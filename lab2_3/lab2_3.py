with open('input_1.txt', 'r') as file1:
    words1 = set(file1.read().split())

with open('input_2.txt', 'r') as file2:
    words2 = set(file2.read().split())

common_words = words1.intersection(words2)

with open('output.txt', 'w') as output_file:
    for word in common_words:
        output_file.write(word + '\n')
        print(common_words)