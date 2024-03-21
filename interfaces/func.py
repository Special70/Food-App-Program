from datetime import date
import csv

from system_files.keyhit_reader import reset_key_hit_val
from interfaces.val_storage import val_container

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
    
def record_purchase():
    target_file = 'records/purchase_records.csv'
    fieldnames = ['date','list of products','total price']
    product_list = str(val_container.get_list_of_selected_items())[1:-1].replace("], [","]\n[")
    values_to_write = {'date':date.today(),'list of products':product_list,'total price':f"{val_container.total_price_of_selected_items:.2f}"}
    
    with open(target_file, 'a') as csvfile:
        dictwriter_obj = csv.DictWriter(csvfile, fieldnames=fieldnames)
        dictwriter_obj.writerow(values_to_write)
        csvfile.close()