n = int(input("Enter number: "))
even = odd = 0

for i in range(1, 11):
    r = n * i
    print(f"{n} x {i} = {r} - {'Even' if r % 2 == 0 else 'Odd'}")
    if r % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even Results:", even)
print("Odd Results:", odd)