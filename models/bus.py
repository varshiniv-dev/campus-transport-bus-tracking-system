class Bus:
    def __init__(self,bus_id,route_id,driver_id):
        self.bus_id=bus_id
        self.route=route_id
        self.driver=driver_id
        self.speed=0
        self.location=(0.0,0.0)
        self.status="Running"

#Each bus is an object with dynamic state like speed, location, and status.
    