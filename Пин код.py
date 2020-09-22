def check_pin_code(pinCode):
    nums = pinCode.split('-')
    first = True
    second = True
    third = True
    if nums[0] == '1':
        return 'Некорректен'
    else:
        for i in range(2, int(nums[0])):
            if int(nums[0]) % i == 0:
                first = False
                return 'Некорректен'
    check_second = []
    for i in nums[1]:
        check_second.append(i)
    check_check = check_second.copy()
    check_second.reverse()
    if check_check != check_second:
        second = False
        return 'Некорректен'
    count = 0
    count_2 = -1
    while count < int(nums[2]):
        count_2 += 1
        count = 2 ** count_2
    if count != int(nums[2]):
        third = False
        return 'Некорректен'
    if first and second and third:
        return 'Корректен'
print(check_pin_code(input()))