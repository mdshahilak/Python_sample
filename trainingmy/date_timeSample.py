import datetime
now=datetime.datetime.now()
print(now.strftime("%d/%m/%Y"))
print(datetime.date.today().month)
x=datetime.datetime(2020,4,12)
y=datetime.datetime(year=2012,day=4,month=12)
diff=x-y
print(diff)
print(x)
end=datetime.datetime.now()

dif=end-now
print(dif)
