import datetime


employee_1 = datetime.date(year=1998, month=6, day=26)
employee_2 = datetime.date(year=1997, month=5, day=11)
employee_3 = datetime.date(year=2001, month=7, day=19)
employee_4 = datetime.date(year=1996,  month=9, day=25)
employee_5 = datetime.date(year=1996, month=12, day=19)
users = [{'name': 'Dima', 'birthday': employee_1},
         {'name': 'Vlad', 'birthday': employee_2},
         {'name': 'Diana', 'birthday': employee_3},
         {'name': 'Dina', 'birthday': employee_4},
         {'name': 'Kolya', 'birthday': employee_5}]
print(users)


def get_birthdays_per_week(users):
    today = datetime.date.today()
    weekdays = ['Monday', 'Tuesday', 'Wednesday',
                'Thursday', 'Friday', 'Saturday', 'Sunday']
    for i in range(7):
        day = today + datetime.timedelta(days=i)
        print(weekdays[i] + ':', end=' ')
        for user in users:
            if (user['birthday'].day == day.day and user['birthday'].month == day.month):
                print(user['name'], end=', ')
        print()


get_birthdays_per_week(users)
