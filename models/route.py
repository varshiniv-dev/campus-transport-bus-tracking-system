class Route:
    def __init__(self, route_id,stops):
        self.route_id=route_id
        self.stops=stops
        
def route_deviation(current, allowed):
    if current not in allowed:
        return True
    return False

#the system continously validates the bus position against the predefined route.