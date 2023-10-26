import requests
import os
import pandas
import time
import datetime

if not os.path.exists("html_files"):
	os.mkdir("html_files")

access_point = "http://www.charcoalpaper.com/exams/github/user/dataset"

headers = {
  'accept': '*/*',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53',
  'accept-language': 'en-US,en;q=0.9,it;q=0.8,es;q=0.7',
  'referer': 'https://www.google.com/'
}

for i in range(0,100):
  current_time = datetime.datetime.fromtimestamp(time.time()).strftime("%y%m%d%H%M%S")

  f = open("html_files/" + current_time + ".html", "w")

  req = requests.Session()
  response = req.get(access_point, headers = headers)

  html = response.text

  f.write(html)
  f.close()

  time.sleep(300)