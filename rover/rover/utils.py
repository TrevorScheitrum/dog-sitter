
def calculateSitterScore(name):
    sitterScore = 5 * (float(len(''.join(set(name))))/26)
    return sitterScore

def calculateOverallSitterRank(stayObjects,sitterScore):
    ratingScoreList = []
    stayCount = 0
    ratingScore = 0
    sitterCount = 0
    
    for count,stay in enumerate(stayObjects):
        ratingScoreList.append(stay.rating)
        sitterCount = count

    if sitterCount > 0:
        ratingScore = float(sitterScore) / sitterCount

    if sitterCount > 1:
        if sitterCount >= 10:
            overallSitterRank = ratingScore
        else:
            overallSitterRank = float(ratingScore + sitterScore) / 2   
    else:
        overallSitterRank = sitterScore
    return overallSitterRank