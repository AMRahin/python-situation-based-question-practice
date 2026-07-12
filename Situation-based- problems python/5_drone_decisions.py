import random
import time
drone_on=True

while drone_on:
    distance=round(random.uniform(0.5,10.0),1)
    print(f"Distance:{distance}m")
    if distance>5:
        print("continue flying")
    elif distance<=5 and distance>2:
        print("slow down")
    elif distance<=2 and distance>1:
        print("hover")
    elif distance<=1:
        print("move backward")
    
    time.sleep(0.5) 