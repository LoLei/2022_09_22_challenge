from datetime import datetime, timedelta

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Talk:
    name: str
    length_minutes: int
    attempted_schedule: bool = False
    scheduled: bool = False


@dataclass
class ScheduledTalk(Talk):
    def __init__(self, start_time: datetime, talk: Talk) -> None:
        super().__init__(talk.name, talk.length_minutes)
        self.start_time: datetime = start_time

    def __str__(self) -> str:
        duration = (
            "lightning" if self.length_minutes == 5 else f"{self.length_minutes}min"
        )
        return "> " + f"{self.start_time} " + f"{self.name} " + duration

    def __repr__(self) -> str:
        return (
            "ScheduledTalk("
            + f"start_time={self.start_time}, "
            + f"name={self.name}, "
            + f"length_minutes={self.length_minutes}, "
            + f"end_time={self.end_time}"
            + ")"
        )

    @property
    def end_time(self) -> datetime:
        return self.start_time + timedelta(minutes=self.length_minutes)


@dataclass
class Track:
    talks_before_lunch: list[ScheduledTalk] = field(default_factory=lambda: [])
    talks_after_lunch: list[ScheduledTalk] = field(default_factory=lambda: [])
    networking_event_start: Optional[datetime] = None  # Filled at a later time

    def __str__(self) -> str:
        string = ""
        for talk in self.talks_before_lunch:
            string += f"{talk}\n"
        string += f"> 12PM Lunch\n"  # TODO: Cannot use LUNCH_START from main due to circular import
        for talk in self.talks_after_lunch:
            string += f"{talk}\n"
        string += f"> {self.networking_event_start} Networking Event"
        return string
