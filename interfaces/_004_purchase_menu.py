from os import system

from interfaces.val_storage import val_container
from lang.lang_obj import _004_purchase_menu
from system_files.sysfunc import change_current_display, dbugprint
from system_files.keyhit_reader import get_key_hit, reset_key_hit_val

def check_for_product(): # Checks if the selected product exists in the list of products
    for index in range(len(val_container.list_of_selected_items)):
        if _004_purchase_menu.selected_product[0] == val_container.list_of_selected_items[index][0]:
            _004_purchase_menu.selected_product[2] = val_container.list_of_selected_items[index][2] # Replaces the amount value with the saved value
            val_container.list_of_selected_items.pop(index) # Removes the item from the list
    return 0

def _self():
    _004_purchase_menu.refresh()
    print(_004_purchase_menu.get_text())
    while True:
        if get_key_hit():
            match(get_key_hit()):
                case "up":
                    _004_purchase_menu.modify_amunt(1)
                case "down":
                    _004_purchase_menu.modify_amunt(-1)
                case "enter":
                    if _004_purchase_menu.selected_product[2] <= 0:
                        continue
                    val_container.add_item_to_list_of_selected_items(_004_purchase_menu.selected_product)
                    val_container.set_seller_of_items(val_container.get_selected_shop())
                    change_current_display("Select Product Menu")
                    system('cls')
                    reset_key_hit_val()
                    break
                case "backspace":
                    change_current_display("Select Product Menu")
                    system('cls')
                    reset_key_hit_val()
                    if _004_purchase_menu.selected_product[2] > 0:
                        val_container.add_item_to_list_of_selected_items(_004_purchase_menu.selected_product)
                    if len(val_container.get_list_of_selected_items()) == 0:
                        val_container.set_seller_of_items("")
                    break
            system('cls')
            print(_004_purchase_menu.get_text())
            reset_key_hit_val()