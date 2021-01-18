# Take a look inside file1.txt and file2.txt.
# They each contain a bunch of numbers, each number on a new line.

# You are going to create a list called result which contains the numbers
# that are common in both files.

with open('file1.txt', mode='r') as file_1:
    numbers1 = file_1.readlines()
    stripped_num1 = [n.strip() for n in numbers1]

with open('file2.txt', mode='r') as file_2:
    numbers2 = file_2.readlines()
    stripped_num2 = [n.strip() for n in numbers2]

result = [int(number) for number in stripped_num1 if number in stripped_num2]

# First *fork* your copy.
# Copy Paste your code above this line 👆
# Then click "Run" to execute the tests

print(result)
