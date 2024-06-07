"""
a, s, p = 1,0,0
while True:
    if d > 10:
        break
    a += 2
    p += a
    s += p
print(f'переменная s:={s} ')
"""

s = 1
for n in range(1,6):
    s *= n
print(s)