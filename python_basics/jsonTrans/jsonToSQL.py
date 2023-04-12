#!/usr/bin/python
# -*- coding: UTF-8 -*-
import json
import pymysql
#import MySQLdb
import sys,io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')




def insert_mysql(dic):

    db = pymysql.connect(host="localhost", user="root", passwd="root", db="case100", port=3306, charset="utf8")
    cursor = db.cursor()
    qmarks = ', '.join(['%s'] * len(dic))
    columns = ', '.join(dic.keys())
    try:
        qry = "Insert Into casedata (%s) Values (%s);" % (columns, qmarks.encode("utf-8"))
        cursor.execute(qry, dic.values())
        db.commit()
    except Exception as e:
        print(str(e))
        db.rollback


def insert_mysql2(dic):
    db = pymysql.connect(host="localhost", user="root", passwd="root", db="case100", port=3306, charset="utf8")
    cursor = db.cursor()
    try:
        qry = "Insert Into casedata_shadow (answer, SAT, TOEFL, IELTS, ACT) values ('%s','%s','%s','%s','%s');" % (
             dic['answer'], dic['SAT'],
            dic['TOEFL'], dic['IELTS'], dic["ACT"])
        qry2 = "Insert Into casedata_shadow (answer, SAT, TOEFL, IELTS, ACT) values (%s,%s,%s,%s,%s)"
        rows = cursor.execute(qry2, (dic['answer'], dic['SAT'], dic['TOEFL'], dic['IELTS'], dic["ACT"]))
        # print(rows)
        # cursor.execute(qry)
        db.commit()
        cursor.close()
        db.close()
    except Exception as e:
        print(str(e))
        db.rollback


def insert_json():
    with open('F:\Programming\case100\Spider\\test.json', encoding='utf-8') as f:
        data = json.load(f)

        '''
        # insert_mysql(data["2017A.csv"]["1"])
        for i in range(1, 304):
            try:
                answerId = i
                dic = data["2017A.csv"][str(i)]
                dic["answerId"] = i
                # print(dic['answer'].encode("utf-8").decode())
                # print(dic)
                insert_mysql2(dic)
            except Exception as result:
                print(result)
        '''

        #'''
        for i in range(1, 634):
            try:
                answerId = i
                dic = data["2020B.csv"][str(i)]
                dic["answerId"] = i
                dic["ACT"] = 'FALSE'
                insert_mysql2(dic)
            except Exception as result:
                print(result)
        #'''

        '''
        insert_mysql(data["2019A.csv"]["1"])
        for i in range(1, 1033):
            try:
                # answerId = i
                dic = data["2019A.csv"][str(i)]
                # dic["answerId"] = i
                # print(dic['answer'].encode("utf-8").decode())
                insert_mysql2(dic)
                # print(dic)
            except Exception as result:
                print(result)
        '''

if __name__ == '__main__':
    insert_json()

