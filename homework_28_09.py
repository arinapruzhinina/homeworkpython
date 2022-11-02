from datetime import date, timedelta


def captain_diary(notes, date):
    with open("diary.txt", "w") as f:
        d = timedelta(days=1)
        for i in notes:
            f.write(str(date) + ': ' + i + '\n')
            date += d


captain_diary(['Привет', 'Как дела?'], date(2022, 10, 23))
