from urllib import request
req=request.Request('http://fanyi.baidu.com/')
res=request.urlopen(req)
html=res.read().decode('utf-8')
# print(html) get it's information

req=request.Request('http://meiju.com/')
res=request.urlopen(req)
print('State:',res.status,res.reason)
for i1,i2 in res.getheaders():
    print('%s:%s'%(i1,i2))
print(res.getheaders())# Obviously, headers are stored
                       #in the form of tuple-list
print(res.info())
print(res.getcode)

req=request.Request('http://www.csdn.net/')
req.add_header('User-Agent','Mozilla/5.0 (Linux; U; Android 2.2.1; zh-cn; HTC_Wildfire_A3333 Build/FRG83D) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1')
res=request.urlopen(req)
html=res.read().decode('utf-8')
print(html)
