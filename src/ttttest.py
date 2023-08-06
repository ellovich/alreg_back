from datetime import datetime


def fix_date(date):
    if date and not isinstance(date, datetime):
        try:
            return datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            return datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ")
        

print(fix_date('2023-08-06T13:30:12.000Z'))
print(fix_date('2001-01-01'))