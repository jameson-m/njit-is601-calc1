"""Testing the Logger class."""
import time
from logger.logger import Logger

def test_set_input_file_name():
    """Tests setting the input file name for Logger.
    """
    Logger.set_input_file_name("hello, world!")
    assert Logger.input_file_name == "hello, world!"
    Logger.set_input_file_name("")

def test_get_unix_timestamp():
    """Tests unix timestamp.
    """
    current_time = int(time.time())
    timestamp = Logger.get_unix_timestamp()
    assert timestamp >= current_time

def test_get_record_number():
    """Tests get record number.
    """
    record_number = Logger.get_record_number()
    assert isinstance(record_number, str)
