def triangle(item):
    eng = 'abcdefghijklmnopqrstuvwxyz'
    letters = []
    for i in eng:
        letters.append(i)
    count = 0
    if item.isalpha():
        for i in item.lower():
            count += letters.index(i) + 1
    else:
        count = int(item)
    n = 1
    result = 1
    while result < count:
        n += 1
        result = n * (n + 1) / 2
    if result == count:
        return n
    else:
        return False
