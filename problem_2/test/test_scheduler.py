import os
from pathlib import Path

from problem_2.src.scheduler import schedule_talks_to_tracks, parse_and_schedule
from problem_2.src.util.consts import LUNCH_START, LUNCH_END, NETWORKING_START_LATEST
from problem_2.test.consts import INPUT_TALKS_1


def test_no_overlap_at_lunch() -> None:
    # Given
    talks_input = INPUT_TALKS_1

    # When
    tracks = schedule_talks_to_tracks(talks_input)

    # Then
    for track in tracks:
        assert all(x.end_time <= LUNCH_START for x in track.talks_before_lunch)
        assert all(x.start_time >= LUNCH_END for x in track.talks_after_lunch)


def test_networking_start_correctly() -> None:
    # Given
    talks_input = INPUT_TALKS_1

    # When
    tracks = schedule_talks_to_tracks(talks_input)

    # Then
    assert all(
        track.talks_after_lunch[-1].end_time < NETWORKING_START_LATEST
        for track in tracks
        if track.talks_after_lunch
    )


def test_no_breaks_between_talks() -> None:
    # Given
    talks_input = INPUT_TALKS_1

    # When
    tracks = schedule_talks_to_tracks(talks_input)

    # Then
    for track in tracks:
        for i in range(len(track.talks_before_lunch) - 1):
            talk1 = track.talks_before_lunch[i]
            talk2 = track.talks_before_lunch[i + 1]
            assert talk1.end_time == talk2.start_time

        for i in range(len(track.talks_after_lunch) - 1):
            talk1 = track.talks_after_lunch[i]
            talk2 = track.talks_after_lunch[i + 1]
            assert talk1.end_time == talk2.start_time


def test_all_talks_are_scheduled() -> None:
    # Given
    talks_input = INPUT_TALKS_1

    # When
    tracks = schedule_talks_to_tracks(talks_input)

    # Then
    number_scheduled_tracks = 0
    for track in tracks:
        number_scheduled_tracks += len(track.talks_before_lunch)
        number_scheduled_tracks += len(track.talks_after_lunch)

    assert number_scheduled_tracks == len(talks_input)


def test_e2e_1() -> None:
    # Given
    path = os.path.dirname(__file__)
    input_file = Path(path).parent / "resources" / "input_1.txt"

    # When
    tracks = parse_and_schedule(input_file)

    # Then
    number_scheduled_tracks = 0
    for track in tracks:
        number_scheduled_tracks += len(track.talks_before_lunch)
        number_scheduled_tracks += len(track.talks_after_lunch)

    assert number_scheduled_tracks == 19


def test_e2e_2() -> None:
    # Given
    path = os.path.dirname(__file__)
    input_file = Path(path).parent / "resources" / "input_2.txt"

    # When
    tracks = parse_and_schedule(input_file)

    # Then
    number_scheduled_tracks = 0
    for track in tracks:
        number_scheduled_tracks += len(track.talks_before_lunch)
        number_scheduled_tracks += len(track.talks_after_lunch)

    assert number_scheduled_tracks == 26
