import time
from abc import ABC, abstractmethod
from biosignals import Recording


class RecordingInterface(ABC):
    """
    The recording interface

    This is used to be able to get timestamps when actions are taken
    """

    @abstractmethod
    def get_timestamp(self) -> str:
        """
        Get the current timestamp

        Returns:
            str: The timestamp as a string
        """

    @abstractmethod
    def tear_down(self) -> None:
        """
        End the recording interface

        Returns:
            None
        """


class SimpleRecording(RecordingInterface):
    """
    Recording timestamps using a the python time library

    This is a simple way to get timestamps, it does not align with any type of
    ECG and EEG recordings and is a more simple but accessible implementation
    """

    def __init__(self):
        """
        Initialize the class
        """

        self.start_time = self.__get_current_timestamp()

    @staticmethod
    def __get_current_timestamp() -> int:
        """
        Get the current timestamp in milliseconds

        Returns:
            int: The number of milliseconds
        """

        return round(time.time() * 1000)

    def get_timestamp(self) -> str:
        """
        Get the timestamp since the game started in milliseconds

        Returns:
            str: The number of milliseconds since the game started
        """

        return str(self.start_time - self.__get_current_timestamp())

    def tear_down(self) -> None:
        """
        Executed when the game is over (nothing required here)

        Returns:
            None
        """

        pass


class BioPlusRecording(RecordingInterface):
    """
    Recording timestamps with the BioPlus library

    This is used to be able to compare timestamps with BioPlus EEG and ECG
    recordings taken when the game is played.
    """

    def __init__(self):
        """
        Initialize the class
        """
        # bp.start()
        Recording.eeg_start()
        pass

    def get_timestamp(self) -> str:
        """
        Get the timestamp since the game started using the BioPlus library

        Returns:
            str: The BioPlus timestamp
        """

        # return bp.get_timestamp()
        return "Todo: Implement BioPlus"

    def tear_down(self) -> None:
        """
        Executed when the game is over

        Returns:
            None
        """

        # bp.stop()
        Recording.eeg_stop()
        pass
