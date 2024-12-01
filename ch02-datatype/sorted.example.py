from operator import itemgetter

a = [(5, 3), (1, 3), (1, 2), (2, -1), (4, 9)]
print(sorted(a))  # [(1, 2), (1, 3), (2, -1), (4, 9), (5, 3)]
print(sorted(a, key=itemgetter(0)))  # [(1, 3), (1, 2), (2, -1), (4, 9), (5, 3)]
print(sorted(a, key=itemgetter(0, 1)))  # [(1, 2), (1, 3), (2, -1), (4, 9), (5, 3)]
print(sorted(a, key=itemgetter(1)))  # [(2, -1), (1, 2), (5, 3), (1, 3), (4, 9)]
sorted(a, key=itemgetter(1), reverse=True)  # [(2, -1), (1, 2), (5, 3), (1, 3), (4, 9)]
