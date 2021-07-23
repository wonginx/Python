import requests
import  json


city = 'Gwangju'
apikey = 'a3ca1452da676b8f459587fa38a7cb47'
lang = "kr"
units = "metric"
api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang{lang}&units=metric"
result = requests.get(api)

print(result.text)

data = json.loads(result.text)

print(data["name"], "의 날씨입니다")
print("날씨는 ", data["weather"][0]["main"],"입니다.")
print("현재 온도는 ", data["main"]["temp"],"입니다")
print("하지만 체감 온도는 ", data["main"]["feels_like"],"입니다")
print("최저 기온은 ",data["main"]["temp_min"],"입니다")
print("최고 기온은 ",data["main"]["temp_max"],"입니다")
print("현재 바람의 풍속은 ",data["wind"]["speed"],"입니다")
print("현재 바람의 풍향은 ",data["wind"]["deg"],"입니다")
print("현재 습도는", data["main"]["humidity"],"입니다")
print("현재 기압은", data["main"]["pressure"],"입니다") 