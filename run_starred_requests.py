import requests
import os
import pandas
import time
import datetime

if not os.path.exists("html_files2"):
	os.mkdir("html_files2")

access_point = "https://github.com"

id_list = pandas.read_csv("parsed_files/all_ids.csv")
id_list = id_list['Login ID']

headers = {
  'accept': '*/*',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53',
  'accept-language': 'en-US,en;q=0.9,it;q=0.8,es;q=0.7',
  'referer': 'https://www.google.com/'
}

for user in id_list:

	file_name = "html_files2/" + user + ".html"

	if os.path.exists(file_name):
		pass
	else:
		try:
			f = open(file_name + ".tmp", "w")

			req = requests.Session()
			response = req.get(access_point + "/" + user + "?tab=stars", headers=headers)

			html = response.text

			f.write(html)
			f.close()

			os.rename(file_name+".tmp", file_name)

		except Exception as e:
			print(e)

		time.sleep(20)

