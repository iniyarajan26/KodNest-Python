name = input("Customer Name: ")
age = int(input("Age: "))
tickets = int(input("Number of Tickets: "))
price = 120 if age < 12 else 150 if age >= 60 else 200
total = price * tickets
if tickets >= 5: total *= 0.9
print("Customer Name:", name, "\nTicket Price:", price, "\nNumber of Tickets:", tickets, "\nTotal Amount:", total)