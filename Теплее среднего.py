def warmer_day(temperatures):
    days = []
    for i in temperatures:
        for j in i:
            days.append(j)
    average = sum(days) / len(days)
    for i in range(len(days)):
        if days[i] > average:
            return i + 1
