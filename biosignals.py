import platform
import sys
from dataclasses import dataclass, field
import plux


osDic = {"Darwin": "MacOS",
         "Linux": "Linux64",
         "Windows": ("Win32_37", "Win64_37")}
if platform.system() != "Windows":
    sys.path.append("PLUX-API-Python3/{}/plux.so".format(osDic[platform.system()]))
else:
    if platform.architecture()[0] == '64bit':
        sys.path.append("PLUX-API-Python3/Win64_37")
    else:
        sys.path.append("PLUX-API-Python3/Win32_37")



@dataclass
class Device:
    """
    Stores the integer corresponding to the port occupied by the device.
    Defaults to port 1
    """

    source: int = 1

    def set_port(self, source: int):
        self.source = source


@dataclass
class Session(Device):
    """
    Stores session data in a dict
    """
    session_data: dict = field(default_factory=dict)
    sampling_frequency: int = 1200
    resolution: int = 16
    allowed_resolutions: list = field(default_factory=lambda: [8, 16])
    allowed_settings: list = field(default_factory=lambda: ['fs', 'res', 'source'])

    def prepare_dict(self):
        """
        Initializes the dictionary where the session's settings
        are stored.
        """
        self.session_data = {
            'fs': self.sampling_frequency,
            'source': Device.source,
            'res': self.resolution
        }

    def update_dict(self, setting: str, value: int):
        if setting not in self.allowed_settings:
            raise ValueError('The setting introduced is not allowed')
        else:
            if setting == 'fs':
                self.sampling_frequency = value
            elif setting == 'source':
                Device.set_port(self, value)
            else:
                if value not in self.allowed_resolutions:
                    raise ValueError('This is not an allowed resolution')
                self.resolution = value
        self.session_data[setting] = value


@dataclass
class Recording(Session):
    """
    Handles the management of the Biosignals Plux recording session
    """

    session = Session()

    def eeg_start(self):
        plux.SignalsDev.start(
            self.session.session_data['fs'],
            self.session.session_data['source'],
            self.session.session_data['res'])

    @staticmethod
    def eeg_stop():
        plux.SignalsDev.stop()
