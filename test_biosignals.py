import unittest
from biosignals import Session
from biosignals import Device
from biosignals import Recording
from dataclasses import dataclass, field


Device(1)
Session(1200, {}, 16, field(default_factory=lambda: [8, 16]), field(default_factory=lambda: ['fs', 'res', 'source']))
Recording(1200, {}, 16)


class TestBioSignals(unittest.TestCase):

    def test_set_port(self):
        self.assertIsNotNone(Device.source)
        Device.set_port(5)
        self.assertIsNotNone(Device.source)

    def test_prepare_dict(self):
        Session.prepare_dict(Session)
        self.assertIsNotNone(Session.session_data)

    def test_update_dict(self):
        Session.update_dict(1, 'r')

    def test_eeg_start(self):
        Recording.eeg_start()

    def test_eeg_stop(self):
        Recording.eeg_stop()


if __name__ == '__main__':
    unittest.main
