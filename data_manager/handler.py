"""File Handler"""
from typing import List
import ntpath
import shutil
from watchdog.events import PatternMatchingEventHandler
from data_manager.calculation_processor import CalculationProcessor

from data_manager.manager import DataManager

class FileHandler(PatternMatchingEventHandler):
    """File Handler"""
    def __init__(self, patterns: List, ignore_directories: bool, case_sensitive: bool):
        # pylint: disable=line-too-long
        super().__init__(patterns=patterns, ignore_directories=ignore_directories, case_sensitive=case_sensitive)

    @staticmethod
    # pylint: disable=inconsistent-return-statements
    def on_any_event(event):
        if event.is_directory:
            return None
        if event.event_type == "created":
            df = DataManager.read_csv_data(event.src_path)
            calculation_types = DataManager.get_calculation_types(df)
            values = DataManager.get_list_of_values(df)
            file_name = ntpath.basename(event.src_path)

            # Process all calculations on CSV file
            print(f"[INFO] Processing {file_name} calculations...")
            CalculationProcessor.process_csv_calculations(file_name, calculation_types, values)

            # Move CSV file to done folder
            new_path = DataManager.get_absolute_path_from_relative_path(f"input_done/{file_name}")
            shutil.move(event.src_path, new_path)
