from movies import movies
def average_imdb(*movies):
    sum = 0
    for mov in movies:
        sum += float(mov['imdb'])
    return sum/len(movies)
print(average_imdb(*movies))