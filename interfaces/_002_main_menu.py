from lang import lang_obj
from os import system
#================================
from system_files.keyhit_reader import get_key_hit, reset_key_hit_val
from system_files.sysfunc import change_current_display, dbugprint
from interfaces.func import arrow_scroll, val_container

def _self():
    print(lang_obj._002_main_menu.get_text())
    while True:
        if get_key_hit():
            match(get_key_hit()):
                case "up" | "down":
                    arrow_scroll(lang_obj._002_main_menu, lang_obj._002_main_menu.get_current_scroll_column(), get_key_hit())
                    system('cls')
                    #dbugprint("Arrow Scroll Occured")
                    print(lang_obj._002_main_menu.get_text())
                case "left" | "right":
                    lang_obj._002_main_menu.change_scroll_bar(get_key_hit())
                    lang_obj._002_main_menu.change_first_index_value("set", 0)
                    system('cls')
                    print(lang_obj._002_main_menu.get_text())
                    reset_key_hit_val()
                case _:
                    if lang_obj._002_main_menu.get_side_bar(0) == '►':
                        if len(get_key_hit()) == 1 or get_key_hit() == "backspace":
                            lang_obj._002_main_menu.modify_search_text(get_key_hit())
                            system('cls')
                            #dbugprint("Added inputs to search bar")
                            reset_key_hit_val()
                            print(lang_obj._002_main_menu.get_text())
        if get_key_hit() == "enter":
            if lang_obj._002_main_menu.get_side_bar(1) == '►':
                lang_obj._002_main_menu.search_bar = ""
                change_current_display("Front Menu")
                system('cls')
                reset_key_hit_val()
                break
            if lang_obj._002_main_menu.get_side_bar(2) == '►':
                system('cls')
                if lang_obj._002_main_menu.sort_mode == "None":
                    lang_obj._002_main_menu.change_sort_mode("Name")
                elif lang_obj._002_main_menu.sort_mode == "Name":
                    lang_obj._002_main_menu.change_sort_mode("None")
                print(lang_obj._002_main_menu.get_text())
                reset_key_hit_val()
            if lang_obj._002_main_menu.get_side_bar(3) == '►':
                system('cls')
                lang_obj._002_main_menu.set_values_to_display("Shops")
                print(lang_obj._002_main_menu.get_text())
                reset_key_hit_val()
            if lang_obj._002_main_menu.get_side_bar(4) == '►':
                system('cls')
                lang_obj._002_main_menu.set_values_to_display("Products")
                print(lang_obj._002_main_menu.get_text())
                reset_key_hit_val()
            if lang_obj._002_main_menu.get_current_scroll_column() == "selector_bar":
                if lang_obj._002_main_menu.get_what_values_displayed() == "Shops":
                    lang_obj._002_main_menu.search_bar = ""
                    change_current_display("Select Product Menu")
                    system('cls')
                    val_container.select_shop(lang_obj._002_main_menu.import_displayed_values()[lang_obj._002_main_menu.selector_bar.index('►')+lang_obj._002_main_menu.first_index_display])
                    reset_key_hit_val()
                    break