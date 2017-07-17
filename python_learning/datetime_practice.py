from datetime import datetime,timedelta,timezone

#获取本地时间（时区）
time_now=datetime.now()
print(time_now)
print(time_now.tzname())
#创建datetime对象，指定日期、时间等
dt=datetime(1980,3,20,20,45,45,22)
print(dt)
#将本地时间转换为时间戳
time_now_stamp=time_now.timestamp()
print(time_now_stamp)
#从时间戳生成datetime对象，默认转化为本地时区时间
print(datetime.fromtimestamp(time_now_stamp))
#从时间戳生成标准时区时间
print(datetime.utcfromtimestamp(time_now_stamp))
#从string对象生成时间
string_date=datetime.strptime('2015-3-12 12:30','%Y-%m-%d %H:%M')
print(string_date)
#将datetime对象生成string对象
date_string=datetime.strftime(string_date,'%A-%b-%d %H:%M:%S')
print(date_string)

#时间加减，要用到timedelta类
tomo_time_now=time_now+timedelta(days=1)
print(tomo_time_now)

print(datetime.utcnow().replace(tzinfo=timezone.utc))
bj_time_now=datetime.utcnow().replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=8)))
print(bj_time_now)