# OK
import requests

url = "http://challenge01.root-me.org/web-serveur/ch5/"


res = requests.get(url=url)

headers = res.headers

for header in headers:

    print(f" {header}       {headers[header]}")


add_header = {"Header-RootMe-Admin":"true"}

response = requests.get(url=url, headers=add_header)

print(response.text)