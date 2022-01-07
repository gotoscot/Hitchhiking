from django.shortcuts import render, redirect
from .models import Trailinfo
import pymysql
from django.db import connection
# Create your views here.
def search_trail(request):
    search_words = request.GET.get('search')
    sql = "select * from trailinformation where trailname like '%s' or areaname like '%s' or city like '%s' or state like '%s' or routetype like '%s' or features like '%s'" % ('%%%s%%'%search_words,'%%%s%%'%search_words,'%%%s%%'%search_words,'%%%s%%'%search_words,'%%%s%%'%search_words,'%%%s%%'%search_words)
    with connection.cursor() as cursor:
        cursor.execute(sql)
        queryList = cursor.fetchall()
    return render(request,'search_trail.html',{'trails':queryList})

def insert_schedule(request):
    sessionKey = request.session.session_key
    if sessionKey:
        trail=request.GET['trail'].split(',')
        trailid=trail[0][1:]
        print(trailid)
        scheduleDate=request.POST['schedule_date']
        userid = request.session['userid']
        if trailid is not None:
            print('trailid is not none')
            try:
                print('sql')
                sql = "insert into schedule(UserID,TrailID,Date) values ('%s','%s','%s')" % (userid, trailid,scheduleDate)
                with connection.cursor() as cursor:
                    cursor.execute(sql)
                    connection.commit()

                return to_schedule(request)
            except Exception as e:
                print(e)
                connection.rollback()
        else:
            print('not sql')
            return to_schedule(request,trail)
    else:
            return redirect("http://127.0.0.1:8000/user/login")

def to_insert_schedule(request):
    trail=request.POST['trail']
    trailname = trail.split(',')[1]
    return render(request, 'to_insert_schedule.html',{'trail':trail,'trailname':trailname})

def to_update_schedule(request,msg=''):
    org_schedule=request.GET['schedule']
    schedule=org_schedule.split(',')
    print(schedule)
    schedule[4] = str('%04d' % int(schedule[4].split('(')[1])) + '-' + str('%02d' % int(schedule[5][1:3])) + '-' + '%02d' %int(schedule[6].split(')')[0][1:3])
    schedule[7] = int(schedule[7])
    print(schedule)
    message=msg
    return render(request, 'to_update_schedule.html',{'schedule':schedule,'message':message,'org_sche':org_schedule})

def to_schedule(request):
    sessionKey = request.session.session_key
    if sessionKey:
        userid = request.session['userid']
        sql = "select s.ScheduleID,t.TrailName,t.AreaName,t.State,s.Date,s.Rating,s.Status from trailinformation as t natural join schedule as s where userid = '%s'" % userid
        with connection.cursor() as cursor:
            cursor.execute(sql)
            queryList = cursor.fetchall()
        return render(request, 'schedule.html', {'user_schedule': queryList})
    else:
        return redirect("http://127.0.0.1:8000/user/login")


#
def delete_schedule(request):
    sessionKey = request.session.session_key
    if sessionKey:
        org_schedule = request.GET['schedule'].split(',')
        print(org_schedule)
        scheduleid = org_schedule[0][1:]
        scheduleid1 = int(scheduleid)
        if scheduleid is not None:
            try:
                with connection.cursor() as cursor:
                    sql = "delete from schedule where scheduleid = %d" % scheduleid1
                    cursor.execute(sql)
                    connection.commit()
                return to_schedule(request)
            except Exception as e:
                print(e)
                connection.rollback()
        else:
            return to_schedule(request)
    else:
        return redirect("http://127.0.0.1:8000/user/login")


def update_schedule(request):
    sessionKey = request.session.session_key
    org_schedule = request.GET['schedule'].split(',')
    scheduleid = org_schedule[0][1:]
    if sessionKey:
        hikedStatus = request.POST['status']
        print(scheduleid)
        scheduledate = request.POST['schedule_date']
        trail_rate = request.POST['schedule_rate']
        trail_rate = int(trail_rate)
        print(hikedStatus, scheduleid, scheduledate, trail_rate)
        if scheduleid is not None:
            scheduleid1 = int(scheduleid)
            try:
                sql = "update schedule set status = '%s', date = '%s', rating = %d where scheduleid = %d" % (hikedStatus,scheduledate,trail_rate,scheduleid1)
                with connection.cursor() as cursor:
                    cursor.execute(sql)
                    connection.commit()
                return to_schedule(request)
            except Exception as e:
                return to_update_schedule(request,e)
        else:
            return to_schedule(request)
    else:
        return redirect("http://127.0.0.1:8000/user/login")

# def insert_likes(request):

