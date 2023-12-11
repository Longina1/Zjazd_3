import datetime

now = datetime.datetime.now()
print(now)
print(type(now))

date1 = now.strftime('Today is %d/%m/%Y. Time is %H:%M')
print(date1)
filename = now.strftime('Result_%H%M%S')
print(filename)

#now = str(now)
#hour = now[11:13]
#print(hour)
#minute = now[14:16]
#print(minute)
