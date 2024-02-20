from system_files.keyhit_reader import reset_key_hit_val
from system_files.sysfunc import dbugprint
from time import sleep

def arrow_scroll(obj, attribute, direction):
    if direction == "up":
        if getattr(obj, attribute).index('►') != 0:
            arrow_index = getattr(obj, attribute).index('►')
            if str(obj) == "SelectorMenuUI_Format":
                if arrow_index == 0 and obj.get_current_scroll_bar() == "selector_bar":
                    obj.change_first_index_value("change", -1)
                    print("a")
                else:
                    getattr(obj, attribute)[arrow_index], getattr(obj, attribute)[arrow_index-1] = ' ','►'
                '''elif arrow_index != 0 and obj.get_current_scroll_bar() == "selector_bar":
                    getattr(obj, attribute)[arrow_index], getattr(obj, attribute)[arrow_index-1] = ' ','►'
                    print("b")'''
            else:
                getattr(obj, attribute)[arrow_index], getattr(obj, attribute)[arrow_index-1] = ' ','►'
                print("c")
        
    if direction == "down":
        if getattr(obj, attribute).index('►') != len(getattr(obj, attribute))-1:
            arrow_index = getattr(obj, attribute).index('►')
            if str(obj) == "SelectorMenuUI_Format": 
                if arrow_index == obj.selector_display_length-1 and obj.get_current_scroll_bar() == "selector_bar" and obj.first_index_display+7 < obj.get_selector_bar_length():
                    obj.change_first_index_value("change", 1)
                elif arrow_index < obj.get_selector_bar_length()-1 and obj.get_current_scroll_bar() == "selector_bar" and obj.first_index_display+7 < obj.get_selector_bar_length():
                    getattr(obj, attribute)[arrow_index], getattr(obj, attribute)[arrow_index+1] = ' ','►'
                else:
                    pass
            else:
                getattr(obj, attribute)[arrow_index], getattr(obj, attribute)[arrow_index+1] = ' ','►'
    reset_key_hit_val()
    sleep(1)
    