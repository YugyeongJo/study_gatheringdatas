# from : https://developers.naver.com/docs/serviceapi/datalab/shopping/shopping.md#%EC%87%BC%ED%95%91%EC%9D%B8%EC%82%AC%EC%9D%B4%ED%8A%B8

import requests     # postman app 역할

# request API 요청
url = "https://openapi.naver.com/v1/datalab/shopping/categories"
# params = {'query':''}
headers = {'X-Naver-Client-Id':'lByKtaErmVuFdMnftwEk'
    ,'X-Naver-Client-Secret':'CVwwZ_zGiG'    
}
bodys = {
  "startDate": "2017-08-01",
  "endDate": "2017-09-30",
  "timeUnit": "month",
  "category": [
      {"name": "패션의류", "param": [ "50000000"]},
      {"name": "화장품/미용", "param": [ "50000002"]}
  ],
  "device": "pc",
  "gender": "f",
  "ages": [ "20",  "30"]
}
response = requests.post(url, headers=headers, json=bodys)

# response API 응답
response.content 

# json을 변수로 변환
import json
contents = json.loads(response.content)
pass