expenses = [250, 1200, 450, 800, 2000]

total = sum(expenses)
avg = total / len(expenses)

print("Total Expense:", total)
print("Average Expense:", avg)
print("Highest Expense:", max(expenses))
print("Lowest Expense:", min(expenses))
print("Number Above ₹500:", sum(x > 500 for x in expenses))
print("Number Below or Equal ₹500:", sum(x <= 500 for x in expenses))

print("Expenses Above Average:")
for x in expenses:
    if x > avg:
        print(x)