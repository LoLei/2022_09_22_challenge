from datetime import datetime, date, time

from problem_2.src.util.timeutil import add_minutes_to_datetime


def test_add_minutes_to_datetime() -> None:
    # Given
    initial_date_time = datetime.combine(date.today(), time(hour=10))
    minutes_to_add = 90

    # When
    result_date_time = add_minutes_to_datetime(initial_date_time, minutes_to_add)

    # Then
    assert result_date_time.hour == 11
    assert result_date_time.minute == 30
