#!/usr/bin/env python3
import copy
import fileinput
import re
from datetime import date, datetime, time
from pathlib import Path
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


def _append_talks_to_track(talks: list[Talk]) -> Track:
    current_time = CONFERENCE_START
    track = Track()

    while True:
        # Take talk from the beginning
        talk = talks.pop(0)
        if talk.scheduled:  # TODO: Maybe not needed since they're popped anyway
            continue
        scheduled_talk = ScheduledTalk(start_time=current_time, talk=talk)
        if scheduled_talk.end_time <= LUNCH_START:
            # Add the talk to the track if it fits, remove it from the list
            track.talks_before_lunch.append(scheduled_talk)
            current_time = scheduled_talk.end_time
            talk.scheduled = True
        else:
            # Otherwise, add it again to the end of the list to try again later
            talk.attempted_schedule = True
            talks.append(talk)
            # Prevent retrying the same over and over again
            if talk.attempted_schedule:
                break

    current_time = LUNCH_END

    # Same as above but checking networking event instead of lunch
    while talks:
        talk = talks.pop(0)
        scheduled_talk = ScheduledTalk(start_time=current_time, talk=talk)
        if scheduled_talk.end_time <= NETWORKING_START_LATEST:
            track.talks_after_lunch.append(scheduled_talk)
            current_time = scheduled_talk.end_time
            talk.scheduled = True
        else:
            talk.attempted_schedule = True
            talks.append(talk)
            if talk.attempted_schedule:
                break

    track.networking_event_start = (
        current_time
        if (
            track.talks_after_lunch
            and track.talks_after_lunch[-1].end_time >= NETWORKING_START_EARLIEST
        )
        else NETWORKING_START_EARLIEST
    )
    return track


def schedule_talks_to_tracks(talks_unsorted: list[Talk]) -> list[Track]:
    talks_to_schedule = copy.deepcopy(talks_unsorted)  # TODO: Deepcopy maybe not needed
    tracks: list[Track] = []

    while talks_to_schedule:
        track = _append_talks_to_track(talks_to_schedule)
        tracks.append(track)

    return tracks


def print_tracks(tracks: list[Track]) -> None:
    for i, track in enumerate(tracks):
        print(f"> Track {i + 1}")
        print(f"{track}\n")


def parse_and_schedule(input_file: Optional[Path] = None) -> list[Track]:
    talks: list[Talk] = parse_input(file_location=input_file)
    return schedule_talks_to_tracks(talks)


def main():
    tracks = parse_and_schedule()
    print_tracks(tracks)


if __name__ == "__main__":
    main()
