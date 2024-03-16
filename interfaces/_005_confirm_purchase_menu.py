from os import system

from lang.lang_obj import _005_confirm_purchase_menu
from system_files.keyhit_reader import get_key_hit, reset_key_hit_val
from system_files.sysfunc import change_current_display, dbugprint
from interfaces.val_storage import val_container
from interfaces.func import arrow_scroll

def _self():
    print(_005_confirm_purchase_menu.get_text())
    while True:
        if get_key_hit():
            match (get_key_hit().lower()):
                case "y":
                    change_current_display("Final Menu")
                    system('cls')
                    reset_key_hit_val()
                    break
                case "n":
                    change_current_display(val_container.get_previous_menu())
                    system('cls')
                    reset_key_hit_val()
                    break
                case "up" | "down":
                    #dbugprint("Arrow Scroll Occured")
                    print(_005_confirm_purchase_menu.get_text(get_key_hit()))
                    system('cls')
                    reset_key_hit_val()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    