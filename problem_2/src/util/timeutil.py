from datetime import datetime, timedelta


def add_minutes_to_datetime(date_time: datetime, minutes_to_add: int) -> datetime:
    return date_time + timedelta(minutes=minutes_to_add)
