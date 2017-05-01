
import datetime
start_date="2016-06-15"
str_date=start_date.strftime ("%Y-%m-%d %H")
print str_date
date_object = datetime.datetime.strptime(start_date, '%Y-%m-%d')
print date_object
time_now=datetime.datetime.now()
print time_now
time_compare=time_now+datetime.timedelta(days=10)
print time_compare
if time_compare>date_object and date_object>=time_now:
	print "YEs"
else:
	print "None"	

