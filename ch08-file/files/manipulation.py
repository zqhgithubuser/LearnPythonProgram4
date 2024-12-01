from collections import Counter
from string import ascii_letters

chars = ascii_letters + " "


def sanitize(s, chars):
    return "".join(c for c in s if c in chars)


def reverse(s):
    return s[::-1]


with open("fear.txt", encoding="utf-8") as stream:
    lines = [line.rstrip() for line in stream]
with open("raef.txt", "w", encoding="utf-8") as stream:
    stream.write("\n".join(reverse(line) for line in lines))

# 删除除英文字母和空格外的字符
lines = [sanitize(line, chars) for line in lines]
whole = "".join(lines)
cnt = Counter(whole.lower().split())
print(cnt.most_common(3))
