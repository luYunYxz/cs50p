import requests
import sys
import json


if len(sys.argv) != 2:
    sys.exit("参数不能为空")

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])

o = response.json()

for result in o["results"]:
   print(result["trackName"])
