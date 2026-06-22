try:
    num = int(input("5이상의 수를 입력하세요 : "))

    if num < 5:
        raise Exception(f"{num}는 5보다 작은 수입니다.")

    print(f"{num}를 입력하셨군요~~잘 하셨습니다^^")

except Exception as e:
    if isinstance(e, ValueError):
        print("올바른 숫자 형식을 입력해 주셔야 합니다")
        print(e)
    else:
        print("예외 발생 :", e)