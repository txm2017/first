# -*- coding: utf-8 -*-  
import urllib  
import sys
#b=urllib.urlencode('E5958A')
a=urllib.quote("啊")
print a
print urllib.unquote(a)
c='E5958A'

d=[]
for x in c:
    d.append(x)
print d
t='\\%'
s=t+d[0]+d[1]+t+d[2]+d[3]+t+d[4]+d[5]
print s
print '\xE5\x95\x8A'.decode('utf-8').encode('utf-8')
print urllib.unquote(s)
print repr('啊')
print 'hello!'+repr('注销')
b=u'\u00E6\u0088\u0096\u00E6\u008C\u0089'
print b.encode('iso-8859-1').decode('utf-8')
str=u'hello'
print 'u'+repr('欢迎')
print str.encode("utf-8")
print unicode(str.encode("utf-8"), "utf-8")
print repr('hello123!@#$%^&*()_+欢迎\r\n')
print 'u'+repr('欢迎')
print u'E5A5BD'.decode('utf-8').encode("utf-8")                                                       

#print urllib.unquote(b)



