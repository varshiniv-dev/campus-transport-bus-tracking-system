SPEED_LIMIT = 40 #kilometer per hour
def check_speed(speed):
    if speed > SPEED_LIMIT:
        return "OVER SPEEDING!"
    return "NORMAL!"