import requests
url="https://oc-jswebsrv.herokuapp.com/api/articles"
content=requests.get(url)
data=content.json()
# t=data['main']['temp']
print("La témpérature est de {} degrés C".format(t-273.15))