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

    allowed_stages: List = field(default_factory=lambda: ['Baseline', 'Game', 'SingleChoiceGame', 'Stimulation'])
    current_round: int = 1 or str
    iap: str = '1'
    max_rounds: int = 81
    stage: str = 'Game'

    def increment(self) -> None:
        """
        Increment the round by 1 or reset to 1 if we hit the limit

        Returns:
            None
        """
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


@dataclass
class Subject:
    """
    The test subject

    Holds information about the subject, the date the test occurred and holds
    the data for the test
    """

    id: str
    date: str
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
                        'Baseline': {},
                        'Stimulation': {}
                    }
                }
            }
        }

    def add_timestamp(self, current_round: Round, words, stage, timestamp: str) -> None:
        """
        Stores the timestamp for a round against a round

        Args:
            current_round (Round): The round object
            timestamp (str): The timestamp to store against said round

        Returns:
            None
        """
        if stage == 'Game':
            self.data[self.id][self.date]['Timestamps']['Baseline'].update({f'Q{words}': timestamp})
            # print(self.data)
            pass
        elif stage == 'Stimulation':
            self.data[self.id][self.date]['Timestamps']['Stimulation'].update(
                {f'IAPS({words})': timestamp})
            # print(self.data)
            pass
        elif stage == 'Baseline':
            self.data[self.id][self.date]['Timestamps']['Stimulation'].update({f'Baseline({words})': timestamp})
            # print(self.data)
            pass

    def save(self) -> None:
        """
        Save the subject data to the appropriate json file
        Returns:
            None
        """

        with open('timestamps.json', 'r') as file:
            subject_file = json.load(file)
        subject_file.update(self.data)
        with open('timestamps.json', 'w') as final_file:
            json.dump(subject_file, final_file)


@dataclass
class Instance:
    """
    Holds the current game instance

    Also contains the appropriate recording concretion, current round and subject
    """

    subject: Subject
    recording_handler: RecordingInterface
    Round: Round

    def add_timestamp(self, words, stage) -> None:
        """
        Add the timestamp to the subject

        Returns:
            None
        """

        # if self.current_round.stage == 'Stimulation':
        #    self.current_round.switch_stimulation_type()

        timestamp = self.recording_handler.get_timestamp()
        self.subject.add_timestamp(self.Round, words, stage, timestamp)
        self.Round.increment()  # TODO: Move this elsewhere

    def save_results(self) -> None:
        """
        The game has ended so save all results and tear down


        Returns:
            None
        """

        self.recording_handler.tear_down()
        self.subject.save()
