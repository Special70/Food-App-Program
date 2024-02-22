from threading import Thread
from os import system
from time import sleep
#===========================
from system_files.keyhit_reader import initialize_keyhit_reader
from system_files.sysfunc import get_current_display, get_program_status, dbugprint

from interfaces import _001_front_menu, _002_main_menu, _003_select_product_menu

def main_program():
    while get_program_status():
        dbugprint("While LOOP Run")
        system('cls')
        
        match (get_current_display()):
            case "Front Menu":
                _001_front_menu._self()
            case "Main Menu":
                _002_main_menu._self()
            case "Select Product Menu":
                _003_select_product_menu._self()
            case _:
                dbugprint("INVALID MENU SELECTION")
            

if __name__ == "__main__":

    thread1 = Thread(target=main_program)
    thread2 = Thread(target=initialize_keyhit_reader)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    dbugprint("[!] Program has ended [!]")