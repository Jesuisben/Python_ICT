# ReverseCharacter.py
# 특정 문자열을 뒤집어주는 함수 reverse()를 구현해 보세요.
# 사용자가 시작 위치와 끝 위치를 지정할 수 있습니다.
# 명시하지 않으면, 전체 문자을 뒤집어 줍니다.

def reverse(setenence, start=None, end=None):
    result = ''  # 반환할 문자열

    if start == None:  # 전체 뒤집기
        length = len(setenence)  # 문자열 개수
        for idx in range(length):
            result = setenence[idx] + result

    else:
        for idx in range(start, end + 1):  # end + 1는 끝 위치도 포함하겠다
            result = setenence[idx] + result
    # end if

    return result


# end def


setenence = 'hello~everyone'
result = reverse(setenence)
print(result)

result = reverse(setenence, 3, 8)
print(result)
