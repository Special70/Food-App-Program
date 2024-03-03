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
    
class InstanceInfo: # Class object used to store values that needs to be carried over to the next UI
    def __init__(self):
        self.selected_shop = ""
        self.selected_product = []
        # Stores selected items
        self.seller_of_items = ""
        self.list_of_selected_items = []
    def get_selected_shop(self):
        return self.selected_shop
    def get_selected_product(self):
        return self.selected_product
    def get_list_of_selected_items(self):
        return self.list_of_selected_items
    def get_seller_of_items(self):
        return self.seller_of_items
    def select_shop(self, shop):
        self.selected_shop = shop
    def select_product(self, product):
        self.selected_product = [product[0], product[1]]
    def set_seller_of_items(self, shop):
        self.seller_of_items = shop
    def add_item_to_list_of_selected_items(self, item, amount):
        self.list_of_selected_items.append([item[0], item[1], amount])
        
val_container = InstanceInfo()