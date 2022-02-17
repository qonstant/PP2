def unique_elements(*lst):
    result = []
    for i in lst:
        if i not in result:
            result.append(i)
    return result
print(*(list(map(str, input().split()))))