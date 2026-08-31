s=input("enter a string :")
a="aeiouAEIOU"
y=""
for ch in s:
    if ch not in a:
        y=y+ch
print(y)