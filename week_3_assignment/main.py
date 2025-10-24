print("=== Book Rental System ===")
print("Enter membership type: student, regular, or premium")
print("Type 'done' when finished selecting books\n")

total = 0.0

while True:
    category = input("Enter membership type: ")

    if category == "done":
        break

    if category == "student":
        price = 2.00
    elif category == "regular":
        price = 4.00
    elif category == "premium":
        price = 6.00
    else:
        print("Invalid membership type. Please enter student, regular, or premium.")
        continue

    total += price
    print(f"Price: ${price:.2f}")
    print(f"Current total: ${total:.2f}\n")

discount = 0.0
if total >= 15.00:
    discount = 2.50

final_total = total - discount

print("\n=== Rental Summary ===")
print(f"Subtotal: ${total:.2f}")
if discount > 0:
    print(f"Bulk Rental Discount: ${discount:.2f}")
else:
    print("No discount.")
print(f"Final Total: ${final_total:.2f}")
print("Thank you for your rental!")