# 데이터명 : 조달청_나라장터 공공데이터개방표준서비스
# from : https://www.data.go.kr/iim/api/selectAPIAcountView.do
import requests

url = 'http://apis.data.go.kr/1230000/PubDataOpnStdService/getDataSetOpnStdBidPblancInfo'

params = {'serviceKey': 'kv5KjSGpridc7Ai+QIqvr+8jzmgkmfQeM5XqJO8xL1Gvknk7KLsDU4lwEaZpY0taxMMY5QKaZGq3QUopmUOYVg=='
          , 'pageNo': 1
          , 'numOfRows' : 10
          , 'type' : 'json'
          , 'bidNtceBgnDt' : 201712010000
          , 'bidNtceEndDt' : 201712312359
          }

response = requests.get(url, params=params)

print(response.content)

import json
contents = json.loads(response.content)
pass

# mongodb 저장
from pymongo import MongoClient                          # mongodb에 접속 -> 자원에 대한 class
mongoClient = MongoClient("mongodb://localhost:27017")   # database 연결
database = mongoClient["data_go_kr"]                     # collection 작업
collection = database['PubDataOpnStdService']                          # insert 작업 진행
result = collection.insert_many(contents['response']['body']['items'])
                       
pass