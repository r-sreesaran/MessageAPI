import ssl
import urllib.request

auth_id = 'MAODUZYTQ0Y2FMYJBLOW'
numbers = ['14153014785', '14153014770']
url = 'https://api.plivo.com/v1/Account/'+auth_id+'/Message/'

src = numbers[0]
dest = numbers[1]
text = 'This is a sample message'

