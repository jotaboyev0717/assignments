def find_section_index(section_names, section_name):
    i = 0
    while i < len(section_names):
        if section_names[i] == section_name:
            return i
        i += 1
    return -1

def process_bookings(initial_sections, initial_seats, operations):
    sections = []
    seats = []
    
    for i in range(len(initial_sections)):
        sections.append(initial_sections[i])
        seats.append(initial_seats[i])
    
    for op in operations:
        cmd = op[0]
        
        if cmd == "ADD_SECTION":
            sec_name = op[1]
            cap = op[2]
            idx = find_section_index(sections, sec_name)
            if idx == -1:
                sections.append(sec_name)
                seats.append(cap)
                
        elif cmd == "BOOK":
            sec_name = op[1]
            num = op[2]
            idx = find_section_index(sections, sec_name)
            if idx != -1:
                if seats[idx] >= num:
                    seats[idx] = seats[idx] - num
                    
        elif cmd == "CANCEL":
            sec_name = op[1]
            num = op[2]
            idx = find_section_index(sections, sec_name)
            if idx != -1:
                seats[idx] = seats[idx] + num
    
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