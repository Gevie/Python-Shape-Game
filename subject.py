from dataclasses import dataclass, field
from datetime import date
from recording import RecordingInterface
from typing import List


@dataclass
class Round:
    allowed_stages: List = field(default_factory=lambda: ['Game', 'SingleChoiceGame', 'Stimulation'])
    current_round: int = 1
    iap: int = 0
    max_rounds: int = 12
    stage: str = 'Game'
    stimulation_type: str = 'Baseline'

    def increment(self) -> None:
        if self.max_rounds <= self.current_round:
            self.current_round = 1
            return None

        self.current_round = self.current_round + 1

    def set_stage(self, stage: str) -> None:
        if stage not in self.allowed_stages:
            raise ValueError(f'"{stage}" is not an accepted stage for this game')

        self.stage = stage

    def switch_stimulation_type(self) -> None:
        self.stimulation_type = f'IAPS{self.iap}' if self.stimulation_type == 'Baseline' else 'Baseline'


@dataclass
class Subject:
    id: int
    date: date
    data: dict

    def get_key(self):
        """Questioning why this is needed given the data example Pedro gave me"""
        pass

    def create_data_template(self):
        self.data = {
            self.id: {
                self.date: {
                    'Timestamps': {
                        'Baseline': {}
                    },
                    'Stimulation': {}
                }
            }
        }

    def add_timestamp(self, current_round: Round, timestamp: str) -> None:
        if current_round.stage != 'Stimulation':
            current_round = f'Q{current_round.current_round}'
            self.data[self.id][self.date]['Timestamps']['Baseline'].update({current_round: timestamp})
            return None

        self.data[self.id][self.date]['Stimulation'][current_round.stimulation_type] = timestamp

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

        if self.current_round.stage == 'Stimulation':
            self.current_round.switch_stimulation_type()

        self.current_round.increment()  # TODO: Move this elsewhere

    def save_results(self):
        self.recording_handler.tear_down()
        self.subject.save()
