# -*- coding: UTF-8 -*-
import gspread, schedule, time
from oauth2client.service_account import ServiceAccountCredentials


def job():
    scope = ['https://spreadsheets.google.com/feeds']

    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        'key-69901d35c3db.json', scope)

    gc = gspread.authorize(credentials)

    worksheet = gc.open("Flat Financial Sheet").sheet1

    list_of_lists = worksheet.get_all_values()
    total = 0
    value = 0
    for record in list_of_lists:
        if record[4] == "FALSE":
            value = record[1]
            if record[2] == "WBQ":
                total -= float(value)
            elif record[2] == "LYC":
                total += float(value)

    payingTo = ""
    if total >= 0:
        payingTo = "LYC"
    else:
        payingTo = "WBQ"

    result_cell = worksheet.update_acell('H2', total)
    payingTo_cell = worksheet.update_acell('I2', payingTo)


if __name__ == '__main__':
    job()
    schedule.every(12).hours.do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)
