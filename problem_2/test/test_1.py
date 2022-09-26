import os
from pathlib import Path

from problem_2.src.main import (
    parse_input,
    schedule_talks_to_tracks,
    LUNCH_START,
    LUNCH_END,
    NETWORKING_START_LATEST,
    parse_and_schedule,
)
from problem_2.src.model.talk import Talk

INPUT_STRS_1 = [
    "> Writing Fast Tests Against Enterprise Rails 60min",
    "> Overdoing it in Python 45min",
    "> Lua for the Masses 30min",
    "> Ruby Errors from Mismatched Gem Versions 45min",
    "> Common Ruby Errors 45min",
    "> Rails for Python Developers lightning",
    "> Communicating Over Distance 60min",
    "> Accounting-Driven Development 45min",
    "",
    "> Woah 30min",
    "> Sit Down and Write 30min",
    "> Pair Programming vs Noise 45min",
    "> Rails Magic 60min",
    "> Ruby on Rails: Why We Should Move On 60min",
    "> Clojure Ate Scala (on my project) 45min",
    "> Programming in the Boondocks of Seattle 30min",
    "> Ruby vs. Clojure for Back-End Development 30min",
    "> Ruby on Rails Legacy App Maintenance 60min",
    "> A World Without HackerNews 30min",
    "> User Interface CSS in Rails Apps 30min",
]

INPUT_TALKS_1 = [
    Talk("Writing Fast Tests Against Enterprise Rails", 60),
    Talk("Overdoing it in Python", 45),
    Talk("Lua for the Masses", 30),
    Talk("Ruby Errors from Mismatched Gem Versions", 45),
    Talk("Common Ruby Errors", 45),
    Talk("Rails for Python Developers", 5),
    Talk("Communicating Over Distance", 60),
    Talk("Accounting-Driven Development", 45),
    Talk("Woah", 30),
    Talk("Sit Down and Write", 30),
    Talk("Pair Programming vs Noise", 45),
    Talk("Rails Magic", 60),
    Talk("Ruby on Rails: Why We Should Move On", 60),
    Talk("Clojure Ate Scala (on my project)", 45),
    Talk("Programming in the Boondocks of Seattle", 30),
    Talk("Ruby vs. Clojure for Back-End Development", 30),
    Talk("Ruby on Rails Legacy App Maintenance", 60),
    Talk("A World Without HackerNews", 30),
    Talk("User Interface CSS in Rails Apps", 30),
]


def test_input_parsing() -> None:
    # Given
    input_strs = INPUT_STRS_1

    # When
    parsed_talks = parse_input(optional_input_strs=input_strs)

    # Then
    expected_talks = INPUT_TALKS_1
    assert parsed_talks == expected_talks


def test_input_parsing_handles_wrong_input() -> None:
    # Given
    input_strs = [
        "> Talk A 60min",
        "> Talk B 60minutes",
        "> Talk C thunder",
    ]

    # When
    parsed_talks = parse_input(optional_input_strs=input_strs)

    # Then
    expected_talks = [Talk("Talk A", 60)]
    assert parsed_talks == expected_talks


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
    # TODO: More assertions


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
