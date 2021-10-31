from dataclasses import dataclass, field
from datetime import date
from recording import RecordingInterface
from typing import List


@dataclass
class Round:
    allowed_stages: List = field(default_factory=lambda: ['Game', 'SingleChoiceGame', 'Stimulation'])
    current_round: int = 1
    max_rounds: int = 12
    stage: str = 'Game'

    def increment(self) -> None:
        if self.max_rounds <= self.current_round:
            self.current_round = 1
            return None

        self.current_round = self.current_round + 1

    def set_stage(self, stage: str) -> None:
        if stage not in self.allowed_stages:
            raise ValueError(f'"{stage}" is not an accepted stage for this game')

        self.stage = stage


@dataclass
class Subject:
    id: int
    date: date
    data: dict

    def get_id(self):
        pass

    def get_date(self):
        pass

    def get_key(self):
        pass

    def add_timestamp(self, current_round: Round, timestamp: str):
        pass

    def save(self):
        pass


@dataclass
class Instance:
    subject: Subject
    recording_handler: RecordingInterface
    current_round: Round

    def add_timestamp(self) -> None:
        timestamp = self.recording_handler.get_timestamp()
        self.subject.add_timestamp(self.current_round, timestamp)

    def save_results(self):
        self.recording_handler.tear_down()
        self.subject.save()
