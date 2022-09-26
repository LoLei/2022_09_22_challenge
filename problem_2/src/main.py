#!/usr/bin/env python3
import copy
import fileinput
import re
from datetime import date, datetime, time
from typing import Optional

from problem_2.src.model.talk import Talk, ScheduledTalk, Track

"""
Problem 2
"""

__author__ = "Lorenz Leitner"
__version__ = "0.1.0"
__license__ = "MIT"

# Consts
CONFERENCE_START = datetime.combine(date.today(), time(hour=9))
LUNCH_START = datetime.combine(date.today(), time(hour=12))
LUNCH_END = datetime.combine(date.today(), time(hour=13))
NETWORKING_START_EARLIEST = datetime.combine(date.today(), time(hour=16))
NETWORKING_START_LATEST = datetime.combine(date.today(), time(hour=17))


def parse_input(optional_input_strs: Optional[list[str]] = None) -> list[Talk]:
    # Inject dependency for testing
    input_strs = optional_input_strs if optional_input_strs else fileinput.input()

    # Read from input and clean each line, remove blank lines
    # Assumption: Each line starts with '> '
    talks_input: list[str] = [line.strip()[2:] for line in input_strs if line.strip()]

    # Replace lightning talks with 5 minutes and split at last space to separate minutes from name
    talks_lightning_replaced: list[list[str]] = [
        t.replace("lightning", "5min").rsplit(" ", 1) for t in talks_input
    ]

    # Replace 'min' with nothing,
    talks_minute_replaced: list[list[str]] = [
        [t[0], re.sub("min$", "", t[1])] for t in talks_lightning_replaced
    ]

    # Transform to data class and return
    return [Talk(name=t[0], length_minutes=int(t[1])) for t in talks_minute_replaced]


def schedule_talks(talks_unsorted: list[Talk]) -> list[Track]:
    talks_to_schedule = copy.deepcopy(talks_unsorted)
    tracks: list[Track] = [Track()]

    current_time = CONFERENCE_START
    current_track = tracks[0]

    while talks_to_schedule:
        talk = talks_to_schedule.pop(0)
        scheduled_talk = ScheduledTalk(start_time=current_time, talk=talk)
        if scheduled_talk.end_time < LUNCH_START:
            current_track.talks_before_lunch.append(scheduled_talk)
            current_time = scheduled_talk.end_time

    while talks_to_schedule:
        talk = talks_to_schedule.pop(0)
        scheduled_talk = ScheduledTalk(start_time=current_time, talk=talk)
        if scheduled_talk.end_time < NETWORKING_START_LATEST:
            current_track.talks_after_lunch.append(scheduled_talk)
            current_time = scheduled_talk.end_time

    if len(talks_to_schedule) != 0:
        # Create second track
        tracks.append(Track())

    return tracks


def main():
    talks: list[Talk] = parse_input()
    print(talks)
    scheduled_talks = schedule_talks(talks)
    print(scheduled_talks)


if __name__ == "__main__":
    main()
