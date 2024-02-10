import threading

from system_files.sysfunc import dbugprint

from system_files import keypress_reader
from system_files import system_status
from language_files import locale_EN as lang

from interfaces import _001_front_menu

# START OF MAIN CODE
def main_program():
    while system_status.isRunning:
        match (system_status.page):
            case "Main Menu":
                dbugprint("Main Menu")
                _001_front_menu.self()
                

thread1 = threading.Thread(target=keypress_reader.initialize_keypress_reader)
thread2 = threading.Thread(target=main_program)

thread1.start()
thread2.start()

thread1.join()
thread2.join()