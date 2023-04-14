count = 0
largest_so_far = float("-inf")
second_largest_so_far = float("-inf")
no_of_number = int(input("How many times do you want to enter a number: "))
while count < no_of_number:
    num = int(input("Give me a number: "))
    if num > largest_so_far:
        second_largest_so_far = largest_so_far
        largest_so_far = num

    count += 1
print("The second largest number is", second_largest_so_far)
