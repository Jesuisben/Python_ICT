# os 모듈 import 받기
import os

# 하위 폴더를 생설할 상위 폴더의 이름 입력받기
saved_path = input("생성할 폴더 이름 : ")

# 상위 폴더가 존재하지 않으면 직접 생성하는 조건문
if not os.path.isdir(saved_path) :
    # 폴더 생성 경로를 입력하지 않으면 기본값은 현재 파일이 있는 폴더임
    os.mkdir(saved_path)
    print("폴더를 생성합니다.")
else:
    print("이미 존재하는 폴더입니다.")

# 역슬래쉬(\)를 2번 쓰는 이유 : \는 이스케이프 문자라 하나만 쓰면 특수문자로 인식됨
# \\처럼 두 번 써야 문자 그대로의 \로 인식됨
# 드라이브 문자는 대소문자 구분이 없어서 D:\\ 혹은 d:\\ 둘다 가능
target_folder = "D:\\"

# os.path.join() : 매개변수들을 경로 구분자(\)로 이어주는 함수
# **원래 \ 기호가 이스케이프 문자여서 여기서도 join함수가 경로 구분자를
# \\ 이렇게 2개를 써줘야하나 싶지만 이스케이프 문자가 작동하는건
# 소스코드에 문자열을 직접 타이핑 했을때 뿐이여서 이때는 \ 하나만 써줘도 \를 문자열로 인식함
# 위의 target_folder는 문자열을 직접 타이핑했기 때문에 \를 2개 적음
parent_path = os.path.join(target_folder, saved_path)
print(parent_path)

# "D:\\"에 폴더 생성
if not os.path.isdir(parent_path) :
    os.mkdir(parent_path)


try:
    for idx in range(1, 11):
        # 매개변수의 숫자만큼의 자리를 확보하고 빈 자리만큼 숫자 0을 채워 주는 함수
        # zfill(2): 2자리 확보 후 빈 자리를 0으로 채움 (예: 1 → "01")
        new_folder = os.path.join(parent_path, "folder" + str(idx).zfill(2))

        # 해당 경로에 디렉토리 생성하는 함수
        os.mkdir(new_folder)
except FileExistsError:
    print("해당 디렉토리가 이미 존재합니다.")






















# # OsTest01.py
# # 운영 체제의 환경 변수나 파일, 디렉토리(폴더) 등의 자원을 제어/컨트롤하는 모듈입니다.
# # 현재 위치에서 특정 폴더 생성하기
# save_path = input('생성할 폴더 이름 : ')
#
# import os
#
# if not os.path.isdir(save_path):# 해당 폴더가 존재하지 않으면
#     os.mkdir(save_path)
# else:
#     print('이미 존재하는 폴더입니다.')
#
# # 특정 위치 아래에 폴더 여러개 생성하기
# # 윈도우는 역슬래시가 폴더 구분자입니다.
# # 특수 문자라서 반드시 역슬래시 2개로 작성해야 합니다.
# targetFolder = 'd:\\'
# parentPath = os.path.join(targetFolder, 'sample')
# print(parentPath)
#
# try:
#     os.mkdir(parentPath)
#
#     # for 구문을 사용하여 하위 폴더 10개를 만들어 봅니다.
#     for idx in range(1, 11):
#         newFolder = os.path.join(parentPath, 'folder'+ str(idx).zfill(2))
#         os.mkdir(newFolder)
#
# except FileExistsError:
#     print('해당 디렉토리가 이미 존재합니다.')
# # end try