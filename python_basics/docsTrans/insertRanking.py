#!/usr/bin/python
# -*- coding: UTF-8 -*-
from docx import Document
import MySQLdb
rowInformation = []
def rank():
    document = Document("Top 30-100.docx")
    all_paragraphs = document.paragraphs
    for paragraph in all_paragraphs:
        strPara = paragraph.text
        if len(strPara.split('#', -1)) > 1:
            after = strPara.split('#', -1)[1]
            rowInformation.append(after)



def insert_mysql(dic):

    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="case100", port=3306)
    cursor = db.cursor()
    qmarks = ', '.join(['%s'] * len(dic))
    columns = ', '.join(dic.keys())
    try:
        qry = "Insert Into collegeranking (%s) Values (%s);" % (columns, qmarks)
        cursor.execute(qry, dic.values())
        db.commit()
    except Exception as e:
        print(str(e))
        db.rollback

dic={}
rank()
for i in range(109, 178, 1):
    dic["collegeId"] = str(i)
    dic["rankingYear"] = "2020"
    dic["rankingUsNewsLocal"] = rowInformation[i-109]
    dic["rankingUsNewsWorld"] = rowInformation[i - 178]
    insert_mysql(dic)
    print(dic)
    print('-'*20)


