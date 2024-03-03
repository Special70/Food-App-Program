from os import system

from interfaces.func import val_container
from lang.lang_obj import _003_select_product_menu
from system_files.keyhit_reader import get_key_hit, reset_key_hit_val
from system_files.sysfunc import change_current_display, dbugprint
from interfaces.func import arrow_scroll, val_container

def _self():
    #print("Selected Shop:",val_container.get_selected_shop())
    _003_select_product_menu.refresh_default_values()
    print(_003_select_product_menu.get_text())
    while True:
        if get_key_hit():
            match(get_key_hit()):
                case "up" | "down":
                    arrow_scroll(_003_select_product_menu, _003_select_product_menu.get_current_scroll_column(), get_key_hit())
                    system('cls')
                    #dbugprint("Arrow Scroll Occured")
                    print(_003_select_product_menu.get_text())
                case "left" | "right":
                    _003_select_product_menu.change_scroll_bar(get_key_hit())
                    _003_select_product_menu.change_first_index_value("set", 0)
                    system('cls')
                    print(_003_select_product_menu.get_text())
                    reset_key_hit_val()
                case _:
                    if _003_select_product_menu.get_side_bar(0) == '►':
                        if len(get_key_hit()) == 1 or get_key_hit() == "backspace":
                            _003_select_product_menu.modify_search_text(get_key_hit())
                            system('cls')
                            #dbugprint("Added inputs to search bar")
                            reset_key_hit_val()
                            print(_003_select_product_menu.get_text())
        if get_key_hit() == "enter":
            if _003_select_product_menu.get_side_bar(1) == '►':
                _003_select_product_menu.search_bar = ""
                change_current_display("Main Menu")
                system('cls')
                reset_key_hit_val()
                break
            if _003_select_product_menu.get_side_bar(2) == '►':
                system('cls')
                if _003_select_product_menu.sort_mode == "None":
                    _003_select_product_menu.change_sort_mode("Name")
                elif _003_select_product_menu.sort_mode == "Name":
                    _003_select_product_menu.change_sort_mode("None")
                print(_003_select_product_menu.get_text())
                reset_key_hit_val()
            if _003_select_product_menu.get_current_scroll_column() == "selector_bar":
                _003_select_product_menu.search_bar = ""
                val_container.select_product(_003_select_product_menu.import_displayed_values()[_003_select_product_menu.selector_bar.index('►')+_003_select_product_menu.first_index_display])
                change_current_display("Purchase Product Menu")
                system('cls')
                reset_key_hit_val()
                break