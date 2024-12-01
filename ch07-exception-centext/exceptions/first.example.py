gen = (n for n in range(2))
print(next(gen))
print(next(gen))
# print(next(gen))  # StopIteration

my_list = [1, 2, 3]
# print(my_list[5])  # IndexError: list index out of range

my_dict = {"a": "A", "b": "B"}
# print(my_dict['c'])  # KeyError: 'c'

print(1 / 0)  # ZeroDivisionError: division by zero
