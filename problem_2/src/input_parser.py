import fileinput
import re
from pathlib import Path
from typing import Optional

from problem_2.src.model.talk import Talk


def parse_input(
    optional_input_strs: Optional[list[str]] = None,
    file_location: Optional[Path] = None,
) -> list[Talk]:
    # Inject dependency for testing
    file_lines: list[str] = []
    if file_location:
        with open(file_location) as file:
            file_lines = file.readlines()
    input_strs = (
        optional_input_strs
        if optional_input_strs
        else file_lines
        if file_lines
        else fileinput.input()
    )

    # Read from input and clean each line, remove blank lines
    # Assumption: Each line starts with '> '
    talks_input: list[str] = [line.strip()[2:] for line in input_strs if line.strip()]

    # Filter lines that do not conform to format
    talks_filtered: list[str] = [
        line for line in talks_input if re.compile(".*(\\d+min|lightning)$").match(line)
    ]

    # Replace lightning talks with 5 minutes and split at last space to separate minutes from name
    talks_lightning_replaced: list[list[str]] = [
        t.replace("lightning", "5min").rsplit(" ", 1) for t in talks_filtered
    ]

    # Replace 'min' with nothing,
    talks_minute_replaced: list[list[str]] = [
        [t[0], re.sub("min$", "", t[1])] for t in talks_lightning_replaced
    ]

    # Transform to data class and return
    return [Talk(name=t[0], length_minutes=int(t[1])) for t in talks_minute_replaced]
