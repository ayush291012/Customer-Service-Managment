from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

SERVICE_ACCOUNT_FILE = 'Keys.json'

creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE,scopes=SCOPES)

SS1 = 'keysaddhere'
SS2 = 'keysaddhere'

service = build('sheets', 'v4', credentials=creds)

sheet = service.spreadsheets().values()

request = sheet.get(spreadsheetId=SS2, range="Sheet3")
A1 = request.execute()
A1 = A1.get('values', [])

for i in A1:
    print(i)


