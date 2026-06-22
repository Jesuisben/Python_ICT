# OsTest01.py
# 운영 체제의 환경 변수나 파일, 디렉토리(폴더) 등의 자원을 제어/컨트롤하는 모듈입니다.
# 현재 위치에서 특정 폴더 생성하기
save_path = input('생성할 폴더 이름 : ')

import os

if not os.path.isdir(save_path):# 해당 폴더가 존재하지 않으면
    os.mkdir(save_path)
else:
    print('이미 존재하는 폴더입니다.')

# 특정 위치 아래에 폴더 여러개 생성하기
# 윈도우는 역슬래시가 폴더 구분자입니다.
# 특수 문자라서 반드시 역슬래시 2개로 작성해야 합니다.
targetFolder = 'd:\\'
parentPath = os.path.join(targetFolder, 'sample')
print(parentPath)

try:
    os.mkdir(parentPath)

    # for 구문을 사용하여 하위 폴더 10개를 만들어 봅니다.
    for idx in range(1, 11):
        newFolder = os.path.join(parentPath, 'folder'+ str(idx).zfill(2))
        os.mkdir(newFolder)

except FileExistsError:
    print('해당 디렉토리가 이미 존재합니다.')
# end try