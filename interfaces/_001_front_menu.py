from os import system

from system_files.sysfunc import is_program_running, dbugprint, kill_program, change_current_display
from system_files.keyhit_reader import get_key_hit, reset_key_hit_val

from lang import lang_obj as langFile
from interfaces.func import arrow_scroll

def _self():
    print(langFile._001_front_menu.get_text())
    while is_program_running:
        if get_key_hit() == "up":
            arrow_scroll(langFile._001_front_menu, "bar", "up")
            #dbugprint("Arrow Scroll UP")
            system('cls')
            print(langFile._001_front_menu.get_text())
        if get_key_hit() == "down":
            arrow_scroll(langFile._001_front_menu, "bar", "down")
            #dbugprint("Arrow Scroll UP")
            system('cls')
            print(langFile._001_front_menu.get_text())
        if get_key_hit() == "enter":
            if langFile._001_front_menu.get_val(1) == '►': # Exit Program
                kill_program()
                reset_key_hit_val()
                break
            if langFile._001_front_menu.get_val(0) == '►':
                # Insert next UI page
                change_current_display("Main Menu")
                reset_key_hit_val()
                break
            