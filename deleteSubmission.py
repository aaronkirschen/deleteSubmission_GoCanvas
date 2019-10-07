import requests

url = "https://www.gocanvas.com/apiv2/delete_submissions" # Delete Submission API URL
username = "<username>" # GoCanvas username
password = "<password>" # GoCanvas password
apiKey = "<API Key>" # GoCanvas API Key

# Set headers used in POST request
headers={
    "Authorization":apiKey, # GoCanvas API Key
}

# Set parameters used in POST request
params={
    "username":username,
    "password":password,
}

# Define a XML payload containing the Submission IDs to delete
data="""
<?xml version="1.0" encoding="utf-8"?>
<Submissions>
<Submission Id="7346" />
<Submission Id="2999" />
<Submission Id="1989" />
</Submissions>
"""

# Submit POST request
r = requests.post(url, params=params, headers=headers, data=data)

# Print result
print(r.text)
