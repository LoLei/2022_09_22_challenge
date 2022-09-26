import pytest

from problem_2.src.main import parse_input
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