import datetime


def date_in_future(integer):
    if isinstance(integer, int) and integer > 0:
        return (datetime.datetime.today() + datetime.timedelta(days=integer)).strftime('%d-%m-%Y %H:%M:%S')
    else:
        return datetime.datetime.today().strftime('%d-%m-%Y %H:%M:%S')


print(date_in_future([]))
print(date_in_future(2))
