number = input("Enter form number number: ")
sum = 0

for i in range(0, len(number), 2):
    # take two digits at once
    two_digits = number[i:i+2]
    # add them together and update the sum
    two_digit_sum = (two_digits[0]) + (two_digits[1])
    sum += int(two_digit_sum)

print("Unique Code:", sum)
