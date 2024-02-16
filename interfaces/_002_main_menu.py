from lang import lang_obj
from os import system
#================================
from system_files.keyhit_reader import get_key_hit, reset_key_hit_val
from system_files.sysfunc import change_current_display, dbugprint
from interfaces.func import arrow_scroll

def _self():
    print(lang_obj._002_main_menu.get_text())
    while True:
        if get_key_hit():
            match(get_key_hit()):
                case "up" | "down":
                    arrow_scroll(lang_obj._002_main_menu, "selector_bar", get_key_hit())
                    system('cls')
                    dbugprint("Arrow Scroll Occured")
                    print(lang_obj._002_main_menu.get_text())
                case _:
                    if lang_obj._002_main_menu.get_selector_bar_val(0) == '►':
                        if len(get_key_hit()) == 1 or get_key_hit() == "backspace":
                            lang_obj._002_main_menu.modify_search_text(get_key_hit())
                            system('cls')
                            #dbugprint("Added inputs to search bar")
                            reset_key_hit_val()
                            print(lang_obj._002_main_menu.get_text())
        if get_key_hit() == "enter":
            if lang_obj._002_main_menu.get_selector_bar_val(1) == '►':
                change_current_display("Front Menu")
                system('cls')
                reset_key_hit_val()
                break