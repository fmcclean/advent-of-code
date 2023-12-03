with open('input.txt') as f:
    lines = f.readlines()

numbers = []

for line in lines:
    number = ''
    for char in line:
        if char.isdigit():
            number += char
            break
    for char in line[::-1]:
        if char.isdigit():
            number += char
            break
    numbers.append(int(number))

print(sum(numbers))