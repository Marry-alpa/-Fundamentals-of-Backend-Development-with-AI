# This file demonstrates for, while, range, and continue.

headers = ["Host", "User-Agent", "Accept"]

# Iterate through each header in the list.
for header in headers:
    print("Header:", header)

# Repeat the loop while count is less than 3.
count = 0

while count < 3:
    print("Count:", count)
    count += 1

# Print numbers from 1 to 10, skipping multiples of 3.
for number in range(1, 11):
    if number % 3 == 0:
        continue
    print("Number:", number)