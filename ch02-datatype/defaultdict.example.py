from collections import defaultdict

dd = defaultdict(int)
# dd['age'] = dd['age'] + 1   # 默认值为 0
dd["age"] += 1
print(dd)  # defaultdict(<class 'int'>, {'age': 1})
