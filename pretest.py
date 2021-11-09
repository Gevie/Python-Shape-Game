from biosignals import Device, Session, Recording
from recording import BioPlusRecording
import time

# TODO: prepare to open log files for recordings
# TODO: prepare to plot all necessary data

'''
Initializing all of the necessary classes
'''
eeg_device = Device(1)
eeg_session = Session(1200, {}, 16, field(default_factory=lambda: [8, 16]), field(default_factory=lambda: ['fs', 'res',
                                                                                                           'source']))
eeg_session.prepare_dict()
eeg = Recording(eeg_session)
BioPlusRecording = BioPlusRecording()
time.sleep(20)
BioPlusRecording.tear_down()

