def calculate_streamer_earnings(filename):
    category_totals = {}
    top_earners = []

    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) != 4:
                continue
            channel, category, ad_rev, sub_rev = parts
            try:
                ad_rev = float(ad_rev)
                sub_rev = float(sub_rev)
            except ValueError:
                continue
            total_earnings = ad_rev + sub_rev
            category_totals[category] = category_totals.get(category, 0) + total_earnings
            if total_earnings > 2000:
                top_earners.append((channel, total_earnings))
    return category_totals, top_earners

def generate_income_statement(category_totals, top_earners):
    with open("income_statement.txt", "w") as file:
        file.write("REVENUE BY CATEGORY\n")
        file.write("-------------------\n")
        for category, total in category_totals.items():
            file.write(f"{category}: ${total:.2f}\n")

        file.write("\nTOP EARNERS (> $2000)\n")
        file.write("---------------------\n")
        for channel, earnings in top_earners:
            file.write(f"{channel} (${earnings:.2f})\n")

category_totals, top_earners = calculate_streamer_earnings("streamer_income.txt")
generate_income_statement(category_totals, top_earners)
