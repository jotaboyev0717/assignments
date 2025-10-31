def calculate_tickets_value(ticket_type, tickets_resolved, priority_level):
    if ticket_type == "technical":
        if priority_level == "low":
            ticket_value = 20
        elif priority_level == "medium":
            ticket_value = 35
        else:  
            ticket_value = 55
    elif ticket_type == "billing":
        if priority_level == "low":
            ticket_value = 15
        elif priority_level == "medium":
            ticket_value = 25
        else:
            ticket_value = 40
    else: 
        if priority_level == "low":
            ticket_value = 10
        elif priority_level == "medium":
            ticket_value = 18
        else:
            ticket_value = 28

    return tickets_resolved * ticket_value


def calculate_resolution_efficiency(agent_quarters, baseline_tickets, resolved_tickets):
    expected_tickets = 1000 + (agent_quarters * 100)
    ticket_capacity = expected_tickets - baseline_tickets
    efficiency_percent = ((resolved_tickets - baseline_tickets) / ticket_capacity) * 100
    return round(efficiency_percent, 1)


def determine_performance_level(efficiency_percent):
    if efficiency_percent < 50:
        return "Developing Level"
    elif efficiency_percent < 60:
        return "Competent Level"
    elif efficiency_percent < 70:
        return "Proficient Level"
    elif efficiency_percent <= 85:
        return "Advanced Level"
    else:
        return "Expert Level"


def calculate_performance_bonus(value, tickets, level):
    if level == "Developing Level":
        multiplier = 0.5
    elif level == "Competent Level":
        multiplier = 1.0
    elif level == "Proficient Level":
        multiplier = 1.2
    elif level == "Advanced Level":
        multiplier = 1.5
    else:
        multiplier = 1.8

    base_bonus = value * 0.05 + tickets * 2
    final_bonus = base_bonus * multiplier
    return round(final_bonus, 1)


def needs_additional_training(service_weeks, total_tickets, avg_efficiency):
    if service_weeks >= 6 and avg_efficiency < 50:
        return True
    elif total_tickets < 100 and avg_efficiency < 60:
        return True
    elif service_weeks >= 4 and avg_efficiency < 40:
        return True
    else:
        return False


def generate_quality_report(agent_name, ticket_type, tickets, priority_level,
                            agent_quarters, baseline_tickets, resolved_tickets, service_weeks):

    print("========================================")
    print(f"Quality Report for: {agent_name}")
    print("----------------------------------------")
    print(f"Ticket Type: {ticket_type}")
    print(f"Tickets Resolved: {tickets}")
    print(f"Priority Level: {priority_level}")

    value = calculate_tickets_value(ticket_type, tickets, priority_level)
    print(f"Tickets Value: ${value}")

    efficiency = calculate_resolution_efficiency(agent_quarters, baseline_tickets, resolved_tickets)
    level = determine_performance_level(efficiency)
    bonus = calculate_performance_bonus(value, tickets, level)
    training_needed = needs_additional_training(service_weeks, tickets, efficiency)

    print("Efficiency Analysis:")
    print(f"  Experience: {agent_quarters} quarters, Baseline: {baseline_tickets}, Resolved Tickets: {resolved_tickets}")
    print(f"  Efficiency: {efficiency}%")
    print(f"  Performance Level: {level}")
    print(f"Performance Bonus: ${bonus}")
    print(f"Service Weeks: {service_weeks}")
    print(f"Additional Training Needed: {'Yes' if training_needed else 'No'}\n")


print("CUSTOMER SERVICE QUALITY MONITOR")
generate_quality_report("Harper", "technical", 45, "high", 3, 800, 1150, 3)
generate_quality_report("Indigo", "billing", 60, "medium", 5, 900, 1300, 5)
generate_quality_report("Jesse", "general", 30, "low", 8, 850, 950, 7)
