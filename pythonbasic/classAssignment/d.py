sentence = input("Enter a sentence: ")

# split sentence into words
words = sentence.split()

longest = ""   # will store longest word

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)
print("Length      :", len(longest))
