from datetime import datetime, date, time

from problem_2.src.util.timeutil import add_minutes_to_datetime, is_before


def test_add_minutes_to_datetime() -> None:
    # Given
    initial_date_time = datetime.combine(date.today(), time(hour=10))
    minutes_to_add = 90

    # When
    result_date_time = add_minutes_to_datetime(initial_date_time, minutes_to_add)

    # Then
    assert result_date_time.hour == 11
    assert result_date_time.minute == 30


def test_is_before_1() -> None:
    # Given
    dt1 = datetime.combine(date.today(), time(hour=10))
    dt2 = datetime.combine(date.today(), time(hour=11))

    # When
    result = is_before(dt1, dt2)

    # Then
    assert result


def test_is_before_2() -> None:
    # Given
    dt1 = datetime.combine(date.today(), time(hour=11))
    dt2 = datetime.combine(date.today(), time(hour=10))

    # When
    result = is_before(dt1, dt2)

    # Then
    assert result is False


def test_is_before_3() -> None:
    # Given
    dt1 = datetime.combine(date.today(), time(hour=10))
    dt2 = datetime.combine(date.today(), time(hour=10))

    # When
    result = is_before(dt1, dt2)

    # Then
    assert result is False
