import pymysql
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def show(request):
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='opensesane', db='cs411', charset='utf8')
    cursor = conn.cursor()
    sql = "select * from trailinformation"
    effect_row = cursor.execute(sql)
    queryList = cursor.fetchall()
    queryList1=queryList[:10]
    cursor.close()
    conn.close()
    return render(request, 'index.html', {'trails': queryList1})