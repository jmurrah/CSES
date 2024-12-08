letters = input()
l =longest = 0

for r in range(len(letters)):
    while letters[r] != letters[l]:
        l += 1
    longest = max(longest, r - l + 1)

print(longest)