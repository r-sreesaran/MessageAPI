import urllib.request
import json
import ssl


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

httpsHandler = urllib.request.HTTPSHandler(context=ctx)

url ='https://api.plivo.com/v1/Account/MAODUZYTQ0Y2FMYJBLOW/Number/'
username='MAODUZYTQ0Y2FMYJBLOW'
password='Mzk0MzU1Mzc3MTc1MTEyMGU2M2RlYTIwN2UyMzk1'

password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
password_mgr.add_password(None,url,username,password)
httpBasicAuthHandler = urllib.request.HTTPBasicAuthHandler(password_mgr)

opener = urllib.request.build_opener(httpsHandler,httpBasicAuthHandler)
urllib.request.install_opener(opener)

response = urllib.request.urlopen(url)
  
jsonData = json.load(response)
objects = jsonData['objects']

numbers =[]
for i in range(0,2):
   numbers.append(objects[i]['number'])

print(numbers)