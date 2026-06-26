# 예외 처리
# 예외처리 동작
# (try 블록 실행 -> 예외 발생 -> 해당 예외의 예외 처리 블록의 코드 실행)
# 만약 2가지 예외처리를 하고 try코드 내에 해당 2가지 예외가 둘다 존재해도
# try 블록 기준으로 가장 먼저 실행되는 예외에 의해 해당 예외처리 블록으로 이동해서 실행됨
# (예외처리 코드가 적힌 순서와는 무관함)

try:
    x, y = 4, 0
    z = x / y
    print(z)

    mylist = [1, 2, 3]
    print(mylist)

    # 리스트 범위를 벗어난 인덱스에 접근할때
except IndexError as err:
    print("인덱스 접근 범위 초과")
    print(err)

    # 숫자를 0으로 나눌때
except ZeroDivisionError as err:
    print("0으로 나누시면 안됩니다.")
    print(err)

    # 모든 예외의 부모 클래스 (모든 예외)
    # (Java의 catch (Exception e)와 같은 개념)
    # 반드시 맨 아래에 써야 함
    # Exception은 모든 예외의 부모 클래스이므로
    # 위에 쓰면 IndexError, ZeroDivisionError도 Exception이 먼저 잡아버림
    # (동일 예외에 해당하는 except가 여러 개일 경우 위에 있는 except가 실행됨)
except Exception as err:
    print("기타 나머지 예외 정보")
    print(err)
else:
    print("예외가 없을때 만 실행이 됩니다.")
finally:
    print("나는 무조건 실행이 됩니다.")


# # Exception01.py
#
# try:
#     mylist = [1, 2, 3]
#     print(mylist[5])
#
#     x, y = 4, 0
#     z = x / y
#     print(z)
#
#     print('예외가 발생하면 나는 실행이 안되요.')
#
# except ZeroDivisionError as err:
#     print('0으로 나누지 마세요.')
#     print('예외 객체 정보 : %s' % err)
#
# except IndexError as err:
#     print('인덱스 접근 범위 초과.')
#     print('예외 객체 정보 : %s' % err)
#
# except Exception as err:
#     print('기타 나머지 예외 발생')
#     print('예외 객체 정보 : %s' % err)
#
# else:
#     print('예외가 발생하지 않으면 실행이 됩니다.')
#
# finally:
#     print('예외 발생 여부와 상관 없이 무조건 실행 됩니다.')