from problem_2.src.input_parser import parse_input
from problem_2.src.model.talk import Talk
from problem_2.test.consts import INPUT_STRS_1, INPUT_TALKS_1


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
