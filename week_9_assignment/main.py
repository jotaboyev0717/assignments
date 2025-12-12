def organize_sales(ticket_log):
    cinema_dict = {}
    for entry in ticket_log:
        parts = entry.split("::")
        movie = parts[0]
        showtime = parts[1]
        sold = int(parts[2])
        if movie not in cinema_dict:
            cinema_dict[movie] = []
        cinema_dict[movie].append((showtime, sold))
    return cinema_dict

def calculate_box_office(cinema_dict):
    for movie, shows in cinema_dict.items():
        total = 0
        for show in shows:
            total += show[1]  
        print(f"{movie}: {total} tickets sold")

ticket_log = [
    "Avatar::10:00AM::50",
    "Titanic::11:00AM::30",
    "Avatar::2:00PM::100",
    "StarWars::1:00PM::80",
    "Titanic::4:00PM::40",
    "StarWars::5:00PM::120"
]

cinema_dict = organize_sales(ticket_log)
calculate_box_office(cinema_dict)
