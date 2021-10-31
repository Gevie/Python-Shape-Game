import datetime
from dataclasses import dataclass
# from mpydev import BioPac as bp
import numpy as np
from datetime import date


@dataclass
class Subject:
    Subject_ID: int
    Subject_Test_Date: date
    Subject_key: dict

class SubjectHandle(Subject):
    def identify_subject(self):
        subject_id = input('Insert subject ID')
        if isinstance(subject_id, int):
            self.Subject_ID = subject_id
        else:
            raise ValueError('The Subjects ID must be an integer')
            self.identify_subject()

    def get_date(self):
        self.Subject_Test_Date = date.today()
        return self.Subject_Test_Date

    def get_subject_id(self):
        return self.Subject_ID

    def get_subject(self):
        self.Subject_Key = f'{self.Subject_ID}({self.Subject_Test_Date})'
        return self.Subject_Key


@dataclass
class TestData(SubjectHandle):
    Test_Data: dict


class TestDataHandler(TestData):

    def initialize_test(self):
        self.identify_subject()
        key = self.Subject_Key()
        self.Test_Data = {key: {}}

    def first_timestamp(self, first_timestamp_list: dict):
        self.Test_Data[self.get_subject()]['Timestamps'] = first_timestamp_list

    def timestamp_add(self, timestamp: dict):
        self.Test_Data[self.get_subject()]['Timestamps'].update(timestamp)

    def database_commit(self):
        with open(f'{self.get_subject()}.txt') as json:
            json.dump(self.Test_Data)


@dataclass
class TimeStamps(TestDataHandler):
    # TODO: figure out better init method for this?
    timestamp: int or float or str
    ts_dict: dict
    stage: str
    one_to_twenty_four: list
    one_to_twenty: list
    one_to_twenty_four = np.arange(1, 25, 1)
    twenty_seven_to_eighty_one = np.arange(27, 81, 1)
    allowed_stages = ['Baseline', f'Q{one_to_twenty_four}', f'IAPS{twenty_seven_to_eighty_one}']


class ManageTimestamps(TimeStamps):
    def create_timestamp(self, stage: str):
        if stage in self.allowed_stages:
            self.stage = stage
        else:
            raise ValueError('Stage must be one of the pre-approved for this protocol.')
            return
        # timestamp = bp.get_timestamp()
        timestamp = 1818
        self.timestamp = timestamp
        self.ts_dict = {self.stage: self.timestamp}
        if self.stage == 'Baseline':
            self.first_timestamp(self.ts_dict)
        else:
            self.timestamp_add(self.ts_dict)
        return self.ts_dict
