def choice(round_score, my_score, opponent_score):
    import random
    d6 = [1,2,3,4,5,6]
    macron = pow(1-1/6, (100-my_score)/4)
    scholz = pow(1-1/6, (100-(opponent_score+round_score))/4)
    if my_score-opponent_score >= 10:
        if round_score >= 20:
            hold = 0
        if round_score <= 20:
            hold = 1
    elif my_score-opponent_score >= 30:
        if round_score >= 25:
            hold = 0
        if round_score <= 25:
            hold = 1
    else:
        if round_score >= 16:
            hold = 0
        if round_score <= 16:
            hold = 1
    advice = random.choice(d6)
    if advice <= 5:
        if((round_score >= 15*(1+macron-scholz) and scholz < 0.5) or opponent_score+round_score >= 100):
            return False
        else:
            return True
    if advice == 6:
        if hold == 0:
            return False
        if hold == 1:
            return True
