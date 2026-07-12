height_list=[165, 181, 168, 175, 190, 169]
passed_people=0

for each_person_height in height_list:
    if each_person_height>=170:
        print(f"Your height is {each_person_height},so you are elligible.")
        passed_people+=1
    else:
        print(f"Your height is {each_person_height},you are not elligible")

print(f"Total passed men:{passed_people}")