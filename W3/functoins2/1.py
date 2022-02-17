from movies import movies
def score_above(movie):
    score = True
    for mov in movies:
        if mov['name'] == movie and mov['imdb'] > 5.5:
            score = True 
        elif mov['name'] == movie and mov['imdb'] < 5.5:
            score = False
    return score   
print(score_above(input()))