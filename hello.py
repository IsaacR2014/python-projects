sentence = input("Enter a sentence: ")
words = sentence.split()
longest = max(words, key=len)
word_count = len(words)
char_count = len(sentence.replace(" ", ""))
wrick_and_wordy = words[::-1]
letter_count = {}
for char in sentence.lower():
    if char.isalpha():
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1
most_common = max(letter_count, key=letter_count.get)
print(f"Words: {word_count}, Longest: {longest} in reverse: {wrick_and_wordy} most common letter is {most_common}")