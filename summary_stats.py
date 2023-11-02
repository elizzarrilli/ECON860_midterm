import pandas
import numpy as np
import re

## Part 1 #######################################################

## No bonus IDs:
ids = pandas.read_csv("parsed_files/cleaned_dataset.csv")
ghids = pandas.read_csv("parsed_files/github_data.csv")
all_ids = pandas.read_csv("parsed_files/all_ids.csv")
charcoal_ids = ids[ids['Login ID'].str.lower().isin(ghids['ghid'].str.lower())]
#print(len(charcoal_ids))

#charcoal_id_stats = charcoal_ids[['Login ID','Repo Count', 'Follower Count', 'Member Since']].describe()
#print(charcoal_id_stats)


## Part 2 #####################################################

## make admin and hireable variables into dummies for summary stats
ghids.hireable = ghids.hireable.replace(r'^\s*$', np.nan, regex=True)
ghids['hireable'] = ghids['hireable'].fillna(0)
ghids.hireable = ghids.hireable.replace({True: 1, False:0})

ghids.admin = ghids.admin.replace(r'^\s*$', np.nan, regex=True)
ghids['admin'] = ghids['admin'].fillna(0)
ghids.admin = ghids.admin.replace({True: 1, False:0})

part2_stats_1 = ghids[['num_followers','num_following','num_starred',
'hireable','admin']].describe()
part2_stats_2 = ghids[['start_time','update_time','num_starred','num_repos']].describe()
print(part2_stats_1)
print(part2_stats_2)













