with open('input.txt') as f:
    lines = f.readlines()

numbers = []
output = []
spelled_numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

for line in lines:
    number = ''
    for i, char in enumerate(line):
        if char.isdigit():
            number += char
            break
        for new_number, spelled_number in enumerate(spelled_numbers, start=1):
            if line[i:i+len(spelled_number)] == spelled_number:
                number += str(new_number)
                break
        if len(number) == 1:
            break

    for i, char in enumerate(line[::-1]):
        if char.isdigit():
            number += char
            break
        for new_number, spelled_number in enumerate(spelled_numbers, start=1):
            if line[-i-len(spelled_number):-i] == spelled_number:
                number += str(new_number)
                break
        if len(number) == 2:
            break
    output.append(line.strip() + ' ' + number + '\n')
    numbers.append(int(number))

print(sum(numbers))
with open('output.txt', 'w') as f:
    f.writelines(output)

# 54270 is too low (replacing strings doesn't work e.g. twone)