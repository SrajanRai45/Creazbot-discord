import gspread
import os
from google.oauth2.service_account import Credentials

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
client = gspread.authorize(creds)

sheet_id = "1JjnjdQopmQ1ewj52EA0cmrzu9-f4JfzDOBwOt50elIM"
workbook = client.open_by_key(sheet_id)

sheets = workbook.worksheet("Sheet1")
def getval(k):
    key_k = k
    try:
        cell = sheets.find(key_k)
        value = sheets.cell(cell.row,2).value
        if value :
            return value
        else:
            return "doesnt exists"
    except Exception as e:
        return f"An error occurred: {e}"
    return "error occured while retrieving"