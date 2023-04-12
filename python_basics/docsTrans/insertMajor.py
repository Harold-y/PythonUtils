
from docx import Document
import MySQLdb

def insert_mysql(major_name):

    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="case100", port=3306, charset="utf8")
    cursor = db.cursor()

    try:
        qry = "Insert Into major (majorId, majorName, majorAlpha) Values (null, '%s', null);" % major_name
        cursor.execute(qry)
        db.commit()
    except Exception as e:
        print(str(e))
        db.rollback


document = Document("majors.docx")
all_paragraphs = document.paragraphs


for paragraph in all_paragraphs:
    # insert_mysql(paragraph.text)
    # print(type(paragraph.text))
    print('<option value="'+paragraph.text+'">'+paragraph.text+"</option>")
