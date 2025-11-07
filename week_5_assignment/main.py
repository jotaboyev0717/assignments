def find_section_index(section_names, section_name):
    i = 0
    while i < len(section_names):
        if section_names[i] == section_name:
            return i
        i += 1
    return -1

def process_bookings(initial_sections, initial_seats, operations):
    sections = list(initial_sections)
    seats = list(initial_seats)
    
    for op in operations:
        command = op[0]
        
        if command == "ADD_SECTION":
            sec_name = op[1]
            capacity = op[2]
            idx = find_section_index(sections, sec_name)
            if idx < 0:
                sections.append(sec_name)
                seats.append(capacity)
                
        elif command == "BOOK":
            sec_name = op[1]
            num_seats = op[2]
            idx = find_section_index(sections, sec_name)
            if idx >= 0 and seats[idx] >= num_seats:
                seats[idx] = seats[idx] - num_seats
                
        elif command == "CANCEL":
            sec_name = op[1]
            num_seats = op[2]
            idx = find_section_index(sections, sec_name)
            if idx >= 0:
                seats[idx] = seats[idx] + num_seats
    
    return sections, seats

sections = ["Orchestra", "Mezzanine", "Balcony"]
seats = [50, 75, 100]
booking_operations = [
    ["BOOK", "Mezzanine", 10],
    ["BOOK", "Orchestra", 60],
    ["CANCEL", "Balcony", 5],
    ["ADD_SECTION", "Box Seats", 12],
    ["BOOK", "Orchestra", 20]
]

final_sections, final_seats = process_bookings(sections, seats, booking_operations)
print(final_sections)
print(final_seats)
