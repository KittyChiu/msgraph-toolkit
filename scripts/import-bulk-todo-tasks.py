# Description: This script reads tasks from a CSV file and imports them into Microsoft To Do using the Microsoft Graph API.
#
# Steps:
# 1. Create a CSV file with two columns: Due Date and Task.
# 2. Get the user ID, tasklist ID, and access code from the Microsoft Graph API.
# 2a. Log in to user account at https://developer.microsoft.com/en-us/graph/graph-explorer
# 2b. Get the user ID: https://graph.microsoft.com/v1.0/me
# 2c. Get the tasklist ID: https://graph.microsoft.com/v1.0/me/todo/lists
# 2d. Get the access code in the "Access Token" section of the Graph Explorer
# 3. Update the variables in the script with the user ID, tasklist ID, access code, and CSV file path.
# 4. Run the script using `python import-bulk-todo-tasks.py`

import csv
import subprocess

# Define the variables
time_zone = "Australia/Sydney"
csv_file_path = '<CSV_FILE>'
user_id = "<USER_ID>"
tasklist_id = "<TASKLIST_ID>"
access_code = "<ACCESS_CODE>"

# Open the csv file
with open(csv_file_path, 'r') as file:
	reader = csv.reader(file)
	next(reader)  # Skip the header row

	# Iterate over each row in the csv file
	for row in reader:
		task = row[1]
		due_date = row[0]

		# Create the curl command, replacing the placeholders with the actual values
		# The placeholders are {access_code}, {user_id}, {tasklist_id}, {task}, {due_date}, {time_zone}
		command = f"""curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {access_code}" -d '{{
			"title": "{task}",
			"dueDateTime": {{
				"dateTime": "{due_date}",
				"timeZone": "{time_zone}"
			}}
}}' https://graph.microsoft.com/v1.0/users/{user_id}/todo/lists/{tasklist_id}/tasks"""

		# Execute the curl command
		subprocess.run(command, shell=True)
