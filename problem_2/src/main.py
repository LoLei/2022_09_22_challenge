#!/usr/bin/env python3

from problem_2.src.model.model import Track
from problem_2.src.scheduler import parse_and_schedule

"""
Problem 2
"""

__author__ = "Lorenz Leitner"
__version__ = "0.1.0"
__license__ = "MIT"


def print_tracks(tracks: list[Track]) -> None:
    for i, track in enumerate(tracks):
        print(f"> Track {i + 1}")
        print(f"{track}\n")


def main():
    tracks = parse_and_schedule()
    print_tracks(tracks)


if __name__ == "__main__":
    main()
