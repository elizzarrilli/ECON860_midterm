import pandas
import os
import re
import glob

from bs4 import BeautifulSoup

if not os.path.exists("parsed_files"):
	os.mkdir("parsed_files")

dataset = pandas.DataFrame()

for file_name in glob.glob("html_files/*.html"):

	file = open(file_name, "r")
	soup = BeautifulSoup(file.read(), 'html.parser')
	file.close()

	check_list = soup.find_all("div",{"class":"userid2"})
	if len(check_list) > 0:
		bonus = str(soup.find("div",{"class":"userid2"})).replace(" ","").replace('">',"$").replace("</","$").replace("\n","").split("$")
		ghid = bonus[1]
		repo = "NA"
		followers = "NA"
		date = "NA"
		dataset = pandas.concat([dataset,
			pandas.DataFrame.from_records([{
				"Login ID": ghid,
				"Repo Count": repo,
				"Follower Count": followers,
				"Member Since": date
				}])
			])
	else:
		#print("no bonus IDs")
		continue


dataset.to_csv("parsed_files/bonus_dataset.csv", index=False)





