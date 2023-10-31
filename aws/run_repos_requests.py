import requests
import json
import os
import pandas
import time

if not os.path.exists("json_files2"):
	os.mkdir("json_files2")

access_point = "https://api.github.com"

f = open("token", "r")
token = f.read()
f.close

id_list = pandas.read_csv("parsed_files/github_user_data.csv")
id_list = id_list['ghid']

github_session = requests.Session()
github_session.auth = ("elizzarrilli", token)

response_text = github_session.get(access_point + "/rate_limit").text
print(json.loads(response_text))

for user in id_list:

	file_name = "json_files2/" + user + ".json"

	if os.path.exists(file_name):
		pass
	else:
		try:
			#user_id = "erinata"
			response_text = github_session.get(access_point + "/users/" + user + "/starred").text

			json_text = json.loads(response_text)

			f = open(file_name + ".tmp", "w")
			f.write(json.dumps(json_text))
			f.close()

			os.rename(file_name+".tmp", file_name)

		except Exception as e:
			print(e)

		time.sleep(3)






