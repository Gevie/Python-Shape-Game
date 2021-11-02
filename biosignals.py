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

    source: str

    def set_port(self, source: int):
        self.source = source


@dataclass
class Session(Device):
    """
    Stores session data in a dict
    """
    Device: Device
    Session_Data: dict
    sampling_frequency: int = 1200
    Resolution: int = 16
    Allowed_Resolutions: list = field(default_factory=lambda: [8, 16])
    Allowed_Settings: list = field(default_factory=lambda: ['fs', 'res', 'source'])

    def prepare_dict(self):
        """
        Initializes the dictionary where the session's settings
        are stored.
        """
        self.Session_Data = {
            'fs': self.sampling_frequency,
            'source': Device.source,
            'res': self.Resolution
        }

    def update_dict(self, setting: str, value: int):
        if setting not in self.Allowed_Settings:
            raise ValueError('The setting introduced is not allowed')
        else:
            if setting == 'fs':
                self.sampling_frequency = value
            elif setting == 'source':
                Device.set_port(self, value)
            else:
                if value not in self.Allowed_Resolutions:
                    raise ValueError('This is not an allowed resolution')
                self.Resolution = value
        self.Session_Data[setting] = value


@dataclass
class Recording(Session):
    """
    Handles the management o the Biosignals Plux recording session
    """
