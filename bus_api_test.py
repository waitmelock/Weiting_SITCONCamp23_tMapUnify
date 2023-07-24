import requests
import json
headers={'user-agent':'Chrome/114.0.0.0'}
city=input()
#train_url = 'https://tdx.transportdata.tw/api/basic/v2/Bus/RouteFare/City/'+city+'?%24top=30&%24format=JSON'
train_url='https://tdx.transportdata.tw/api/basic/v2/Bike/Availability/City/Taichung?%24select=%22StationUID%22%3A%20%22TXG500601004%22&%24top=30&%24format=JSON'
print(train_url)
train_res = requests.get(train_url,headers=headers)
j = train_res.json()
#print(j)
with open ("bus.json","w") as f:
    json.dump(j,f)
'''
with open('result.json', 'w', encoding='utf-8') as f:
    json.dump(res, f, indent=2, sort_keys=True, ensure_ascii=False) 
print(j[0]['RouteID']['Zh_tw'])
print(j[0]['EndingStationName']['Zh_tw'])

'''