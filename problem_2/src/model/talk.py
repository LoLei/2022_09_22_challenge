from datetime import datetime, timedelta

from dataclasses import dataclass


@dataclass
class Talk:
    name: str
    length_minutes: int


@dataclass
class ScheduledTalk(Talk):
    def __init__(self, start_time: datetime, talk: Talk) -> None:
        super().__init__(talk.name, talk.length_minutes)
        self.start_time: datetime = start_time

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
    talks_before_lunch: list[ScheduledTalk]
    talks_after_lunch: list[ScheduledTalk]
    networking_event_start: datetime
