import json
import pandas
import os
import glob
import re

if not os.path.exists("parsed_files"):
	os.mkdir("parsed_files")

dataset = pandas.DataFrame()

for json_file_name in glob.glob("json_files2/*.json"):

	f = open(json_file_name, "r")
	json_data = json.load(f)

	num_starred = len(json_data)

	row = pandas.DataFrame.from_records([{
		'ghid': json_file_name.replace("json_files2/","").replace(".json",""),
		'num_starred': num_starred
		}])

	dataset = pandas.concat([dataset,row])

print(dataset)
print(len(dataset))
dataset.to_csv("parsed_files/num_starred_data.csv", index = False)
