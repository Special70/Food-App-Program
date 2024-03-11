from system_files.keyhit_reader import reset_key_hit_val
from system_files.sysfunc import dbugprint
from time import sleep

def arrow_scroll(obj, attribute, direction):
    arrow_index = getattr(obj, attribute).index('►')
    
    if direction == "up":
        if str(obj) == "RegularUI_Format":
            if arrow_index != 0:
                getattr(obj, attribute)[arrow_index], getattr(obj, attribute)[arrow_index-1] = ' ','►'
        elif str(obj) == "SelectorMenuUI_Format":
            if getattr(obj, attribute).index('►') == 0 and obj.first_index_display > 0 and obj.get_current_scroll_column() == "selector_bar" :
                obj.change_first_index_value("change", -1)
            elif getattr(obj, attribute).index('►') != 0:
                getattr(obj, attribute)[arrow_index], getattr(obj, attribute)[arrow_index-1] = ' ','►'
            
        
    if direction == "down":
        if str(obj) == "RegularUI_Format":
            if getattr(obj, attribute).index('►') != len(obj.bar)-1:
                getattr(obj, attribute)[arrow_index], getattr(obj, attribute)[arrow_index+1] = ' ','►'
        elif str(obj) == "SelectorMenuUI_Format":
            if getattr(obj, attribute).index('►') == obj.selector_display_length-1 and obj.get_current_scroll_column() == "selector_bar" and obj.first_index_display+7 < obj.get_selector_bar_length():
                obj.change_first_index_value("change", 1)
            elif getattr(obj, attribute).index('►') < obj.get_selector_bar_length()-1 and obj.get_current_scroll_column() == "selector_bar" and obj.first_index_display+getattr(obj, attribute).index('►') < obj.get_selector_bar_length()-1:
                getattr(obj, attribute)[arrow_index], getattr(obj, attribute)[arrow_index+1] = ' ','►'
            elif getattr(obj, attribute).index('►') != len(getattr(obj, attribute))-1 and obj.get_current_scroll_column() == "side_bar":
                getattr(obj, attribute)[arrow_index], getattr(obj, attribute)[arrow_index+1] = ' ','►'
    reset_key_hit_val()
    #sleep(1)
    