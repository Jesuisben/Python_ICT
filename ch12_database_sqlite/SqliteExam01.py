import sqlite3

conn = sqlite3.connect('student.db') # 접속 객체
mycursor = conn.cursor() # 커서 객체

try:
    mycursor.execute("drop table students")
except sqlite3.OperationalError:
    print('테이블이 존재하지 않습니다.')
# end try

# 테이블 생성
mycursor.execute('''
create table students(
    id text primary key,
    name text not null,
    birth text,
    gender text,
    major text,
    grade integer,
    phone text
)
''')

# 기본 데이터 추가하기
mycursor.execute("""
insert into students 
values('lee', '이민혁', '1989/12/12', 'M', '컴퓨터공학', 4, '010-1111-2222')
""")

mycursor.execute("""
insert into students 
values('kang', '강호사', '1970/07/17', 'M', '수학과', 2, '010-3333-4444')
""")

# 리스트를 사용한 데이터 추가하기
student_list =[
    ('jo', '조용원', '1985/03/01', 'F', '체육학과', 2, '010-5555-6666'),
    ('ko', '고두식', '1990/06/25', 'M', '디자인과', 2, '010-7777-8888'),
    ('sim', '심유이', '1950/07/17', 'F', '연극영화과', 2, '010-2222-6666')
]

sql = """
insert into students 
values(?, ?, ?, ?, ?, ?, ?)
"""

mycursor.executemany(sql, student_list)

print('# id로 조회')
findId = 'kang22'
sql = "select * from students where id = '%s'"
mycursor.execute(sql % findId)
result = mycursor.fetchone()
# print(type(result))

if result == None:
    print('존재하지 않는 회원입니다.')
else:
    print('#'.join([str(item) for item in result]))
# end if

print('\n# 데이터 정렬')
sql = "select * from students order by name desc"
for row in mycursor.execute(sql):
    print(row)
# end if

print('\n# 컬럼별 출력하기')
for (id, name, birth, gender, major, grade, phone) in mycursor.execute(sql):
    print(f'{id}, {name}, {birth}, {gender}, {major}, {grade}, {phone}')
# end if

print('\n# like 검색')
findWord = '이'
sql = f"select * from students where name like '%{findWord}%' "
print(f'이름에 "{findWord}"라는 글자가 포함된 사람')
mycursor.execute(sql)
for row in mycursor.fetchall():
    print(row)

# execute() 메소드의 2번째 매개 변수는 tuple 또는 list 타입
print('\n# update 구문')
pid, newName = 'lee', '이순철'
sql = "update students set name = ? where id = ?"
mycursor.execute(sql, (newName, pid))

print('\n# delete 구문')
pid = 'sim'
sql = "delete from students where id = ?"
mycursor.execute(sql, (pid,))

print('\n# 최종 출력')
sql = "select * from students order by id asc "
for row in mycursor.execute(sql):
    print(row)
# end for

conn.commit()

mycursor.close()
conn.close()
print('finished')