from datetime import date, timedelta
def captain_diary(notes, date):
    a=open("diary.txt", "w")
    b=timedelta(days=1)
    for i in notes:
        a.write(str(date)+ ': '+ i + '\n')
        date+=b 
    a.close()
captain_diary(['Привет', 'Как дела?'], date(2022, 10, 23))