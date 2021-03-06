# Bite 107. Filter numbers with a list comprehension

"""
    Complete the function below that receives a list of numbers and returns only the even numbers that are > 0 and even (divisible by 2).

    The challenge here is to use Python's elegant list comprehension feature to return this with one line of code (while writing readable code).
"""

numberList = list(range(-10, 11))


def filter_positive_even_numbers(numbers):
    """Receives a list of numbers, and returns a filtered list of only the
       numbers that are both positive and even (divisible by 2), try to use a
       list comprehension."""
    result = []
    for number in numbers:
        if (number > 0 and (number % 2 == 0)):
            result.append(number)

    return result


print(filter_positive_even_numbers(numberList))
