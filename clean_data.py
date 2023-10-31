import pandas

### Charcoal Papers data ##########################################################

dataset = pandas.read_csv("parsed_files/dataset.csv")
bonus = pandas.read_csv("parsed_files/bonus_dataset.csv")

##remove duplicates
bonus = bonus.drop_duplicates()
dataset = dataset.drop_duplicates()

all_ids = pandas.concat([dataset, bonus])

print("total number of users: ", len(all_ids))
print("number of unique static ids: ", len(dataset))
print("number of unique bonus ids: ", len(bonus))

dataset.to_csv("parsed_files/cleaned_dataset.csv", index=False)
dataset.to_csv("parsed_files/cleaned_bonus.csv", index=False)
dataset.to_csv("parsed_files/all_ids.csv", index=False)

### Github data ##################################################################

github_user_data = pandas.read_csv("parsed_files/github_user_data.csv")
starred = pandas.read_csv("parsed_files/num_starred_data.csv")
invalid_users = pandas.read_csv("parsed_files/invalid_id_list.csv")

print("number of valid github ids: ", len(github_user_data))
print("number of invalid ids: ", len(invalid_users))
print("number of starred data: ", len(starred))

## combine star data with other user data

df = pandas.merge(github_user_data, starred)
df.to_csv("parsed_files/github_data.csv", index=False)








