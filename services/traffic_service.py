import random


def traffic_status():
    return random.choice(["Clear", "Moderate", "Heavy"])


def route_violation(current_stop, allowed_stops):
    return current_stop not in allowed_stops
# delays are predicted proactively using traffic conditions. traffic_status
