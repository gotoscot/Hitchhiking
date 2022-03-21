from django.shortcuts import render, redirect
from django.db import connection
# Create your views here.

def to_like(request):
    sessionKey = request.session.session_key
    if sessionKey:
        userid = request.session['userid']
        sql = "select f.FeatureName, l.Score, l.LikeID from Feature as f natural join Likes as l where UserID = '%s' order by f.FeatureName" % userid
        with connection.cursor() as cursor:
            cursor.execute(sql)
            queryList = cursor.fetchall()
            # print(queryList[0], queryList[1])
        return render(request, 'like.html', {'user_like': queryList})
    else:
        return redirect("http://127.0.0.1:8000/user/login")

def update_like(request):
    sessionKey = request.session.session_key
    if sessionKey:
        like_rate = request.POST['like_rate']
        feature = request.POST['feature']
        # print(feature,like_rate)
        if feature == 99:
            return to_like(request)
        userid = request.session['userid']
        # print(userid)
        sql = "select LikeID from Likes where UserID = '%s' AND FeatureID = '%s'" % (userid, feature)
        with connection.cursor() as cursor:
            cursor.execute(sql)
            queryList = cursor.fetchall()
            print(queryList)
        if not queryList:
            # print('likeid is none')
            try:
                # print('sql')
                sql = "insert into Likes(UserID,FeatureID,Score) values ('%s','%s','%s')" % (userid, feature,like_rate)
                with connection.cursor() as cursor:
                    cursor.execute(sql)
                    connection.commit()
                return to_like(request)
            except Exception as e:
                print(e)
                connection.rollback()
        else:
            likeid = queryList[0][0]
            # print(likeid)
            # print('likeid already exist')
            try:
                # print('sql_update')
                sql = "update Likes set Score = '%s' where LikeID = %s" % (like_rate, likeid)
                with connection.cursor() as cursor:
                    cursor.execute(sql)
                    connection.commit()
                return to_like(request)
            except Exception as e:
#                 print(e)
                connection.rollback()
        return to_like(request)
    else:
        return redirect("http://127.0.0.1:8000/user/login")

def delete_like(request):
    sessionKey = request.session.session_key
    if sessionKey:
        org_like = request.GET['like'].split(',')
        likeid = org_like[2][1:-1]
        # print(likeid)
        if likeid is not None:
            try:
                with connection.cursor() as cursor:
                    sql = "delete from Likes where LikeID = %s" % likeid
                    cursor.execute(sql)
                    connection.commit()
                return to_like(request)
            except Exception as e:
                print(e)
                connection.rollback()
        else:
            return to_like(request)
    else:
        return redirect("http://127.0.0.1:8000/user/login")
