from lang import locale_EN as lang_text
from system_files.food_data_reader import get_info

class RegularUI_Format:
    def __repr__(self):
        return "RegularUI_Format"
    def __init__(self, length):
        self.bar = ['►']+[' ']*(length-1)
        self.text = None
    def get_val(self, targetIndex):
        return self.bar[targetIndex]
    def set_text(self, stringVal):
        self.text = '\n'.join(stringVal)
    def get_text(self):
        text_to_print = self.text
        for i in range(len(self.bar)):
            replace_text = "%"+str(i)+"%"
            text_to_print = text_to_print.replace(replace_text, self.get_val(i))
        return text_to_print

_001_front_menu = RegularUI_Format(2)
_001_front_menu.set_text(lang_text._001_front_menu)

class SelectorMenuUI_Format:
    def __repr__(self):
        return "SelectorMenuUI_Format"
    def __init__(self, bar_length=5):
        self.side_bar = ['►']+[' ']*(bar_length-1)
        self.selector_bar = [' ']+[' ']*(6)
        self.selector_bar_length = 0
        self.text = ""
        self.search_bar = ""
        self.sort_mode = "None"
        self.display_values = "Products"
        self.scroll_column = "left"
        
        self.first_index_display = 0
        self.selector_display_length = 7 # Hard-Coded Value
        self.selector_possible_displays = 0

    def get_side_bar(self, targetIndex): # Get left sliding array values
        return self.side_bar[targetIndex]
    def get_selector_bar(self, targetIndex): # Get right sliding array values
        return self.selector_bar[targetIndex]
    def get_selector_bar_length(self): # Get right sliding supposed length
        return self.selector_bar_length
    def get_search_bar_value(self):
        return self.search_bar
    def get_data_list(self, datatype="keys"): # Get data values for display usage
        data_info = get_info(datatype)
        return data_info
    def get_current_scroll_bar(self): # Get which scroll bar is being used currently
        if '►' in self.side_bar:
            return "side_bar"
        if '►' in self.selector_bar:
            return "selector_bar"
    def get_text(self):
        text_to_print = self.text
        
        # Get Specified Data
        data_to_display = []
        text_to_display = []
        if self.display_values == "Shops":
            data_list = self.get_data_list()
        elif self.display_values == "Products":
            data_list = self.get_data_list("products")
        
        # Filter Data based on search bar input
        if len(self.search_bar) > 0:
            data_list = [element for element in data_list if self.get_search_bar_value().lower() in element.lower()]
        
        # If Name Sort Enabled:
        if self.sort_mode == "Name":
            data_to_display = sorted(data_list)
        else:
            data_to_display = data_list
        
        # Add values to display array
        for i in range(len(data_to_display)):
            text_to_display.append(data_to_display[i+self.first_index_display])
            if len(text_to_display) >= 7:
                break
        self.set_selector_bar_length(len(data_to_display))
        # Writing placeholders
        for i in range(len(self.side_bar)): 
            text_to_print = text_to_print.replace("%side"+str(i)+"%", self.get_side_bar(i))

        for i in range(len(self.selector_bar)): 
            text_to_print = text_to_print.replace("%selector"+str(i)+"%", self.get_selector_bar(i))
        
        for i in range(len(text_to_display)):
            text_to_print = text_to_print.replace("%line"+str(i)+"%", text_to_display[i])
        
        text_to_print = text_to_print.replace("%text%", self.search_bar)
        
        text_to_print = text_to_print.replace("%up_arrow%", '▲' if self.first_index_display > 0 else "")
        text_to_print = text_to_print.replace("%down_arrow%", '▼' if self.first_index_display+7 < len(data_to_display) else "")
        text_to_print = text_to_print.replace("%possible_results_text%","Possible Results : "+str(self.get_selector_bar_length()))
        text_to_print = text_to_print.replace("%namesort%", "←" if self.sort_mode == "Name" else " ")
        # Searchbar Guide
        textguide = ""
        if self.side_bar[0] == '►':
            textguide = "Hit Characters to type. Hit Backspace to press delete" 
        elif self.side_bar[1] == '►':
            textguide = "Hit ENTER to go back"
        elif self.side_bar[2] == '►':
            textguide = "Hit ENTER to toggle Name-Sorting Mode"
        elif self.side_bar[3] == '►':
            textguide = "Hit ENTER to view available shops"
        elif self.side_bar[4] == '►':
            textguide = "Hit ENTER to view available products across shops"
        text_to_print = text_to_print.replace("%searchbar_guide%", textguide)
        # Blanking unused placeholders:
        for i in range(7):
            text_to_print = text_to_print.replace("%line"+str(i)+"%", "")
        # =======================================================================
        self.set_number_of_values_displayed(len(data_to_display))
        
        return text_to_print
    
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
    def set_selector_bar_length(self, length): # ( Mainly used by self.get_text() ) to change the supposed length to let the rest of the code know the supposed length
        self.selector_bar_length = length
    def set_text(self, stringVal): # Set Text
        self.text = '\n'.join(stringVal)
    def set_values_to_display(self, saidVal="Shops"): # Set what values to show ( Refer to food_data_reader.py )
        self.display_values = saidVal
    def set_number_of_values_displayed(self, value): # Sets the value of self.selector_possible_displays to know how many items are displayed
        self.selector_possible_displays = value
        
_002_main_menu = SelectorMenuUI_Format()
_002_main_menu.set_text(lang_text._002_main_menu)