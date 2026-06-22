import sqlite3
from xml.etree.ElementTree import parse

def getAllInfo(mycursor):
    for onetuple in mycursor:
        print('아이디 : ' + onetuple[0], end='')
        print(', 과목 : ' + onetuple[1], end='')
        print(', 점수 : ' + str(onetuple[2]), end='')
        print()

# -----------------------------
# 1) SQLite DB 연결
# -----------------------------
conn = sqlite3.connect('student.db')
mycursor = conn.cursor()

# -----------------------------
# 2) 테이블 생성
# -----------------------------
try:
    mycursor.execute("DROP TABLE sungjuk")
except sqlite3.OperationalError:
    print('테이블이 존재하지 않습니다.')

mycursor.execute('''
CREATE TABLE sungjuk (
    id TEXT,
    subject TEXT,
    jumsu INTEGER
)
''')

# -----------------------------
# 3) XML 읽기
# -----------------------------
tree = parse('sungjuk.xml')
root = tree.getroot()

# -----------------------------
# 4) XML 데이터를 DB에 INSERT
# -----------------------------
insert_sql = "INSERT INTO sungjuk(id, subject, jumsu) VALUES(?, ?, ?)"
data_list = []

for student in root.iter('student'):
    sid = student.find('id').text
    subject = student.find('subject').text
    jumsu = int(student.find('jumsu').text)
    data_list.append((sid, subject, jumsu))

# 다량 INSERT
mycursor.executemany(insert_sql, data_list)
conn.commit()

# -----------------------------
# 5) DB 내용 출력
# -----------------------------
sql = "SELECT * FROM sungjuk"
mycursor.execute(sql)
print('-' * 40)
getAllInfo(mycursor)

print('-' * 40)
sql = "SELECT * FROM sungjuk ORDER BY id, subject"
for row in mycursor.execute(sql):
    print(row)

# -----------------------------
# 6) 종료
# -----------------------------
mycursor.close()
conn.close()
print('-' * 40)
print('작업 완료^^')
