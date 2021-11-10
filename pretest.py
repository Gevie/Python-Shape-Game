from biosignals import Device, Session, Recording
from recording import BioPlusRecording
import time
# import matplotlib.pyplot as plt


# TODO: prepare to open log files for recordings
# TODO: prepare to plot all necessary data

'''
Initializing all of the necessary classes
'''
eeg_device = Device()
eeg_session = Session()
eeg_session.prepare_dict()
eeg = Recording()
BioPlusRecording = BioPlusRecording()
time.sleep(20)
BioPlusRecording.tear_down()


