# 패키지 실습
# OsExercise01.py (Python(실습).pdf (P.108))
import os
# 상위 폴더 이름 생성위치
upper_directory = "exercise"
# 상위 폴더 생성 위치
upper_path = "D:\\"

target_upper = os.path.join(upper_path, upper_directory)

if not os.path.isdir(target_upper) :
    os.mkdir(target_upper)
    print(f"{upper_path} 경로에 {upper_directory} 폴더를 생성합니다.")
else:
    print(f"{upper_path} 경로에 {upper_directory} 폴더가 이미 존재합니다.")

mylist = ["alpha", "bravo", "delta", "nova", "terra", "pixel", "orbit", "matrix", "spark", "fusion"]

try:
    for item in mylist:
        target_lower = os.path.join(target_upper, item)
        os.mkdir(target_lower)
except FileExistsError:
    print(f"{target_lower} 경로에 {item} 폴더가 이미 존재합니다.")