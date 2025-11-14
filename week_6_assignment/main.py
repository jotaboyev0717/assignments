def calculate_price_per_ticket(event_tuple):
    event_id, artist_name, tickets_sold, revenue = event_tuple
    return revenue / tickets_sold


def find_top_earning_event(events):
    if len(events) == 0:
        return None
    
    max_revenue = events[0][3]
    top_event_id = events[0][0]
    
    for event in events:
        if event[3] > max_revenue:
            max_revenue = event[3]
            top_event_id = event[0]
        elif event[3] == max_revenue:
            if event[0] < top_event_id:
                top_event_id = event[0]
    
    return top_event_id


def get_events_by_artist(events, artist_name):
    result = []
    
    for event in events:
        if event[1] == artist_name:
            result.append(event[0])
    
    for i in range(len(result)):
        for j in range(i + 1, len(result)):
            if result[i] > result[j]:
                result[i], result[j] = result[j], result[i]
    
    return result


def get_artist_sales_summary(events):
    artists = []
    tickets = []
    
    for event in events:
        artist_found = False
        for i in range(len(artists)):
            if artists[i] == event[1]:
                tickets[i] += event[2]
                artist_found = True
                break
        
        if not artist_found:
            artists.append(event[1])
            tickets.append(event[2])
    
    summary = []
    for i in range(len(artists)):
        summary.append((artists[i], tickets[i]))
    
    for i in range(len(summary)):
        for j in range(i + 1, len(summary)):
            if summary[i][0] > summary[j][0]:
                summary[i], summary[j] = summary[j], summary[i]
    
    return summary


def analyze_ticket_sales(events):
    top_event = find_top_earning_event(events)
    imagine_events = get_events_by_artist(events, 'Imagine Dragons')
    artist_summary = get_artist_sales_summary(events)
    
    return (top_event, imagine_events, artist_summary)


events = [
    ('EV101', 'The Killers', 5000, 375000),
    ('EV205', 'Imagine Dragons', 8000, 600000),
    ('EV102', 'The Killers', 4500, 360000),
    ('EV301', 'Coldplay', 10000, 950000),
    ('EV206', 'Imagine Dragons', 8500, 680000)
]

print(analyze_ticket_sales(events))