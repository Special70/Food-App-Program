from lang import locale_EN as lang_text
from system_files.food_data_reader import get_info
from system_files.sysfunc import dbugprint
from lang.return_text_formatters import _002, _003, _004, _005
from interfaces.val_storage import val_container

class RegularUI_Format:
    def __repr__(self):
        return "RegularUI_Format"
    def __init__(self, length):
        self.bar = ['►']+[' ']*(length-1)
        self.text = None
    def get_val(self, targetIndex):
        return self.bar[targetIndex]
    def get_text(self):
        text_to_print = self.text
        for i in range(len(self.bar)):
            replace_text = "%"+str(i)+"%"
            text_to_print = text_to_print.replace(replace_text, self.get_val(i))
        return text_to_print
    def set_text(self, stringVal):
        self.text = '\n'.join(stringVal)

_001_front_menu = RegularUI_Format(2)
_001_front_menu.set_text(lang_text._001_front_menu)

# ============================================================================================
# ============================================================================================
# ============================================================================================

class SelectorMenuUI_Format:
    def __repr__(self):
        return "SelectorMenuUI_Format" 
    def __init__(self, bar_length=5, name=""):
        self.obj_name = name # Used to specify what UI is using this class

        self.side_bar = ['►']+[' ']*(bar_length-1)
        self.selector_bar = [' ']+[' ']*(6)
        self.selector_bar_length = 0
        self.text = ""
        self.search_bar = ""
        self.sort_mode = "None"
        self.display_values = "Shops"
        self.scroll_column = "selector_bar"
        
        self.first_index_display = 0
        self.selector_display_length = 7 # Hard-Coded Value
        self.selector_possible_displays = 0
        
        self.displayed_values = []
        
    def refresh_default_values(self):
        if '►' in self.side_bar:
            self.side_bar[self.side_bar.index('►')] = ' '
        if '►' in self.selector_bar:    
            self.selector_bar[self.selector_bar.index('►')] = ' '
        self.side_bar[0] = '►'
        self.selector_bar_length = 0
        self.search_bar = ""
        self.sort_mode = "None"
        self.display_values = "Shops"
        self.scroll_column = "selector_bar"
        
        self.first_index_display = 0
        self.selector_display_length = 7 # Hard-Coded Value
        self.selector_possible_displays = 0
        
        self.displayed_values = []
    def get_what_values_displayed(self): # Get what values are displayed
        return self.display_values
    def get_side_bar(self, targetIndex): # Get left sliding array values
        return self.side_bar[targetIndex]
    def get_selector_bar(self, targetIndex): # Get right sliding array values
        return self.selector_bar[targetIndex]
    def get_selector_bar_length(self): # Get right sliding supposed length
        return self.selector_bar_length
    def get_search_bar_value(self): # Get the string written at the search bar
        return self.search_bar
    def get_data_list(self, datatype="keys"): # Get data values for display usage
        data_info = get_info(datatype)
        return data_info
    def get_current_scroll_column(self): # Get which scroll bar is being used currently
        if '►' in self.side_bar:
            return "side_bar"
        if '►' in self.selector_bar:
            return "selector_bar"
    def get_text(self, arg0=""):
        if self.obj_name == "_002_main_menu":
            return _002._self(self)
        if self.obj_name == "_003_select_product_menu":
            return _003._self(self)
        if self.obj_name == "_005_confirm_purchase_menu":
            return _005._self(self, scroll_direction=arg0)
    
    # Modification Methods ============================================================================================================================================
    # Modification Methods ============================================================================================================================================
    # Modification Methods ============================================================================================================================================
    
    def modify_search_text(self, keyhit): # Modify search bar via keypresses
        self.change_first_index_value("set", 0)
        if keyhit == "backspace" and len(self.search_bar) > 0:
            self.search_bar = self.search_bar[:-1]
        elif keyhit != "backspace" and len(keyhit) == 1:
            self.search_bar += keyhit
    def change_sort_mode(self, mode): # Change sort mode
        self.sort_mode = mode
    def change_scroll_bar(self, side): # Change which scrollbar to use
        if '►' in self.selector_bar and side == "left":
            self.selector_bar[self.selector_bar.index('►')] = " "
            self.side_bar[1] = '►'
            self.scroll_column = "side_bar"
        elif '►' in self.side_bar and side == "right":
            self.side_bar[self.side_bar.index('►')] = " "
            self.selector_bar[0] = '►'
            self.scroll_column = "selector_bar"
    def change_first_index_value(self, modification, value):
        if modification == "change":
            self.first_index_display += value
        elif modification == "set":
            self.first_index_display = value
    def export_displayed_values(self, values):
        self.displayed_values = values
    def import_displayed_values(self):
        return self.displayed_values
    def set_selector_bar_length(self, length): # ( Mainly used by self.get_text() ) to change the supposed length to let the rest of the code know the supposed length
        self.selector_bar_length = length
    def set_text(self, stringVal): # Set Text
        self.text = '\n'.join(stringVal)
    def set_values_to_display(self, saidVal="Shops"): # Set what values to show ( Refer to food_data_reader.py )
        self.display_values = saidVal
    def set_number_of_values_displayed(self, value): # Sets the value of self.selector_possible_displays to know how many items are displayed
        self.selector_possible_displays = value
        
_002_main_menu = SelectorMenuUI_Format(name="_002_main_menu", bar_length=5)
_002_main_menu.set_text(lang_text._002_main_menu)

# ============================================================================================
# ============================================================================================
# ============================================================================================

_003_select_product_menu = SelectorMenuUI_Format(name="_003_select_product_menu", bar_length=4)
_003_select_product_menu.set_text(lang_text._003_select_product_menu)

# ============================================================================================
# ============================================================================================
# ============================================================================================

class PurchaseMenuUI_Format:
    def __init__(self):
        self.text = ""
        self.selected_product = [] # Name, Price
        self.selected_shop = ""
    def refresh(self):
        self.amount = 0
    def set_text(self, value):
        self.text = '\n'.join(value)
    def modify_amunt(self, value):
        if self.selected_product[2]+value >= 0:
            self.selected_product[2] += value
    def get_text(self):
        return _004._self(self)
    def get_amount(self):
        return self.amount
    def get_selected_product(self):
        index = 0
        for item in val_container.get_list_of_selected_items():
            if _004_purchase_menu.selected_product[0] == item[0]:
                _004_purchase_menu.selected_product[2] = item[2]
                val_container.list_of_selected_items.remove(item)
                break
            index += 1
        return self.selected_product
    

_004_purchase_menu = PurchaseMenuUI_Format()
_004_purchase_menu.set_text(lang_text._004_purchase_menu)

_005_confirm_purchase_menu = SelectorMenuUI_Format(name="_005_confirm_purchase_menu")
_005_confirm_purchase_menu.set_text(lang_text._005_confirm_purchase_menu)
_005_confirm_purchase_menu.current_index = 0

class SimpleUI_Format:
    def __init__(self):
        self.text = ""
    def set_text(self, value):
        self.text = '\n'.join(value)
    def get_text(self):
        return self.text

_006_end_menu = SimpleUI_Format()
_006_end_menu.set_text(lang_text._006_end_menu)