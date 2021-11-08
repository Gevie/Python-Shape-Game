import unittest
from biosignals import Session
from biosignals import Device
from biosignals import Recording


class TestBioSignals(unittest.TestCase):

    def test_set_port(self):
        self.assertIsNotNone(Device.source)
        Device.set_port(5)
        self.assertIsNotNone(Device.source)

    def test_prepare_dict(self):
        Session.prepare_dict()
        self.assertIsNotNone(Session.session_data)

    def test_update_dict(self):
        Session.update_dict(1, 'r')

    def test_eeg_start(self):
        Recording.eeg_start()

    def test_eeg_stop(self):
        Recording.eeg_stop()

if __name__ == '__main__':
    unittest.main
