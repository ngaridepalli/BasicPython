import urllib
import json
import httplib
import requests


serviceurl = 'https://stg-elasticsearch.ticketing.encore.rackspace.com/lefty/ticket/_search/'
url='https://core-1215.dev.core.rackspace.com//ctkapi/login/fmwcoreuser'

# data ={
#     "query": {
#         "query_string" : {
#             "query": "account_id:10237484 AND NOT(status:Closed OR status:Solved) AND category_id:2 AND sub_category_id:ord-0001068"
#                           }
#             }
# }

data ={"password":"ar@njy8JVWP#xS"}
# req= requests.request('GET',serviceurl)
r = requests.post("https://core-1215.dev.core.rackspace.com//ctkapi/login/fmwcoreuser",data=data,json)
k=requests.post
print r




# uh = urllib.urlopen(url);
# data = uh.read()

print req