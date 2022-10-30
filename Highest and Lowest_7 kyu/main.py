def high_and_low(numbers):
    s = [int(i) for i in numbers.split(" ")]
    return f'{max(s)} {min(s)}'