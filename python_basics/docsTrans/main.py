#!/usr/bin/python
# -*- coding: UTF-8 -*-
from docx import Document
import MySQLdb

def insert_mysql(dic):

    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="case100", port=3306)
    cursor = db.cursor()
    qmarks = ', '.join(['%s'] * len(dic))
    columns = ', '.join(dic.keys())
    try:
        qry = "Insert Into college (%s) Values (%s);" % (columns, qmarks)
        cursor.execute(qry, dic.values())
        db.commit()
    except Exception as e:
        print(str(e))
        db.rollback

document = Document("Top 30-100.docx")
all_paragraphs = document.paragraphs
rowInformation = {}
count = 0;
for paragraph in all_paragraphs:
    strPara = paragraph.text
    # 情况1：空行：录入 & 清空
    if strPara == "" or strPara == ' ':
        print("-" * 20)
        count = count+1
        rowInformation["collegeArea"] = "USA"
        # print(rowInformation)
        insert_mysql(rowInformation)
        print(rowInformation)
        rowInformation = {}
    # 情况2：split:的长度为2 -> 信息
    elif len(strPara.split(':', -1)) == 2:
        before = strPara.split(':', -1)[0]
        after = strPara.split(':', -1)[1]
        before = before.strip()
        after = after.lstrip()
        if after == "":
            after = "No Data"
        if before == "Acceptance rate":
            rowInformation["collegeAcceptanceRate"] = after
        if before == "Tuition":
            rowInformation["collegeTuition"] = after
        if before == "Campus size":
            rowInformation["collegeCampSize"] = after
        if before == "Men and Women ratio":
            rowInformation["collegeMenWomanRadio"] = after
        if before == "Gender ratio":
            rowInformation["collegeMenWomanRadio"] = after
        if before == "Early Decision":
            rowInformation["collegeEarlyDecision"] = after
        if before == "Early Action":
            rowInformation["collegeEarlyAction"] = after
        if before == "Regular Decision":
            rowInformation["collegeRegularDecision"] = after
        if before == "Freshman Retention rate":
            rowInformation["collegeAvgFreshmanRetention"] = after
        if before == "Student number":
            rowInformation["collegeStudentCount"] = after
        if before == "International Student number":
            rowInformation["collegeInternationalStuCount"] = after
        if before == "Student/Teacher ratio":
            rowInformation["collegeTeacherStudentRatio"] = after
    # 情况3：split:的长度为3 -> 信息
    elif len(strPara.split(':', -1)) == 3:
        before = strPara.split(':', 1)[0]
        after = strPara.split(':', 1)[1]
        before = before.strip()
        after = after.lstrip()
        if after == "":
            after = "无数据"
        if before == "Acceptance rate":
            rowInformation["collegeAcceptanceRate"] = after
        if before == "Tuition":
            rowInformation["collegeTuition"] = after
        if before == "Campus size":
            rowInformation["collegeCampSize"] = after
        if before == "Men and Women ratio":
            rowInformation["collegeMenWomanRadio"] = after
        if before == "Gender ratio":
            rowInformation["collegeMenWomanRadio"] = after
        if before == "Early Decision":
            rowInformation["collegeEarlyDecision"] = after
        if before == "Early Action":
            rowInformation["collegeEarlyAction"] = after
        if before == "Regular Decision":
            rowInformation["collegeRegularDecision"] = after
        if before == "Freshman Retention rate":
            rowInformation["collegeAvgFreshmanRetention"] = after
        if before == "Student number":
            rowInformation["collegeStudentCount"] = after
        if before == "International Student number":
            rowInformation["collegeInternationalStuCount"] = after
        if before == "Student/Teacher ratio":
            rowInformation["collegeTeacherStudentRatio"] = after
    # 情况2：split#的长度为2 -> 学校名称和排名
    elif len(strPara.split('#', -1))>1:
        before = strPara.split('#', -1)[0]
        after = strPara.split('#', -1)[1]
        before = before.strip()
        after = after.lstrip()
        if after == "":
            after = "Null"
        rowInformation["collegeName"] = before
        # rowInformation["Rank"] = after
    # 情况1：split# or split:的数组长度为1 -> 私立 or 公立
    else:
        strPara = strPara.strip()
        collegeIsPublic = strPara in "Public school"
        if collegeIsPublic:
            collegeIsPublic = "1"
        else:
            collegeIsPublic = "0"
        rowInformation["collegeIsPublic"] = collegeIsPublic

print(count)
