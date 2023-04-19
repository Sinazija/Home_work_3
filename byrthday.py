import datetime



employee_1 = datetime.date(year = 1998, month = 6, day = 26)
employee_2 = datetime.date(year = 1997, month = 5, day = 11)
employee_3 = datetime.date(year = 2001, month = 7, day = 19)
employee_4 = datetime.date(year = 1996,  month = 9, day = 25)
employee_5 = datetime.date(year = 1996, month = 12,day = 19)
employee_6 = datetime.date(year = 1996, month = 4,day = 23)
users = [{'name': 'Dima', 'birthday': employee_1},
            {'name': 'Vlad', 'birthday': employee_2},
            {'name': 'Diana', 'birthday': employee_3},
            {'name': 'Dina', 'birthday': employee_4},
            {'name': 'Kolya', 'birthday': employee_5},
            {'name': 'Vasya', 'birthday': employee_6}]
print(users)
def get_birthdays_per_week(users):
     today = datetime.date.today()
     weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
     if today.weekday() == 0:
         # Якщо сьогодні понеділок, то додаємо дні народження зі суботи та неділі минулого тижня
         start_week = today - datetime.timedelta(days=6)
     else:
         # Якщо сьогодні не понеділок, то додаємо дні народження з поточного тижня
         start_week = today - datetime.timedelta(days=today.weekday() - 1)
         print(start_week)
     end_week = start_week + datetime.timedelta(days=6)

     print("Birthdays for the week of {} to {}".format(start_week, end_week))

     for i in range(7):
         day = start_week + datetime.timedelta(days=i)
         print(weekdays[i] + ':', end=' ')
         for user in users:
             if user['birthday'].day == day.day and user['birthday'].month == day.month:
                 if i == 0 and user['birthday'].weekday() > 4:
                     # Якщо сьогодні понеділок і день народження був на вихідному, то вітаємо у понеділок
                     print("Happy birthday {}! (Belated)".format(user['name']))
                 else:
                     print("Happy birthday {}!".format(user['name']), end=' ')
         print()


get_birthdays_per_week(users)
