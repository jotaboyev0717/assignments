title1 = input("1st book title: ")
price1 = float(input("1st book price: "))
quantity1 = int(input("1st book quantity: "))

title2 = input("2nd book title: ")
price2 = float(input("2nd book price: "))
quantity2 = int(input("2nd book quantity: "))

title3 = input("3rd book title: ")
price3 = float(input("3rd book price: "))
quantity3 = int(input("3rd book quantity: "))

name = input("Customer name: ")
is_faculty_staff = input("Is faculty/staff (yes/no): ") == "yes"
is_textbook_order = input("is_textbook_order (yes/no): ") == "yes"
number_of_books = int(input("total number books: "))

subtotal = price1 * quantity1 + price2 * quantity2 + price3 * quantity3

faculty_discount = 0.20 * subtotal * is_faculty_staff
textbook_discount = 0.25 * subtotal * is_textbook_order

main_discount = faculty_discount * (faculty_discount >= textbook_discount) + textbook_discount * (textbook_discount > faculty_discount)

bulk_discount = 0.08 * subtotal * (number_of_books >= 10)
total_discounts = main_discount + bulk_discount

small_order_fee = 1000 * (number_of_books < 3)
subtotal_after_discount = subtotal - total_discounts + small_order_fee

tax = 0.05 * subtotal_after_discount * (not is_textbook_order)
shipping = 20000 * (subtotal < 200000)

final_total = subtotal_after_discount + tax + shipping
net_savings = total_discounts - small_order_fee - tax - shipping

print(f"Customer: {name}")
print(f"Faculty/Staff: {is_faculty_staff}")
print(f"Order: {is_textbook_order}\n")

print("Purchased books:")
print(f"{title1}: {quantity1} * {price1} = {quantity1 * price1}")
print(f"{title2}: {quantity2} * {price2} = {quantity2 * price2}")
print(f"{title3}: {quantity3} * {price3} = {quantity3 * price3}")

print(f"\nSubtotal: {subtotal}")
print(f"\nFaculty Discount Eligible: {is_faculty_staff}  {faculty_discount}")
print(f"Textbook Discount Eligible: {is_textbook_order}  {textbook_discount}")
print(f"Applied Discount better: {main_discount}")
print(f"Bulk Discount Eligible: {(number_of_books >= 10)}  {bulk_discount}")
print(f"Total Discount: {total_discounts}")

print(f"\nSmall Order Fee Applied: {(number_of_books < 3)} → {small_order_fee}")
print(f"Subtotal After Discounts and Fees: {subtotal_after_discount}")
print(f"\nTax Applied (5% if not textbook): {not is_textbook_order}  {tax}")
print(f"Free Shipping Eligible: {(subtotal >= 200000)}  {shipping}")

print(f"\ntotal: {final_total}")
print(f"Net savings / Extra fees: {net_savings}")