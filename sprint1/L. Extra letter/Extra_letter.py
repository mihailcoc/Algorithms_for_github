s = str(input())
t = str(input())

for character in s:
    t = t.replace(character, '', 1)

print(t)