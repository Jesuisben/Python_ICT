dataIn = "../dataIn/"

print("파일에 기록합니다.")
filename = dataIn + "newfile.txt"

# 파일 객체 생성
# 1. 문법
# 파일 객체 = open(file="파일이름(확장자를 포함한 파일경로)", mode="읽기/쓰기모드", encoding="인코딩 문자열(UTF-8)")
# 2. mode는 읽기모드(r)과 쓰기모드(w)가 존재함
# -> wt는 write text라는 의미 (텍스트 모드) (t가 기본값이라 생략가능)
# -> b도 존재함 (바이너리 모드) - 텍스트가 아닌 파일 (이미지, 동영상, 음악, 압축파일, pdf 등)
# -> 모드들 : r(읽기) / w(덮어쓰기) / a(추가쓰기(append)) / x(쓰기(파일 없을때만-파일있으면 오류발생))
# 3. 읽기와 쓰기 모드를 동시에 할 수 없음 (중요!)
# 읽기 모드로 파일을 열고 읽는 일하고 파일을 닫고
# 다시 쓰기모드로 파일을 열고 쓰는 일하고 파일을 닫아야 함
# 4. 쓰기모드(w)일때 해당 파일이 없으면 자동으로 생성해줌 (단, 디렉토리는 존재해야함)
# 읽기모드(r)일때 해당 파일이 없으면 FileNotFoundError를 발생시킴
# 5. 파일 작업이 끝나면 반드시 닫아야 함 ( 객체.close() )
# 파일을 닫기 전에는 write()는 실행되지만 데이터가 메모리 버퍼에 임시 저장됨
# close() 할 때 버퍼에 있는 데이터를 실제 파일에 씀
myfile01 = open(file=filename, mode="wt", encoding="UTF-8")
print(type(myfile01)) # <class '_io.TextIOWrapper'>

members = ["홍영식", "김민수", "박진철", "강호숙"]

for men in members:
    message = f"{men}님~~안녕하세요.\n"
    myfile01.write(message)

# 파일 객체로 파일을 열때 자동으로 닫는 함수도 적고나서 일처리 하는게 좋음
myfile01.close()

print(f"{filename} 파일이 생성됨")