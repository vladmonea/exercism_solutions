import datetime


WEEKDAYS = {
    'Monday': 1,
    'Tuesday': 2,
    'Wednesday': 3,
    'Thursday': 4,
    'Friday': 5,
    'Saturday': 6,
    'Sunday': 7
}


class MeetupDayException(Exception):
    pass


def resolve_current_date(year, month, day):
    try:
        return datetime.date(year, month, day)
    except ValueError:
        pass


def meetup(year, month, week, day_of_week):
    if week == "teenth":
        for i in range(13, 20):
            cd = datetime.date(year, month, i)
            wd = datetime.date.isoweekday(cd)
            if wd == WEEKDAYS[day_of_week]:
                return cd
    else:
        day_of_week = WEEKDAYS[day_of_week]
        if week != "last":
            week = int(week[:1])
        counter = 0
        for i in range(1, 32):
            cd = resolve_current_date(year, month, i)
            if cd:
                wd = datetime.date.isoweekday(cd)
                if wd == day_of_week:
                    found = cd
                    counter += 1
                    if counter == week:
                        return found
        return found

