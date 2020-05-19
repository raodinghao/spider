#获取天气列表
# import pandas as pd
# import  requests
# import time
# import json
# df = pd.read_csv('china-city-list.csv')
#
# for item in df['City_ID']:
#     url = 'https://free-api.heweather.net/s6/weather/now?location=' +item+ '&key=16c37de562ea4530a9f0aa6671376ca9'
#     strhtml = requests.get(url)
#     strhtml.encoding = 'utf8'
#     time.sleep(1)
#     print( strhtml.text)
#


# #将数据写入mongo中
# import requests
# import pymongo
# import pandas as pd
# client = pymongo.MongoClient('localhost', 27017)
# book_weather = client['weather']
# sheet_weather = book_weather['sheet_weather_3']
# df = pd.read_csv('china-city-list.csv')
# for item in df['City_ID']:
#     url = 'https://free-api.heweather.net/s6/weather/now?location=' +item+ '&key=e62719afde314cb9a130fc7cdbd7c324'
#     strhtml = requests.get(url)
#     strhtml.encoding = 'utf8'
#     dic = strhtml.json()
#     sheet_weather.insert_one(dic)


#数据库查询
import pymongo
client = pymongo.MongoClient('localhost', 27017)
book_weather = client['weather']
sheet_weather = book_weather['sheet_weather_3']
# for item in sheet_weather.find({'HeWeather6.basic.admin_area':"北京"}):
#     print(item)
# print("-------------------------------------")
for item in sheet_weather.find():
    print(item)
    #print(item['HeWeather6'][0]['now']['tmp'])

