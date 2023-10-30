import pandas

## Part 1 #######################################################

## No bonus IDs:
ghids = pandas.read_csv("parsed_files/cleaned_dataset.csv")

ghid_stats = ghids[['Login ID','Repo Count', 'Follower Count', 'Member Since']].describe()

print(ghid_stats)


## Part 2 #####################################################

ghids = pandas.read_csv("parsed_files/cleaned_dataset.csv")

