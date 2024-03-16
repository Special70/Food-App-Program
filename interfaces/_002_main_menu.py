from os import system
#================================
from lang.lang_obj import _002_main_menu
from system_files.keyhit_reader import get_key_hit, reset_key_hit_val
from system_files.sysfunc import change_current_display, dbugprint
from interfaces.func import arrow_scroll
from interfaces.val_storage import val_container

def _self():
    _002_main_menu.refresh_default_values()
    print(_002_main_menu.get_text())
    while True:
        if get_key_hit():
            match(get_key_hit()):
                case "up" | "down":
                    arrow_scroll(_002_main_menu, _002_main_menu.get_current_scroll_column(), get_key_hit())
                    system('cls')
                    #dbugprint("Arrow Scroll Occured")
                    print(_002_main_menu.get_text())
                case "left" | "right":
                    _002_main_menu.change_scroll_bar(get_key_hit())
                    _002_main_menu.change_first_index_value("set", 0)
                    system('cls')
                    print(_002_main_menu.get_text())
                    reset_key_hit_val()
                case "V":
                    if val_container.get_list_of_selected_items():
                        change_current_display("Purchase Finalization Menu")
                        val_container.set_previous_menu("Main Menu")
                        system('cls')
                        reset_key_hit_val()
                        break
                case _:
                    if _002_main_menu.get_side_bar(0) == '►':
                        if len(get_key_hit()) == 1 or get_key_hit() == "backspace":
                            _002_main_menu.modify_search_text(get_key_hit())
                            system('cls')
                            #dbugprint("Added inputs to search bar")
                            reset_key_hit_val()
                            print(_002_main_menu.get_text())
        if get_key_hit() == "enter":
            if _002_main_menu.get_side_bar(1) == '►':
                _002_main_menu.search_bar = ""
                change_current_display("Front Menu")
                system('cls')
                reset_key_hit_val()
                break
            if _002_main_menu.get_side_bar(2) == '►':
                system('cls')
                if _002_main_menu.sort_mode != "Name":
                    _002_main_menu.change_sort_mode("Name")
                elif _002_main_menu.sort_mode == "Name":
                    _002_main_menu.change_sort_mode("None")
                print(_002_main_menu.get_text())
                reset_key_hit_val()
            if _002_main_menu.get_side_bar(3) == '►':
                system('cls')
                _002_main_menu.set_values_to_display("Shops")
                print(_002_main_menu.get_text())
                reset_key_hit_val()
            if _002_main_menu.get_side_bar(4) == '►':
                system('cls')
                _002_main_menu.set_values_to_display("Products")
                print(_002_main_menu.get_text())
                reset_key_hit_val()
            if _002_main_menu.get_current_scroll_column() == "selector_bar":
                if _002_main_menu.get_what_values_displayed() == "Shops":
                    _002_main_menu.search_bar = ""
                    change_current_display("Select Product Menu")
                    system('cls')
                    val_container.select_shop(_002_main_menu.import_displayed_values()[_002_main_menu.selector_bar.index('►')+_002_main_menu.first_index_display])
                    reset_key_hit_val()
                    break