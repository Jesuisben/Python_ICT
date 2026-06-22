def zfillFunc(year, month, day):
    # 오늘은 2021년 03월 01일입니다.
    result = '오늘은 ' + str(year) + '년 ' + str(month).zfill(2) + '월 ' + str(day).zfill(2) + '일입니다.'
    return result

result = zfillFunc(2021, 3, 1)
print(result)

print(zfillFunc(2023, 10, 2))