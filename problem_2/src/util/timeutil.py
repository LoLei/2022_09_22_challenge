from datetime import datetime, timedelta


def add_minutes_to_datetime(date_time: datetime, minutes_to_add: int) -> datetime:
    return date_time + timedelta(minutes=minutes_to_add)


# TODO: Maybe not needed
def is_before(dt1: datetime, dt2: datetime) -> bool:
    return dt1 < dt2
