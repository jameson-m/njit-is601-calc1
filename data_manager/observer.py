"""File Observer"""
import time
from watchdog.observers import Observer
from data_manager.manager import DataManager
from data_manager.handler import FileHandler

# pylint: disable=too-few-public-methods
class FileObserver:
    """File Observer"""
    DIRECTORY: str = DataManager.get_absolute_path_from_relative_path("input")

    def __init__(self):
        self.observer = Observer()

    def run(self):
        """Starts the FileObserver
        """
        patterns = ["*.csv"]
        ignore_directories = True
        case_sensitive = True
        # pylint: disable=line-too-long
        file_event_handler = FileHandler(patterns=patterns, ignore_directories=ignore_directories, case_sensitive=case_sensitive)
        self.observer.schedule(file_event_handler, self.DIRECTORY)
        self.observer.start()

        # pylint: disable=bare-except
        try:
            while True:
                time.sleep(1)
        except:
            self.observer.stop()
            self.observer.join()
