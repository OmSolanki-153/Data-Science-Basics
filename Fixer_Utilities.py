import string
import datetime as dt
print('#1 Removing spaces from a data entry');
baddata = " too many spaces is bad! "
print('>',baddata,'<')
cleandata=baddata.strip()
print('cleandata',cleandata)
print('\n #2 Removing nonprintable characters')
#printable = set(string.printable)
baddata = "Data\x00 Science with \x02 funny characters is \x03 bad!!!"
cleandata=''.join(filter(lambda x: x in string.printable,baddata))
print('Bad Data : ',baddata);
print('Clean Data : ',cleandata)
print('\n # 3 Reformatting data entry to match specific formatting criteria.')
baddate = dt.date(2019, 10, 31)
baddata=format(baddate,'%Y-%m-%d')
gooddate = dt.datetime.strptime(baddata,'%Y-%m-%d')
gooddata=format(gooddate,'%d %B %Y')
print('Bad Data : ',baddata)
print('Good Data : ',gooddata)
#comments:
#strip() removes whitespaces, filter() used for iteration
#strptime() converts time into string format
