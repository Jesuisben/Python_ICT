import re
import sqlite3
from xml.etree.ElementTree import parse

# ========== 1) XML 불러오기 ==========
tree = parse('shopList.xml')
shopRoot = tree.getroot()
print(type(shopRoot))
print('매장 개수 : %d' % len(shopRoot))

# ========== 2) SQLite 연결 ==========
con = sqlite3.connect('sqlite3.db')
cursor = con.cursor()

# stores 테이블이 없다면 생성
cursor.execute("""
CREATE TABLE IF NOT EXISTS stores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    address TEXT,
    phone TEXT
)
""")

# ========== 3) XML 데이터 파싱 후 DB 삽입 ==========
for store in shopRoot.iter('item'):

    # -------------------------------
    # (1) 매장명
    # -------------------------------
    name = store.find('aname1').text

    # -------------------------------
    # (2) 주소 조합
    # -------------------------------
    address01 = store.find('aname4').text
    imsi = store.find('aname5').text

    regex = r'\d\S*'
    pattern = re.compile(regex)
    mysearch = pattern.search(imsi)
    address02 = mysearch.group()

    address02 = address02.replace('번길', '번길 ')
    address02 = address02.replace('번지', '번지 ')

    address = address01 + ' ' + address02

    # -------------------------------
    # (3) 전화번호 (- → / 변환)
    # -------------------------------
    phone = store.find('aname7').text
    phone = re.sub('-', '/', phone)

    # -------------------------------
    # (4) SQLite DB에 INSERT
    # -------------------------------
    cursor.execute("""
        INSERT INTO stores (name, address, phone)
        VALUES (?, ?, ?)
    """, (name, address, phone))

# end for

# 변경사항 반영
con.commit()
con.close()

print("SQLite 저장 완료!")
