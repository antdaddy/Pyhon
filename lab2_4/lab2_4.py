with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read()

freq = {} #slovar

for letter in text:
     if letter.isalpha(): # letter?
        if letter in freq:
            freq[letter] += 1
        else:
            freq[letter] = 1

sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True) #sort_freq_dec

with open('output.txt', 'w', encoding='utf-8') as f:
    for letter, count in sorted_freq:
        f.write(f'{letter}: {count}\n')