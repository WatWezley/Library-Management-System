multipier = 1
decimal = 0
number = input("Enter the binary number for conversion: ")

for i in range(len(number)-1, -1, -1):
    digit = int(number[i]) * multipier

    decimal = decimal + digit

    multipier = multipier*2

print(decimal)
