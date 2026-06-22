import cx_Oracle
from xml.etree.ElementTree import parse

conn = None
cur = None

tree = parse('mystudent.xml')
myroot = tree.getroot()

try:
    loginfo = 'oraman/oracle@localhost:1521/xe'
    conn = cx_Oracle.connect(loginfo, encoding='utf-8')
    print(type(conn))
    mycursor = conn.cursor()
    print(type(mycursor))
    students = myroot.findall('student')

    for oneitem in students:
        total = float(oneitem[1].text) + float(oneitem[1].text) + float(oneitem[1].text)
        average = total / 3.0

        sql = " insert into students"
        sql += " values('"
        sql += oneitem[0].text + "', '"
        sql += oneitem[1].text + "', '"
        sql += oneitem[2].text + "', '"
        sql += oneitem[3].text + "', '"
        sql += str(total) + "', '"
        sql += str(average) + "'"
        sql += " )"

        print( sql )
        mycursor.execute(sql)

    conn.commit()
except Exception as err:
    if conn != None:
        conn.rollback()
    print(err)

finally:
    if cur != None:
        cur.close()

    if conn != None:
        conn.close()

print('finished')