import json
import pandas
import os
import glob

if not os.path.exists("parsed_files"):
	os.mkdir("parsed_files")

dataset = pandas.DataFrame()
invalid_users = pandas.DataFrame()

for json_file_name in glob.glob("json_files/*.json"):

	f = open(json_file_name, "r")
	json_data = json.load(f)

	if len(json_data) < 3:
		row = pandas.DataFrame.from_records([{
			'Login ID': json_file_name.replace("json_files/","").replace(".json",""),
			}])
		invalid_users = pandas.concat([invalid_users,row])

	else:
		ghid = json_data['login']
		avatar_url = json_data['avatar_url']
		url = json_data['url']
		followers = json_data['followers']
		following = json_data['following']
		starred_url = json_data['starred_url']
		full_name = json_data['name']
		company = json_data['company']
		blog = json_data['blog']
		location = json_data['location']
		email = json_data['email']
		hireable = json_data['hireable']
		bio = json_data['bio']
		start_time = json_data['created_at'].split("T")[0]
		update_time = json_data['updated_at'].split("T")[0]
		admin = json_data['site_admin']
		num_repos = json_data['public_repos']

		row = pandas.DataFrame.from_records([{
			'ghid': ghid,
			'avatar_url':avatar_url,
			'url':url,
			'num_followers': followers,
			'num_following':following,
			'full_name':full_name,
			'company':company,
			'blog':blog,
			'location':location,
			'email':email,
			'hireable':hireable,
			'bio':bio,
			'start_time':start_time.replace("-",""),
			'update_time':update_time.replace("-",""),
			'starred_url': starred_url,
			'admin': admin,
			'num_repos':num_repos
			}])

		dataset = pandas.concat([dataset,row])

print(dataset)
print(invalid_users)
dataset.to_csv("parsed_files/github_user_data.csv", index = False)
invalid_users.to_csv("parsed_files/invalid_id_list.csv", index = False)








