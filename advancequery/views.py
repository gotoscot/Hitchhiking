from django.shortcuts import render, redirect
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from datetime import date, timedelta
from django.db import connection
# Create your views here.

# class UserRanking(viewsets.ModelViewSet):
    # serializer_class = UserRankingserializers
    # renderer_classes = [JSONRenderer, TemplateHTMLRenderer]

def get_ranking(request):
    template_name = 'Ranking_table.html'
    today = date.today()
    startdate = today - timedelta(days=90)
    queryset = UserRankingmodel.objects.raw('CALL user_ranking(%s)', [startdate])
    print(queryset[0].Difficulty)
    return render(request, template_name, {'Ranking_table': queryset})

def get_recommend(request):
    sessionKey = request.session.session_key
    if sessionKey:
        template_name = 'Recommend_table.html'
        userid = request.session['userid']
        queryset = Recommendlistmodel.objects.raw('Call recommend_list(%s)', [userid])
        # print(queryset[0])
        return render(request, template_name, {'Recommend_table': queryset})
    else:
        return redirect("http://127.0.0.1:8000/user/login")

def buddy_restaurant_recommend(request):
    sessionKey = request.session.session_key
    if sessionKey:
        userid = request.session['userid']
        sql = "Call oneShotRecommend(%d)" % int(userid)
        with connection.cursor() as cursor:
            query=cursor.execute(sql)
            queryList1 = cursor.fetchall()
            cursor.nextset()
            queryList2 = cursor.fetchall()
            cursor.nextset()
            queryList3 = cursor.fetchall()

        return render(request, 'experience_table.html', {'buddies_same_plan': queryList1,'restaurant':queryList2,'buddies_same_likes':queryList3})
    else:
        return redirect("http://127.0.0.1:8000/user/login")

# class UserRecommend(viewsets.ModelViewSet):
#     userid = '10005'
#     queryset = Recommendlistmodel.objects.raw('Call recommend_list(%s)', [userid])
#     serializer_class = Recommendlistserializers


# def displayRanking(request):
#     ranktable = request.get('http://127.0.0.1:8000/advancequery/UserRankingmodel/')
#     jsonobj = ranktable.json()
#     return render(request, 'Ranking_table.html', {"Ranking_table": jsonobj})
