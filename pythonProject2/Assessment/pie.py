pie = 4
count = 0
terms = 1

for i in range(3, 200000, 2):
    result = 4 / i

    if count == 0:
        raw_pie = pie - result
        pie = round(raw_pie, 6)

    if count == 1:
        raw_pie = pie + result
        pie = round(raw_pie, 6)

    if count == 0:
        count = count + 1
    elif count == 1:
        count = 0
    if pie == 3.141590:
        terms = i
        break
    print(pie)
print(terms)
