import urllib.request
import json
import ssl


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url ='https://api.plivo.com/v1/Account/MAODUZYTQ0Y2FMYJBLOW/Number/'
username='MAODUZYTQ0Y2FMYJBLOW'
password='Mzk0MzU1Mzc3MTc1MTEyMGU2M2RlYTIwN2UyMzk1'

password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
password_mgr.add_password(None,url,username,password)

handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
opener = urllib.request.build_opener(handler)

opener.open(url, None, 30, context=ctx)




