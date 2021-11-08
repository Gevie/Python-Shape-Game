import unittest
from biosignals import Session
from biosignals import Device
from biosignals import Recording


class TestBioSignals(unittest.TestCase):

    def test_set_port(self):
        self.assertIsNotNone(Device.source)
        Device.set_port(5)
        self.assertIsNotNone(Device.source)
