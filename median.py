"""Median calculator."""

def median(numbers):
    if len(numbers) % 2 == 0:
        var = len(numbers) // 2
        val_1 = numbers[var]
        val_2 = numbers[var - 1]
        return (val_1 + val_2) / 2
    else:
        return numbers[len(numbers) // 2]

"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(median(numbers))
