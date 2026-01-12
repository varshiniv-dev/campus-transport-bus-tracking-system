import random

def breakdown_check():
    return random.choice([True,False,False,False]) 
  
##if breakdown occurs, notifies admin, alert campus security, change bus status.

def accident_detect(speed, sudden_drop):
    if speed > 30 and sudden_drop :
        return True
    return False
#accidents are inferred using sudden deceleration combined with speed thresholds.

#checks the breakdowns
import random
def check_breakdowns():
    return random.choice([False,False,False,False,True])

#accident detection
def detect_accident(speed,sudden_drop):
    if speed > 30 and sudden_drop:
        return True
    return False    

#Accidents are inferred using sudden deceleration logic.