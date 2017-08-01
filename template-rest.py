# -*- coding: UTF-8 -*-
# you may need to do:
# pip3 install requests
import requests

# check out https://httpbin.org/ for end points
# and https://resttesttest.com/ to test the endpoints
url='https://httpbin.org/post'

headers = {"Content-Type":"application/json","Accept":"application/json"}
data='{"data":"Have a nice day!"}'
response = requests.post(url,headers=headers,data=data.encode('utf-8'))

print ("code:" + str(response.status_code))
print ("headers:"+str(response.headers))
print ("data:"+str(response.text))
