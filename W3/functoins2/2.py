from movies import movies
def movies_above(*movies):
    result = []
    for mov in movies:
        if mov['imdb'] > 5.5:
            result.append(mov['name'])
    return result
print(*movies_above(*movies), sep = '\n')