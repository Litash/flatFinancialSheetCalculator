# -*- coding: UTF-8 -*-
import gspread, requests, schedule, time, datetime
from oauth2client.service_account import ServiceAccountCredentials
from bs4 import BeautifulSoup

def job():
    scope = ['https://spreadsheets.google.com/feeds']

    credentials = ServiceAccountCredentials.from_json_keyfile_name('tvReminder-9c2fc76b87b6.json', scope)

    gc = gspread.authorize(credentials)

    worksheet = gc.open("Flat Financial Sheet").sheet1

    dlurl_cells = worksheet.range('E2:E62')
    note_cells = worksheet.range('F2:F62')
    update_cells = worksheet.range('G2:G62')

    isUpdate = 0

    # Update in batch
    if isUpdate==1 :
        worksheet.update_cells(note_cells)
        worksheet.update_cells(update_cells)

if __name__ == '__main__':
    job()
    schedule.every(1).days.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)