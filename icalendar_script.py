from icalendar import Calendar, Event, Alarm
from datetime import datetime, timedelta
from birthday_events import example

REPEAT_UNTIL = datetime(2040, 1, 1, 1, 1)
FREQ = "yearly"

if __name__ == "__main__":
    cal = Calendar()
    for birthday in example:
        event = Event()
        event.add('summary', birthday.name + " Geburtstag")
        event.add('dtstart', birthday.date)
        event.add('rrule', { 'FREQ': FREQ, 'UNTIL': REPEAT_UNTIL})

        alarm = Alarm()
        alarm.add('action', 'DISPLAY')
        alarm.add('trigger', timedelta(hours=7))
        event.add_component(alarm)

        cal.add_component(event)

    f = open('birthdays.ics', 'wb')
    f.write(cal.to_ical())
    f.close()
