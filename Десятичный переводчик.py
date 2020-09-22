def decimal_translator(number, base):
    for i in str(number):
        if int(i) >= base:
            return None
    numbers = []
    for i in str(number):
        numbers.append(int(i))
    numbers.reverse()
    answer = 0
    for i in range(len(numbers)):
        answer += base ** i * numbers[i]
    return answer
print(decimal_translator(10, 2))
