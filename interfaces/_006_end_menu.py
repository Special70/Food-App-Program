from os import system

from lang.lang_obj import _006_end_menu
from system_files.keyhit_reader import get_key_hit, reset_key_hit_val
from system_files.sysfunc import change_current_display
from interfaces.val_storage import val_container

def _self():
    print(_006_end_menu.get_text())
    while True:
        if get_key_hit():
            match (get_key_hit().lower()):
                case "y":
                    change_current_display(val_container.get_previous_menu())
                    system('cls')
                    reset_key_hit_val()
                    break
                case "n":
                    change_current_display("Null")
                    system('cls')
                    reset_key_hit_val()
                    break