import pymysql
import sys,io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')


def select_all():
    db = pymysql.connect(host="localhost", user="root", passwd="root", db="case100", port=3306, charset="utf8")
    cursor = db.cursor()
    try:
        cursor.execute('SELECT * FROM casedata')
        res = cursor.fetchall()
        for line in res:
            # print(line[1])
            if line[1][0:7] == 'SAT1470':
                print(line)
        cursor.close()
        db.close()
    except Exception as e:
        print(str(e))
        db.rollback


if __name__ == '__main__':
    select_all()
