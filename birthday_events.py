from datetime import datetime, date
import pytz

YEAR = 2022
HOUR = 1
MINUTE = 1
SECOND = 1


class Birthday():
    def __init__(self, name, day, month) -> None:
        self.name = name
        self.date = date(YEAR, month, day)

example = [
    Birthday("test", 31, 1),
]
