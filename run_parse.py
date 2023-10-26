import pandas
import os
import re
import time

from bs4 import BeautifulSoup

if not os.path.exists("parsed_files"):
	os.mkdir("parsed_files")

dataset = pandas.DataFrame()

file_name = "html_files/231025215350.html"

file = open(file_name, "r")
soup = BeautifulSoup(file.read(), 'html.parser')
file.close()

#text = soup.get_text()
#print(text)

user_list = soup.find_all("div", {"class": "grid grid-cols-4 gap-4"})
#print(user_list)

for user in user_list:
	a_list = str(user.find_all("span")).split()
	ghid = a_list[1]
	b_list = str(user.find_all("div", {"class": "repocount"})).replace(">","<").split("<")
	repo = b_list[2]
	c_list = str(user.find_all("div", {"class": "followercount"})).replace("<b>*","").replace(">","<").replace(" ","").split("<")
	followers = c_list[2]
	d_list = str(user.find_all("div", {"class": "membersince"})).replace("(","$").replace(")","$").replace(" ","").split("$")
	date = d_list[1]


	dataset = pandas.concat([dataset,
		pandas.DataFrame.from_records([{
			"Login ID": ghid,
			"Repo Count": repo,
			"Follower Count": followers,
			}])
		])

#print(dataset)
dataset.to_csv("parsed_files/dataset.csv", index=False)












