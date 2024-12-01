from itertools import compress

data = range(10)
even_selector = [1, 0] * 5
odd_selector = [0, 1] * 5
print(even_selector)  # [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
print(odd_selector)  # [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
even_number = list(compress(data, even_selector))
odd_number = list(compress(data, odd_selector))

print(even_number)  # [0, 2, 4, 6, 8]
print(odd_number)  # [1, 3, 5, 7, 9]
