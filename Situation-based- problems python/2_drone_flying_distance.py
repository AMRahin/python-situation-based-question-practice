km_flown=0
battery=100

drone_patrol=True

while drone_patrol:
    km_flown+=1
    if km_flown%3==0:
        battery-=10       
    else:
        battery-=5
        if battery==15:
            print(f"At {km_flown}km battery hit {battery}%.")
            drone_patrol=False