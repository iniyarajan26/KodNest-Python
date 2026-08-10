s = input("Enter text: ")
u = l = d = sp = o = 0

for c in s:
    if c.isupper(): u += 1
    elif c.islower(): l += 1
    elif c.isdigit(): d += 1
    elif c == ' ': sp += 1
    else: o += 1

print("Uppercase Letters:", u)
print("Lowercase Letters:", l)
print("Digits:", d)
print("Spaces:", sp)
print("Other Characters:", o)