import urllib.request
import json
import ssl

class client:

    def __init__(self,userName,password):
        self.userName=userName
        self.password=password

# importing a ssl certificate      
      ctx = ssl.create_default_context()
      ctx.check_hostname = False
      ctx.verify_mode = ssl.CERT_NONE

# creating ssl handler

      httpsHandler = urllib.request.HTTPSHandler(context=ctx)

# creating basicauth handler

     password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
     password_mgr.add_password(None,url,self.userName,self.password)
     httpBasicAuthHandler = urllib.request.HTTPBasicAuthHandler(password_mgr)
