import pandas
import os
import re
import glob

from bs4 import BeautifulSoup

if not os.path.exists("parsed_files"):
	os.mkdir("parsed_files")

dataset = pandas.DataFrame()

for file_name in glob.glob("html_files2/*.html"):

	file = open(file_name, "r")
	soup = BeautifulSoup(file.read(), 'html.parser')
	file.close()

	star_list = soup.find_all("div", {"class": "d-inline-block mb-1"})

	num_starred = len(star_list)
	print(num_starred)

	row = pandas.DataFrame.from_records([{
		'Login ID': file_name.replace("html_files2/","").replace(".html",""),
		'num_starred': num_starred
		}])

	dataset = pandas.concat([dataset,row])

print(dataset)
