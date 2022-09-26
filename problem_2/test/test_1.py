from problem_2.src.main import (
    parse_input,
    schedule_talks,
    LUNCH_START,
    LUNCH_END,
    NETWORKING_START_LATEST,
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
    parsed_talks = parse_input(input_strs)

    # Then
    expected_talks = INPUT_TALKS_1
    assert parsed_talks == expected_talks


def test_no_overlap_at_lunch() -> None:
    # Given
    talks_input = [
        Talk(name="Talk Two", length_minutes=5),
        Talk(name="Talk Three", length_minutes=25),
        Talk(name="Talk One", length_minutes=10),
    ]

    # When
    tracks = schedule_talks(talks_input)

    # Then
    for track in tracks:
        assert all(x.end_time < LUNCH_START for x in track.talks_before_lunch)
        assert all(x.start_time > LUNCH_END for x in track.talks_after_lunch)


def test_networking_start_correctly() -> None:
    # Given
    talks_input = [
        Talk(name="Talk Two", length_minutes=5),
        Talk(name="Talk Three", length_minutes=25),
        Talk(name="Talk One", length_minutes=10),
    ]

    # When
    tracks = schedule_talks(talks_input)

    # Then
    assert all(
        track.talks_after_lunch[-1].end_time < NETWORKING_START_LATEST
        for track in tracks
        if track.talks_after_lunch
    )


def test_no_breaks_between_talks() -> None:
    # Given
    talks_input = [
        Talk(name="Talk Two", length_minutes=5),
        Talk(name="Talk Three", length_minutes=25),
        Talk(name="Talk One", length_minutes=10),
    ]

    # When
    tracks = schedule_talks(talks_input)

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
