from poly import *

"""For when pip wants to check the date or time.
"""

import datetime


def today_is_later_than(year: int, month: int, day: int) -> bool:
    today = datetime.date.today()
    given = datetime.date(year, month, day)

    return today > given


res = worker(Request(json.loads(sys.stdin.read())))
print(res.to_json())
