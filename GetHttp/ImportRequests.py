import requests
url="http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID=a78ee777a5e02651271cf5a820129f2b"
content=requests.get(url)
data=content.json()
t=data['main']['temp']
print("La témpérature est de {} degrés C".format(t-273.15))
print(content.text)