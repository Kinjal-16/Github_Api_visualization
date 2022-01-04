# Github_Api_visualization
This repository contains python code for data extraction from the github API and visualization using python libraries.
There are three python scripts in this repository for data extraction-repos.py, Script1.py and Script2.py. 
repos.py extracts the repositories of an organization chosen by the user.
Script1.py extracts the branches in these repositories and counts the number of branches in each of them.
Script2.py extracts the pull requests made to each repository to calculate the pull request size.

All these data are stored in mongoDB which must be running in the background on docker(Execute the run-db.sh file to run the database).
There are 4 python scripts for visualization using python libraries like Matplotlib and pandas that utilizes this data stored in the database.

You can run all these scripts at once by executing the run.sh file.
When the run.sh file has finished running, a python web server will host a website that displays these visualizations.

[Please note that the config.py file has to be provided with a GitHub username and a GitHub access token to run the Scripts successfully]

