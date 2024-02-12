from threading import Thread
#===========================
from system_files.keyhit_reader import initialize_keyhit_reader
from system_files.sysfunc import current_display_ui

from interfaces import _001_front_menu

def main_program():
    while True:
        match (current_display_ui):
            case "Front Menu":
                _001_front_menu._self()

if __name__ == "__main__":

    thread1 = Thread(target=main_program)
    thread2 = Thread(target=initialize_keyhit_reader)

    thread1.start()
    thread2.start()