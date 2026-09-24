numbers = [12,7,25,3,19]
def max_number(numbers):
    if len(numbers)== 1:
        return numbers[0]
    x = max_number(numbers[1:])
    if numbers[0] > x:
        return numbers[0]
    else:
        return x
print(max_number(numbers))

