# coding = utf-8

import sys
from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，文字匹配
import urllib.request  # 指定url，获取网页数据
import urllib.response
import xlwt  # 进行Excel操作
import _sqlite3  # 进行SQLite数据库操作
import MySQLdb
import sys, io
import time
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')


def main():
    baseurl = "https://www.niche.com/colleges/"
    baseurl2 = "https://www.niche.com/graduate-schools/"
    # print(askURL(baseurl+"university-of-wisconsin"))
    # print(nicheSpider(baseurl+"university-of-wisconsin","https://www.niche.com/graduate-schools/university-of-wisconsin/"))
    nameList = findCollegeNameList()
    theName = nameList[2][0]
    theName = theName.replace(' ', '-')
    theName = theName.replace('--', '---')
    print(nicheSpider(baseurl + theName, baseurl2 + theName))
    for name in nameList:
        theName = name[0]
        theName = theName.replace(' ', '-')
        theName = theName.replace('--', '---')
        # print(nicheSpider(baseurl+theName, baseurl2+theName))
        # time.sleep(30 * 1)

# College Name
findCollegeName = re.compile(r'<h1 class="postcard__title">(.*?)</h1>')  # 创建正则表达式对象，表示规则（字符串的模式）
# College General Position
findCollegeGeneralPosition = re.compile(r'<li class="postcard__attr postcard-fact">(.*?)</li>')  # 创建正则表达式对象，表示规则（字符串的模式）
# College Information, Intro
findCollegeInfo = re.compile(r'<span class="bare-value">(.*?)</span>')  # 创建正则表达式对象，表示规则（字符串的模式）
# College Niche Grade (Overall)
findCollegeNicheGradeOverall = re.compile(r'<div class="niche__grade niche__grade--a-plus">(.*?)</div>')  # 创建正则表达式对象，表示规则（字符串的模式）
# College Website
findCollegeWeb = re.compile(r'<a class="profile__website__link" href="(.*?)" rel="nofollow noopener" target="_blank">')  # 创建正则表达式对象，表示规则（字符串的模式）
# College Specific Location
findCollegeSpecificLocation = re.compile(r'<address class="profile__address--compact">(.*?)</address>')  # 创建正则表达式对象，表示规则（字符串的模式）
# College Acceptance Rate
findCollegeAcceptanceRate = re.compile(r'<div class="scalar__value"><span>(\d*)%</span></div>')  # 创建正则表达式对象，表示规则（字符串的模式）
# College Student Amount
findCollegeStudentAmount = re.compile(r'<div class="scalar__value"><span>(.*?)</span>')  # 创建正则表达式对象，表示规则（字符串的模式）
# College After Graduation Income
findCollegeGraduationIncome = re.compile(r'<div class="scalar__value"><span>(.*?)</span><span class="scalar__value__suffix">/ year</span><div class="scalar__national__value"><div class="scalar__national__label">National</div>')
# College Normal Image
findCollegeImg = re.compile(r'background-image: url(.*?), url')
# College Map Image
findCollegeMapImg = re.compile(r'background-image: url(.*?), url')


def findCollegeNameList():
    db = MySQLdb.connect(host="localhost", user="root", passwd="root", db="case100", port=3306, charset="utf8")
    cursor = db.cursor()
    returnList = []
    try:
        qry = "select collegeName from college"
        cursor.execute(qry)
        results = cursor.fetchall()
        for row in results:
            returnList.append(row)
        return returnList
    except Exception as e:
        print(str(e))
        db.rollback


def download_img(img_url, api_token, img_name, download_path):
    header = {"Authorization": "Bearer " + api_token} # 设置http header
    request = urllib.request.Request(img_url, headers=header)
    try:
        response = urllib.request.urlopen(request)
        filename = download_path+img_name
        if (response.getcode() == 200):
            with open(filename, "wb") as f:
                f.write(response.read()) # 将内容写入图片
            return filename
    except:
        return "failed"



def nicheSpider(url1, url2):
    html1 = askURL(url1)
    html2 = askURL(url2)
    soup1 = BeautifulSoup(html1, "html.parser")
    soup2 = BeautifulSoup(html2, "html.parser")
    for item in soup1.find_all('div', class_="platform__wrapper"):
        data = []
        item = str(item)
        college_name = re.findall(findCollegeName, item)[0]  # re库用正则表达式来查找指定字符串
        college_generalposition = re.findall(findCollegeGeneralPosition, item)[0]  # re库用正则表达式来查找指定字符串
        college_information = re.findall(findCollegeInfo, item)[0]  # re库用正则表达式来查找指定字符串
        college_nichegrade = re.findall(findCollegeNicheGradeOverall, item)[0]  # re库用正则表达式来查找指定字符串
        college_web = re.findall(findCollegeWeb, item)[0]  # re库用正则表达式来查找指定字符串
        college_specificposition = re.findall(findCollegeSpecificLocation, item)[0]  # re库用正则表达式来查找指定字符串
        college_acceptancerate = re.findall(findCollegeAcceptanceRate, item)[0]  # re库用正则表达式来查找指定字符串
        college_studentamount = re.findall(findCollegeStudentAmount, item)[20]  # re库用正则表达式来查找指定字符串
        college_graduationincome = re.findall(findCollegeStudentAmount, item)[25]  # re库用正则表达式来查找指定字符串
        college_normalimg = re.findall(findCollegeImg, item)[1]  # re库用正则表达式来查找指定字符串
        item2 = str(soup2.find_all('div', class_="platform__wrapper"))
        college_mapimg = re.findall(findCollegeMapImg, item2)[1]

        data.append(college_name)
        data.append(college_generalposition)
        data.append(college_information)
        data.append(college_nichegrade)
        data.append(college_web)
        data.append(college_specificposition)
        data.append(college_acceptancerate+"%")
        data.append(college_studentamount)
        data.append(college_graduationincome)
        data.append(college_normalimg)
        data.append(college_mapimg)
        return data


# 得到制定URL的网页内容
def askURL(url):
    head = {  # tell server what we are able to receive
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 86.0.4240.193 Safari / 537.36"
        # User Agent is a camouflage to tell the server that we are actually human

    }
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
    except urllib.error.URLError as result:
        print(result)
    return html


if __name__ == "__main__":
    main()
