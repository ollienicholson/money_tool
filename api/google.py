# == ChatGPT instructions for connecting Python script with Google API ==

# Python can be used to interact with Google Sheets through the Google Sheets API. Here are the general steps to get started:

# Enable the Google Sheets API and obtain credentials:
# To use the Google Sheets API, you need to enable it in the Google Cloud Console and obtain credentials (client ID and secret) that allow your Python script to access the API.

# Install the required libraries: You need to install the google-auth and google-api-python-client libraries in your Python environment.

# (Ollie): imported google-auth to conda -> base
# (Ollie): imported google-api-python-client to conda -> base
# see https://www.google.com/search?q=python+google+sheets&oq=python+google+sheets&aqs=chrome..69i57j0i512l9.37153j0j7&sourceid=chrome&ie=UTF-8 for reference

# Authenticate: You need to authenticate your Python script using the credentials you obtained in step 1. This can be done using the google-auth library.

# Access the spreadsheet: You can access a Google Sheets spreadsheet using the google-api-python-client library. You need to specify the ID of the spreadsheet you want to access, which can be found in the URL of the spreadsheet.

# Perform operations on the spreadsheet: Once you have access to the spreadsheet, you can perform various operations on it, such as reading and writing data, formatting cells, and creating new sheets.

# Here is a sample code that demonstrates how to read data from a Google Sheets spreadsheet:

# from google.oauth2 import service_account
# from googleapiclient.discovery import build

# # Authenticate using credentials
# creds = service_account.Credentials.from_service_account_file('path/to/credentials.json')
# service = build('sheets', 'v4', credentials=creds)

# # Access the spreadsheet
# spreadsheet_id = 'your_spreadsheet_id_here'
# range_name = 'Sheet1!A1:B2'
# result = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()

# # Print the data
# values = result.get('values', [])
# if not values:
#     print('No data found.')
# else:
#     for row in values:
#         print(row)
#
# In this code, credentials.json is the file containing your API credentials, spreadsheet_id is the ID of the spreadsheet you want to access, and range_name is the range of cells you want to read (in this case, cells A1 to B2 on the first sheet).
# The result variable contains the data that was read from the spreadsheet, which is then printed to the console.
