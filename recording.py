import time
from abc import ABC, abstractmethod


class RecordingInterface(ABC):
    """The recording interface, used for gathering timestamps"""

    @abstractmethod
    def get_timestamp(self) -> str:
        """Get the current timestamp"""

    @abstractmethod
    def tear_down(self) -> None:
        """End the recording interface"""


class SimpleRecording(RecordingInterface):
    """A simple recording class for getting milliseconds since the game started"""

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
    def __init__(self):
        """
        Initialize the class
        """

        # bp.start()
        pass

    def get_timestamp(self) -> str:
        """
        Get the timestamp since the game using the bioplus library

        Returns:
            str: The bioplus timestamp
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
        pass
