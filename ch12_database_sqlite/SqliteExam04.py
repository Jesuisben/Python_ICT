######################################################
filename = 'mem.txt'
myfile = open(file=filename, mode='r', encoding='utf-8')
mylist = [item.strip() for item in myfile.readlines()]
print(mylist)
myfile.close()
######################################################
import sqlite3

# 데이터베이스 연결
conn = sqlite3.connect('mem.db')
mycursor = conn.cursor()

# ✅ 기존 테이블이 있으면 삭제하고 새로 생성
mycursor.execute("DROP TABLE IF EXISTS members")

create_table_sql = """
CREATE TABLE members (
    id TEXT PRIMARY KEY,
    name TEXT
)
"""
mycursor.execute(create_table_sql)

# ✅ 데이터 삽입
sql = "INSERT INTO members(id, name) VALUES(?, ?)"
for item in mylist:
    columnlist = item.split(',')
    mycursor.execute(sql, columnlist)

# 변경 내용 저장
conn.commit()

# 연결 종료
mycursor.close()
conn.close()
print('finished')
