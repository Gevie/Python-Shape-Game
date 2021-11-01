import json
from dataclasses import dataclass, field
from datetime import date
from recording import RecordingInterface
from typing import List


@dataclass
class Round:
    """
    Holds the information about the game round

    This class holds information about current round and all potential rounds
    """

    allowed_stages: List = field(default_factory=lambda: ['Game', 'SingleChoiceGame', 'Stimulation'])
    current_round: int = 1
    iap: str = '1'
    max_rounds: int = 24
    stage: str = 'Game'
    stimulation_type: str = 'Baseline'

    def increment(self) -> None:
        """
        Increment the round by 1 or reset to 1 if we hit the limit

        Returns:
            None
        """

        if self.max_rounds <= self.current_round:
            self.current_round = 1
            return None

        self.current_round = self.current_round + 1

    def set_stage(self, stage: str) -> None:
        """
        Used to set the stage operation

        Args:
            stage (str): The new stage to set

        Returns:
            None
        """

        if stage not in self.allowed_stages:
            raise ValueError(f'"{stage}" is not an accepted stage for this game')

        self.stage = stage

    def switch_stimulation_type(self) -> None:
        """
        Switch the stimulation type from either IAPS{n} or Baseline

        Returns:
            None
        """

        if self.stimulation_type == 'Baseline':
            self.stimulation_type = f'IAPS({self.iap})'
        else:
            self.stimulation_type = 'Baseline'


@dataclass
class Subject:
    """
    The test subject

    Holds information about the subject, the date the test occurred and holds
    the data for the test
    """

    id: int
    date: date
    data: dict

    def get_key(self):
        """
        Gets the key for the subject file name

        Returns:
            str: The subject key
        """

        return f'{self.id}({self.date})'

    def create_data_template(self):
        """
        Create the data template ready for data population

        Returns:
            dict: The template for the json data
        """

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
        """
        Stores the timestamp for a round against a round

        Args:
            current_round (Round): The round object
            timestamp (str): The timestamp to store against said round

        Returns:
            None
        """
        fround = f'Q{current_round.current_round}'
        self.data[self.id][self.date]['Timestamps']['Baseline'].update({fround: timestamp})
        return None

    def add_stim_timestamp(self, timestamp, iap):
        fround = f'IAPS({iap})'
        self.data[self.id][self.date]['Stimulation'].update({fround: timestamp})

    def save(self) -> None:
        """
        Save the subject data to the appropriate json file

        Returns:
            None
        """

        subject_file = open('timestamps.json', 'w')
        json.dump(self.data, subject_file, ensure_ascii=False, indent='\t', separators=(',', ':'))
        subject_file.close()


@dataclass
class Instance:
    """
    Holds the current game instance

    Also contains the appropriate recording concretion, current round and subject
    """

    subject: Subject
    recording_handler: RecordingInterface
    current_round: Round

    def add_timestamp(self) -> None:
        """
        Add the timestamp to the subject

        Returns:
            None
        """

        #if self.current_round.stage == 'Stimulation':
        #    self.current_round.switch_stimulation_type()

        timestamp = self.recording_handler.get_timestamp()
        self.subject.add_timestamp(self.current_round, timestamp)

        self.current_round.increment()  # TODO: Move this elsewhere

    def add_stim_timestamp(self, iap) -> None:
        """
        Add the timestamp to the subject

        Returns:
            None
        """

        #if self.current_round.stage == 'Stimulation':
        #    self.current_round.switch_stimulation_type()

        timestamp = self.recording_handler.get_timestamp()
        self.subject.add_stim_timestamp(timestamp, iap)

        self.current_round.increment()  # TODO: Move this elsewhere

    def save_results(self) -> None:
        """
        The game has ended so save all results and tear down


        Returns:
            None
        """

        self.recording_handler.tear_down()
        self.subject.save()
