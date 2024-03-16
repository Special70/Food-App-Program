from os import system

from interfaces.val_storage import val_container
from lang.lang_obj import _003_select_product_menu ,_004_purchase_menu
from system_files.sysfunc import change_current_display, dbugprint
from system_files.keyhit_reader import get_key_hit, reset_key_hit_val

def _self():
    #print(val_container.get_selected_product())
    _004_purchase_menu.refresh()
    print(_004_purchase_menu.get_text())
    while True:
        if get_key_hit():
            match(get_key_hit()):
                case "up":
                    _004_purchase_menu.modify_amunt(1)
                case "down":
                    _004_purchase_menu.modify_amunt(-1)
                case "c":
                    if _004_purchase_menu.get_amount() <= 0:
                        continue
                    val_container.add_item_to_list_of_selected_items(val_container.get_selected_products(), _004_purchase_menu.get_amount())
                    val_container.set_seller_of_items(val_container.get_selected_shop())
                    change_current_display("Select Product Menu")
                    system('cls')
                    reset_key_hit_val()
                    break
                case "b":
                    change_current_display("Select Product Menu")
                    system('cls')
                    reset_key_hit_val()
                    break
            system('cls')
            print(_004_purchase_menu.get_text())
            reset_key_hit_val()