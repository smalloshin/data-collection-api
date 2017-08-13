import requests

api_url = "http://163.13.128.41:5000/data_collection"

params = {'db':'testdb','collection':'testcollection','test1':'aaa','test2':'bbb'}

r = requests.get(api_url,params=params)
#print "1. hit:"+r.url
print r.text

