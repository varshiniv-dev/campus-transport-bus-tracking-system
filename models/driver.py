class Driver:
    def __init__(self,driver_id,name):
        self.driver_id=driver_id
        self.name=name
        self.violations=0
        
def update_driver_behaviour(driver,status):
    if status == "OVERSPEED":
        driver.violations += 1        
        