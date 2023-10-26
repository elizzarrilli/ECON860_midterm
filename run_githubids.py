import requests
import os
import pandas
import time
import datetime

if not os.path.exists("html_files"):
	os.mkdir("html_files")

access_point = "http://www.charcoalpaper.com/exams/github/user/dataset"

current_time = datetime.datetime.fromtimestamp(time.time()).strftime("%y%m%d%H%M%S")
print(current_time)

f = open("html_files/" + current_time + ".html", "w")

req = requests.Session()
response = req.get(access_point, headers = headers)

html = response.text

f.write(html)
f.close()

time.sleep(60)