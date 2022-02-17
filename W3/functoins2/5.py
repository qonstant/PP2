from movies import movies
def average_of_category(category):
    sum = 0
    cnt = 0
    for mov in movies:
        if mov['category'] == category:
            sum += float(mov['imdb'])
            cnt += 1
    return sum / cnt
print(average_of_category(input()))