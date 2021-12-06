"""Main"""
from data_manager.observer import FileObserver

def main():
    """Main"""
    print("Calculator is running...")

    # if __name__ == "main":
    file_observer = FileObserver()
    file_observer.run()

main()
