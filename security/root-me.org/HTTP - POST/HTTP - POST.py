# OK
import requests

url = "http://challenge01.root-me.org/web-serveur/ch56/"

data = {"score":10000000,"generate":"Give a try!"}

res = requests.post(url,data=data)

print(res,res.text)