from time import time

mx = 5000

t = time()

floop = []
for a in range(1, mx):
    for b in range(a, mx):
        floop.append(divmod(a, b))
print(f"for loop: {(time() - t): .4f} s")

t = time()
compr = [divmod(a, b) for a in range(1, mx) for b in range(a, mx)]
print(f"list comprehension: {(time() - t): .4f} s")

t = time()
gener = list(divmod(a, b) for a in range(1, mx) for b in range(a, mx))

print(f"generator expression: {(time() - t): .4f} s")
