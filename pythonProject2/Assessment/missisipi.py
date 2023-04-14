word = "MISSISSIPPI"
count = 0
for i in range(0, len(word), 1):
    if word[i] == "S":
        count = count + 1

print(count)
