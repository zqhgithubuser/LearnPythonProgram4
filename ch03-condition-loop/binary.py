n = 39
remainders = []
while n > 0:
    n, remainder = divmod(n, 2)
    remainders.append(remainder)
remainders.reverse()
print("".join([str(remainder) for remainder in remainders]))  # 100111
