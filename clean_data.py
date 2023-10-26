import pandas

dataset = pandas.read_csv("parsed_files/dataset.csv")
bonus = pandas.read_csv("aws/parsed_files/bonus_dataset.csv")

bonus = bonus.drop_duplicates()
dataset = dataset.drop_duplicates()

all_ids = pandas.concat([dataset, bonus])

print(len(all_ids))

dataset.to_csv("parsed_files/cleaned_dataset.csv", index=False)
dataset.to_csv("parsed_files/cleaned_bonus.csv", index=False)
dataset.to_csv("parsed_files/all_ids.csv", index=False)
