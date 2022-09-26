#!/usr/bin/env python3
from pathlib import Path
from typing import Optional
import fileinput

from problem_2.src.model.talk import Talk

"""
Problem 2
"""

__author__ = "Lorenz Leitner"
__version__ = "0.1.0"
__license__ = "MIT"


def parse_input(optional_input_strs: Optional[list[str]] = None) -> list[Talk]:
    # Inject dependency for testing
    input_strs = optional_input_strs if optional_input_strs else fileinput.input()

    # Read from input and clean each line, remove blank lines
    # Assumption: Each line starts with '> '
    talks_input: list[str] = [line.strip()[2:] for line in input_strs if line.strip()]

    # Replace lightning talks with 5 minutes,
    # replace 'min' with nothing,
    talks_replaced: list[list[str]] = [
        ti.replace("lightning", "5min").replace("min", "").rsplit(" ", 1)
        for ti in talks_input
    ]

    # Transform to data class and return
    return [Talk(name=x[0], length_minutes=int(x[1])) for x in talks_replaced]


def main():
    talks: list[Talk] = parse_input()
    print(talks)


if __name__ == "__main__":
    main()
