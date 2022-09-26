import pytest

from problem_2.src.main import (
    parse_input,
    schedule_talks,
    LUNCH_START,
    LUNCH_END,
    NETWORKING_START_LATEST,
)
from problem_2.src.model.talk import Talk


def test_input_parsing() -> None:
    # Given
    input_strs = ["> Talk One 10min", "> Talk Two lightning", "> Talk Three 25min"]

    # When
    parsed_talks = parse_input(input_strs)

    # Then
    expected_talks = [
        Talk(name="Talk One", length_minutes=10),
        Talk(name="Talk Two", length_minutes=5),
        Talk(name="Talk Three", length_minutes=25),
    ]
    assert parsed_talks == expected_talks


def test_no_overlap_at_lunch() -> None:
    # Given
    talks_unsorted = [
        Talk(name="Talk Two", length_minutes=5),
        Talk(name="Talk Three", length_minutes=25),
        Talk(name="Talk One", length_minutes=10),
    ]

    # When
    tracks = schedule_talks(talks_unsorted)

    # Then
    for track in tracks:
        assert all(x.end_time < LUNCH_START for x in track.talks_before_lunch)
        assert all(x.start_time > LUNCH_END for x in track.talks_after_lunch)


def test_networking_start_correctly() -> None:
    # Given
    talks_unsorted = [
        Talk(name="Talk Two", length_minutes=5),
        Talk(name="Talk Three", length_minutes=25),
        Talk(name="Talk One", length_minutes=10),
    ]

    # When
    tracks = schedule_talks(talks_unsorted)

    # Then
    assert all(
        track.talks_after_lunch[-1].end_time < NETWORKING_START_LATEST
        for track in tracks
    )


def test_no_breaks_between_talks() -> None:
    pass
