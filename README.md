# ECON860_midterm

This is a walkthrough of how to run the shown code to answer the ECON8600 midterm question. In general, python files run on the local server are saved under the main folder, ‘midterm’, while code run on a remote server are saved in the ‘aws' folder for convenience in copying files.

**Scraping User IDs from the Charcoal Papers website**
1. run run_githubids.py on local computer to download an html with the user information. This saves a single .html file in a new folder called html_files.
2. (Optional) to obtain the bonus user IDs, run run_ids_bonus.py on an aws server to obtain many time stamped html files. Some of these will contain bonus ID information which we will parse later.

**Parsing User ID information from Charcoal Papers website**
1. run run_parse.py to parse the single .html file with the static user information. This creates a csv called ‘dataset.csv’ of the provided static user information in a new folder called ‘parsed_files'.
2. (Optional) to parse the bonus ids, run parse_aws_ids.py. This runs through all available html files and looks for the existence of bonus IDs. If found it adds this information to a dataset that will be saved as bonus_dataset.csv.

**Clean Data**
1. run clean_data.py to create a master list of github IDs. The first part of the code in this file removes duplicates and creates three separate csv datasets: ‘cleaned_dataset.csv’ which contains only the static list of ids, 2. ‘cleaned_bonus.csv’ which is a cleaned list of the bonus ids and ‘all_ids.csv’ which combines the previous two. (Note: this clean_data.py code is used multiple times, at this point only the top part of the code will run, the rest can be commented out for now).

**Requesting User Information from Github**
1. Run run_github_requests.py to obtain user information in json files. These will be saved as individual .json files in the json_files folder.
2. Also run repos_requests.py to obtain json files with data on user repositories. These will be saved in the json_files2 folder and will contain the information on the number of starred repositories.

**Parse Github information**
1. Run parse_github.py to parse the json files and pull all information except the number of starred. This creates a csv called github_user_data.csv in parsed_files folder for only the valid usernames. This will also create a separate csv file with the list of invalid usernames called invalid_id_list.csv.
2. Run parse_starred.py to parse the repository json files. This will create a csv with the number of starred repositories data for only the valid usernames. We will concat this with the previous data set later.

**Finish Cleaning Data**
We now have all data scraped. We can rerun the entirety of clean_data.py to finished cleaning our data. This will create a new complete dataset with all github information called ‘github_data.csv’ in the parsed_files folder. This will also print the number of valid, unique ids and number of invalid ids.

**Sample Statistic and Scatterplots**
1. Run summary_stats.py to return summary stastics tables for the Part 1 data and the GitHub.com data.
2. Run scatterplots.py to create scatterplots for the report.
