s = input("Enter a string: ")

freq = {}   # empty dictionary

for ch in s:
    if ch in freq:
        freq[ch] += 1   # increment existing count
    else:
        freq[ch] = 1    # first occurrence, set to 1

print("Character frequencies:")
for ch, count in freq.items():
    print(ch, ":", count)
