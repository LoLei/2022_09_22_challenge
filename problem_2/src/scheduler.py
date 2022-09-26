import copy
from datetime import datetime
from pathlib import Path
from typing import Optional

from problem_2.src.input_parser import parse_input
from problem_2.src.model.model import Talk, Track, ScheduledTalk
from problem_2.src.util.consts import (
    LUNCH_START,
    NETWORKING_START_LATEST,
    CONFERENCE_START,
    LUNCH_END,
    NETWORKING_START_EARLIEST,
)


def _do_schedule(
    talks: list[Talk], track: Track, criteria_time: datetime, current_time: datetime
) -> datetime:
    """
    This method schedules a list of talks to a track,
    either before lunch or before the latest networking event start time.
    Warning: This method mutates the input arguments.
    """
    while talks:
        # Take talk from the beginning
        talk = talks.pop(0)
        scheduled_talk = ScheduledTalk(start_time=current_time, talk=talk)
        if scheduled_talk.end_time <= criteria_time:
            # Add the talk to the track if it fits, remove it from the list
            if criteria_time == LUNCH_START:
                track.talks_before_lunch.append(scheduled_talk)
            elif criteria_time == NETWORKING_START_LATEST:
                track.talks_after_lunch.append(scheduled_talk)
            else:
                raise ValueError(f"Cannot use {criteria_time=}")
            current_time = scheduled_talk.end_time
        else:
            # Otherwise, add it again to the end of the list to try again later
            talk.attempted_schedule = True
            talks.append(talk)
            # Prevent retrying the same over and over again
            if talk.attempted_schedule:
                break
    return current_time


def _append_talks_to_track(talks: list[Talk]) -> Track:
    current_time = CONFERENCE_START
    track = Track()

    _do_schedule(
        talks=talks, track=track, criteria_time=LUNCH_START, current_time=current_time
    )

    current_time = LUNCH_END

    current_time = _do_schedule(
        talks=talks,
        track=track,
        criteria_time=NETWORKING_START_LATEST,
        current_time=current_time,
    )

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
    # Deepcopy may be not needed, used in case preservation of original argument is desired
    talks_to_schedule = copy.deepcopy(talks_unsorted)
    tracks: list[Track] = []

    while talks_to_schedule:
        track = _append_talks_to_track(talks_to_schedule)
        tracks.append(track)

    # Make networking event start time the same for all tracks, i.e. the latest of all tracks
    networking_event_start_time_latest_scheduled: datetime = max(
        [track.networking_event_start for track in tracks]
    )
    for track in tracks:
        track.networking_event_start = networking_event_start_time_latest_scheduled

    return tracks


def parse_and_schedule(input_file: Optional[Path] = None) -> list[Track]:
    talks: list[Talk] = parse_input(file_location=input_file)
    return schedule_talks_to_tracks(talks)
