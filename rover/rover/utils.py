import re

def remove_non_ascii_letters(string):
    return re.compile(r'[^a-zA-Z]').sub('',string)

def calculate_sitter_score(name):
    name = remove_non_ascii_letters(name)
    #Sitter Score is 5 times the fraction of the English alphabet comprised 
    #by the disinct letters in what we've recovered of the sitter's name.
    #so we throw the name into a set to get only unique letters
    sitter_score = 5.0 * (len(''.join(set(name)))/26.0)
    return sitter_score

def calculate_rating_score(stay_objects):
    total = 0
    rating_score = 0
    
    #add up ratings from stays
    for stay in stay_objects:
        total += stay.rating
    
    #calculate their average stay rating
    if len(stay_objects) > 0:
        rating_score = float(total) / len(stay_objects)
        
    return rating_score
    
def calculate_overall_sitter_rank(stay_objects,sitter_score):
    stay_count = len(stay_objects)
    rating_score = calculate_rating_score(stay_objects)
    
    #We want the overall score to be a ratio of the sitter's rating score, and sitter score between 0-10
    if stay_count <= 0:
        overall_sitter_rank = sitter_score
    elif stay_count < 10:
        stay_ratio = stay_count/10
        sitter_ratio = (10-stay_count)/10
        overall_sitter_rank = float(rating_score*stay_ratio) + float(sitter_score*sitter_ratio)
    else:
        overall_sitter_rank = rating_score
        
    return overall_sitter_rank