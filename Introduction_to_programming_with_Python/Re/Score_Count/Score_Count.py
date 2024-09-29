def score_count(x):
    if x == 1:
        return 1
    elif x == 2:
        return 2
    elif x == 3:
        return 3
    else:
        return score_count(x-1) + score_count(x-2) + score_count(x-3)
    

print(score_count(5))