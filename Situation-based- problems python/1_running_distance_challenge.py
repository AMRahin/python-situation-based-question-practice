day=1
todays_km=5
total_km=5

tracker_on=True

while tracker_on:
    if total_km>=50:
        print(f"you reached {total_km}km in {day}days.")
        tracker_on=False
    else:
        if day%4==0:
            day+=1
            todays_km+=0
            total_km+=0
        else:
            day+=1
            todays_km+=2
            total_km+=todays_km
