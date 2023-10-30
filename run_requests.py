import requests
import json
import os
import pandas
import time

if not os.path.exists("json_files"):
	os.mkdir("json_files")

access_point = "https://api.github.com"

f = open("token", "r")
token = f.read()
f.close

id_list = pandas.read_csv("parsed_files/all_ids.csv")
id_list = id_list['Login ID']

github_session = requests.Session()
github_session.auth = ("elizzarrilli", token)

response_text = github_session.get(access_point + "/rate_limit").text
print(json.loads(response_text))

user = "erinata"
file_name = "json_files/" + user + ".json"

if os.path.exists(file_name):
	pass
else:
	try:
		response_text = requests.get(access_point + "/users/" + user).text

		json_text = json.loads(response_text)

		f = open(file_name + ".tmp", "w")
		f.write(json.dumps(json_text))
		f.close()

		os.rename(file_name+".tmp", file_name)

	except Exception as e:
		print(e)

	time.sleep(60)
