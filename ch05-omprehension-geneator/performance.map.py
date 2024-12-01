from time import time

mx = 2 * 10**7
t = time()
abs_loop = []

for n in range(mx):
    abs_loop.append(abs(n))
print(f"for loop: {(time() - t): .4f} s")

t = time()
abs_list = [abs(n) for n in range(mx)]
print(f"list comprehension: {(time() - t): .4f} s")

t = time()
abs_map = list(map(abs, range(mx)))
print(f"map: {(time() - t): .4f} s")
