from os import system
from time import sleep

from system_files.sysfunc import is_program_running, dbugprint
from system_files.keyhit_reader import key_hit, get_key_hit, reset_key_hit_val

from lang import locale_EN as langFile
from interfaces.func import arrow_scroll

def _self():
    print(langFile._001_front_menu.get_text())
    while is_program_running:
        print(langFile._001_front_menu.bar)
        if get_key_hit() == "up":
            arrow_scroll(langFile._001_front_menu, "up")
            #dbugprint("Arrow Scroll UP")
            system('cls')
            print(langFile._001_front_menu)
        if get_key_hit() == "down":
            arrow_scroll(langFile._001_front_menu, "down")
            #dbugprint("Arrow Scroll UP")
            system('cls')
            print(langFile._001_front_menu.get_text())
        sleep(0.5)