def choice(round_score, my_score, opponent_score):
    opponentChance = pow(5/6, (100-opponent_score)/4)
    selfChance = pow(5/6, (100-(my_score + round_score))/4)
    if((round_score >= 16*(1+opponentChance-selfChance) and selfChance < 0.5) or round_score + my_score >= 100):
        return False
    return True
