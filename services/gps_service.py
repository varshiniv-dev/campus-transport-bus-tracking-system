import random
def get_live_location():
    lat=12.520 + random.uniform(-0.01,0.01)
    lon=76.900 + random.uniform(-0.01,0.01)
    return lat, lon

#since real GPS hardware isn't available, location updates are simulated realistically using coordinate variance.   