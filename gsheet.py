from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

SERVICE_ACCOUNT_FILE = 'Keys.json'

# creds=None
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE,scopes=SCOPES)

# If modifying these scopes, delete the file token.json.

# The ID spreadsheet.
SS1 = '1wkGPp_hn5jmRRwRSsTFab7IdOzbo2B8sVIDiBouHC58'
SS2 = '1HHMo8dThMlOwlOel7qrTVqllvxyd8icQ9iuX8X41xWE'
#Task Completion

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API

sheet = service.spreadsheets().values()
# result = sheet.get(spreadsheetId=SS1,
#         range="sheet1").execute()
# #values = result.get('values', [])

request = sheet.get(spreadsheetId=SS2, range="Sheet3")
A1 = request.execute()
A1 = A1.get('values', [])

for i in A1:
    print(i)


# request = sheet.clear(spreadsheetId=SS1, range="Sheet2").execute()#to clear the whole sheet


# request = sheet.update(spreadsheetId=SS1, range="Sheet2",valueInputOption="USER_ENTERED", body={"values":aao})
# request = sheet.update(spreadsheetId=SS1, range="Sheet2",valueInputOption="USER_ENTERED", body={"values":A1})
# A1=request.execute()

# #print('{0} cells appended.'.format(result
#                                     .get('updates')
#                                     .get('updatedCells')))


# print(A1)

