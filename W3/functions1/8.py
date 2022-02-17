def spy_game(*arr):
    starr = [str(x) for x in arr]
    string = ''.join(starr)
    print(True if '007' in string else False)
spy_game(*(list(map(int, input().split()))))