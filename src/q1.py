def sum_for(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum


def sum_while(numbers):
    sum = 0
    i = 0
    while i < len(numbers):
        sum += numbers[i]
        i += 1
    return sum


def sum_rec(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return numbers[0] + sum_rec(numbers[1:])

numbers = range(1, 11)

print(sum_for(numbers))
print(sum_while(numbers))
print(sum_rec(numbers))
