#19. Count vowels in a string
s = "programming"
count = 0

for ch in s:
    if ch in "aeiou":
        count += 1

print(count)