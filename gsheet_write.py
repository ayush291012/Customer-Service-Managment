from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

SERVICE_ACCOUNT_FILE = 'Keys.json'

creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE,scopes=SCOPES)

SS1 = '1wkGPp_hn5jmRRwRSsTFab7IdOzbo2B8sVIDiBouHC58'
SS2 = '1HHMo8dThMlOwlOel7qrTVqllvxyd8icQ9iuX8X41xWE'

service = build('sheets', 'v4', credentials=creds)

sheet = service.spreadsheets().values()

request = sheet.get(spreadsheetId=SS2, range="Sheet3")
A1 = request.execute()
A1 = A1.get('values', [])

# for i in A1:
#     print(i)

request = sheet.clear(spreadsheetid=SS1, range="sheet3").execute()#to clear the whole sheet


# request = sheet.update(spreadsheetid=ss1, range="sheet2",valueinputoption="user_entered", body={"values":aao})
request = sheet.update(spreadsheetid=SS1, range="sheet2",valueinputoption="user_entered", body={"values":A1})
a1=request.execute()

# print('{0} cells appended.'.format(result.get('updates').get('updatedcells')))


print(a1)

