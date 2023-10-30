import json
import pandas
import os
import glob

if not os.path.exists("parsed_files"):
	os.mkdir("parsed_files")

dataset = pandas.DataFrame()
invalid_users = pandas.DataFrame()

for json_file_name in glob.glob("json_files/*.json")[0:3]:
	f = open(json_file_name, "r")
	json_data = json.load(f)
	print(len(json_data))