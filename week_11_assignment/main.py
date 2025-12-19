def redeem_prize(players, prizes, player, item, qty):
    if player not in players:
        raise KeyError("Player not found")

    if item not in prizes:
        raise KeyError("Prize not available")

    if not isinstance(qty, int) or qty < 1:
        raise ValueError("Quantity must be positive integer")

    cost = prizes[item]["cost"] * qty

    if qty >= 3:
        cost -= 100
        if cost < 0:
            cost = 0

    if players[player]["tickets"] < cost:
        raise ValueError("Not enough tickets")

    players[player]["tickets"] -= cost
    return cost


def process_redemptions(players, prizes, queue):
    total_spent = 0
    failed = 0

    for player, item, qty in queue:
        try:
            total_spent += redeem_prize(players, prizes, player, item, qty)
        except (KeyError, ValueError) as e:
            print(f"Redemption Error for {player}: {e}")
            failed += 1

    return {
        "tickets_spent": total_spent,
        "failed_redemptions": failed
    }


# ===== TEST =====
prizes = {
    "Bear": {"cost": 500},
    "Candy": {"cost": 50}
}

players = {
    "P1": {"tickets": 1000},
    "P2": {"tickets": 100}
}

queue = [
    ("P1", "Candy", 4),
    ("P2", "Bear", 1),
    ("P9", "Toy", 1),
    ("P1", "PS5", 1),
    ("P1", "Bear", 0)
]

print(process_redemptions(players, prizes, queue))
