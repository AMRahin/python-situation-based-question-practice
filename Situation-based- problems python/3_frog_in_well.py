day=0
frog_climbs=0
frog_climbing=True
while frog_climbing:
    day+=1
    frog_climbs+=3
    if frog_climbs==10:
        print(f"At {day}day frog reached the top")
        frog_climbing=False
    frog_climbs-=2
          
