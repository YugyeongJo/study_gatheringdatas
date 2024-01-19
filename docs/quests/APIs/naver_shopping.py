# 데이터명 : 네이버 open API 쇼핑
# from : https://developers.naver.com/docs/serviceapi/search/shopping/shopping.md#%EC%87%BC%ED%95%91
import requests

url = 'https://openapi.naver.com/v1/search/shop'

params = {'query':'아몬드빼빼로'}
headers = {'X-Naver-Client-Id':'sgAvYOCSCnc0Y629Lsy3'
    ,'X-Naver-Client-Secret':'iZaxHGk39l'    
}

response = requests.get(url, params=params, headers=headers)

# json 변환
import json
contents = json.loads(response.content)
pass

shop_info = {
    "lastBuildDate": contents["lastBuildDate"],
    "total": contents["total"],
    "start": contents["start"],
    "display": contents["display"]
    }
    
# mongodb 저장
from pymongo import MongoClient                          # mongodb에 접속 -> 자원에 대한 class
mongoClient = MongoClient("mongodb://localhost:27017")   # database 연결
database = mongoClient["navercom"]                     # collection 작업

# search_shop_info collection에 data 넣어주기
collection = database['search_shop_info']
collection.delete_many({})
result = collection.insert_one(shop_info)               # insert 작업 진행
id_relative = result.inserted_id
pass

# search_shop_list collection에 data 넣어주기
collection2 = database['search_shop_list']              # insert 작업 진행
collection2.delete_many({})
for i in contents['items']:                             # id 찾아주기
    i['id_relative'] = id_relative
result2 = collection2.insert_many(contents['items'])
pass