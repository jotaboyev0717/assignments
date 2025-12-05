def calculate_quote(quote_text):
    lines = quote_text.split('\n')

    subtotal = 0.0
    credit = 0.0
    surcharge_rate = 0.0

    for line in lines:
        line = line.strip()

        if "hrs x" in line:
            parts = line.split(":")           
            work = parts[1].strip()          
            
            hours = float(work.split("hrs")[0].strip())         
            rate  = float(work.split("x $")[1].split("/")[0])   

            subtotal += hours * rate

        elif line.startswith("SURCHARGE"):
            percent = line.split(":")[1].replace("%", "").strip()
            surcharge_rate = float(percent) / 100

        elif line.startswith("CREDIT"):
            amount = line.split(":")[1].replace("$", "").strip()
            credit = float(amount)

    total = (subtotal - credit) * (1 + surcharge_rate)
    return f"${total:.2f}"


# Test Case 1: Standard quote
quote1 = """Design : 10 hrs x $50.00/hr
Coding : 20 hrs x $60.00/hr
SURCHARGE: 20%
CREDIT: $100.00"""
print(calculate_quote(quote1))

# Test Case 2: No credit
quote2 = """Consulting : 5 hrs x $100.00/hr
Reporting : 2 hrs x $50.00/hr
SURCHARGE: 5%"""
print(calculate_quote(quote2))

# Test Case 3: Credit, no surcharge
quote3 = """Testing : 10 hrs x $30.00/hr
Docs : 5 hrs x $20.00/hr
CREDIT: $50.00
SURCHARGE: 0%"""
print(calculate_quote(quote3))