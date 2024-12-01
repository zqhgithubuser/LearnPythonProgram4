import sys
from decimal import Decimal as D

print(7 / 4, 7 // 4)  # 1.75 1
print(-7 / 4, -7 // 4)  # -1.75 -2

print(int("10110", base=2))  # 22

print(sys.float_info)

print(D(3.14))
print(D("3.14"))
print(D(0.3) - D(0.1) * 3)
print(D("0.3") - D("0.1") * 3)  # 0.0
