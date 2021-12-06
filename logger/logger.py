"""Logger"""
import time
import uuid
from data_manager.manager import DataManager

class Logger:
    """Logger class that writes system logs to files."""
    input_file_name = ""

    @staticmethod
    def set_input_file_name(file_name: str) -> True:
        """Sets the input file name for Logger.
        """
        Logger.input_file_name = file_name
        return True

    @staticmethod
    def get_unix_timestamp() -> int:
        """Get a UNIX timestamp.

        Returns:
            int: timestamp
        """
        return int(time.time())

    @staticmethod
    def get_record_number() -> str:
        """Gets a unique record number.

        Returns:
            str: UUID number
        """
        return str(uuid.uuid4())

    @staticmethod
    def write_to_log(data: tuple, columns: tuple, output_file_path: str) -> bool:
        """Writes the given data to a CSV log file.

        Args:
            data (tuple): Data to be written.
            columns (tuple): Column headers.
            output_file_path (str): Absolute file path for output file.

        Returns:
            bool: Whether or not the log was written.
        """
        was_written_to_csv = DataManager.write_csv_data(data, columns, output_file_path)
        return was_written_to_csv

    @staticmethod
    def write_calculation_log(operation: str, calculation_result: str) -> bool:
        """Writes a calculation's information to a log file.

        Args:
            operation (str): Operation done. Ex: 2 + 2
            calculation_result (str): Result of operation.

        Returns:
            bool: Whether or not the calculation was written to log.
        """
        timestamp = Logger.get_unix_timestamp()
        record_number = Logger.get_record_number()
        # pylint: disable=line-too-long
        output_file_path = DataManager.get_absolute_path_from_relative_path("results/calculation_results.csv")

        # pylint: disable=line-too-long
        output_data = (record_number, timestamp, Logger.input_file_name, operation, calculation_result)
        columns = ("record", "timestamp", "input_file", "operation", "result")

        log_was_written = Logger.write_to_log(output_data, columns, output_file_path)
        return log_was_written

    @staticmethod
    def write_error_log(operation: str, error_message: str) -> bool:
        """Writes a calculation error to the error log file.

        Args:
            operation (str): Operation done. Ex: 2 + 2
            error_message (str): Error message explaining what was wrong.

        Returns:
            bool: Whether or not the error was written to log.
        """
        timestamp = Logger.get_unix_timestamp()
        record_number = Logger.get_record_number()
        # pylint: disable=line-too-long
        output_file_path = DataManager.get_absolute_path_from_relative_path("results/calculation_results_errors.csv")

        output_data = (record_number, timestamp, Logger.input_file_name, operation, error_message)
        columns = ("record", "timestamp", "input_file", "operation", "error_message")

        log_was_written = Logger.write_to_log(output_data, columns, output_file_path)
        return log_was_written
