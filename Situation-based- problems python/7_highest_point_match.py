score_list=[34, 45, 28, 52, 41]

highest_score=0


for each_match_score in score_list:
    if each_match_score>highest_score:
        highest_score-=highest_score
        highest_score+=each_match_score
    

print(highest_score)  