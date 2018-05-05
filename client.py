import urllib.request
import json
import ssl

class clientFactory:

    def __init__(self,userName,password):
        self.userName=userName
        self.password=password
 
    def handlerIntializer(): 
# importing a ssl certificate      
       ctx = ssl.create_default_context()
       ctx.check_hostname = False
       ctx.verify_mode = ssl.CERT_NONE

# creating ssl handler

       httpsHandler = urllib.request.HTTPSHandler(context=ctx)

# creating basicauth handler

       password_mgr = urllib.request.HTTPPasswordMgr()
       password_mgr.add_password(self.userName,self.password)
       httpBasicAuthHandler = urllib.request.HTTPBasicAuthHandler(password_mgr)
      
       opener = urllib.request.build_opener(httpsHandler,httpBasicAuthHandler)
       urllib.request.install_opener(opener)

      
