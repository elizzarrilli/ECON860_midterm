import pandas
import numpy as np
import re
import matplotlib.pyplot as plt
import numpy as np

ghids = pandas.read_csv("parsed_files/github_data.csv")

plt.scatter(ghids.num_followers, ghids.num_following)
plt.xlabel("Number of Followers")
plt.ylabel("Number of Following")
plt.show()

plt.scatter(ghids.num_followers, ghids.num_starred)
plt.xlabel("Number of Followers")
plt.ylabel("Number of Starred Repositories")
plt.show()

plt.scatter(ghids.hireable.fillna(0), ghids.num_repos)
plt.xlabel("Hireable")
plt.ylabel("Number of Public Repositories")
plt.show()

plt.scatter(ghids.hireable.fillna(0), ghids.num_followers)
plt.xlabel("Hireable")
plt.ylabel("Number of Followers")
plt.show()

plt.scatter(ghids.start_time, ghids.num_followers)
plt.xlabel("Account Start Date")
plt.ylabel("Number of Followers")
plt.show()

plt.scatter(ghids.start_time, ghids.num_repos)
plt.xlabel("Account Start Date")
plt.ylabel("Number of Public Repositories")
plt.show()

