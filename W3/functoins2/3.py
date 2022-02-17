from movies import movies
def category_sort(category):
    result = []
    for mov in movies:
        if mov['category'] == category:
            result.append(mov['name'])
    return result
category = input()
print(*category_sort(category), sep = '\n')