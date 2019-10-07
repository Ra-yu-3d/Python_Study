#2つの日付間の日数を計算

import datetime

#年月日の入力
def input_date():
    year = int(input("年を入力:"))
    month = int(input("月を入力:"))
    day = int(input("日にちを入力:"))

    date = datetime.datetime(year, month, day)
    print(date)
    return date

date1 = input_date()
date2 = input_date()

result = date2-date1
print(result)
