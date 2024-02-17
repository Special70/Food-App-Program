from lang import locale_EN as lang_text
from system_files.food_data_reader import get_info

class RegularUI_Format:
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
    def __init__(self, bar_length=7):
        self.side_bar = ['►']+[' ']*(bar_length-1)
        self.selector_bar = [' ']+[' ']*(9)
        self.text = ""
        self.search_bar = ""
        self.sort_mode = "None"
    def get_side_bar(self, targetIndex):
        return self.side_bar[targetIndex]
    def get_selector_bar(self, targetIndex):
        return self.selector_bar[targetIndex]
    def set_text(self, stringVal):
        self.text = '\n'.join(stringVal)
    def get_text(self):
        text_to_print = self.text
        for i in range(len(self.side_bar)): # Writing placeholders
            text_to_print = text_to_print.replace("%side"+str(i)+"%", self.get_side_bar(i))
        text_to_print = text_to_print.replace("%text%", self.search_bar)

        for i in range(len(self.selector_bar)): 
            text_to_print = text_to_print.replace("%selector"+str(i)+"%", self.get_selector_bar(i))
        text_to_print = text_to_print.replace("%text%", self.search_bar)

        if self.get_side_bar(0) == '►': # If the arrow is pointing at the search bar
            text_to_print = text_to_print.replace("%searchbar_guide%", "Type characters to type. Hit Backspace to remove characters")
        else:
            text_to_print = text_to_print.replace("%searchbar_guide%", "")

        data_list = self.assemble_list()
        
        data_list_iteration = 0
        match (self.sort_mode):
            case "None":
                for iteration in data_list:
                    text_to_print = text_to_print.replace("%line"+str(data_list_iteration)+"%", iteration)
                    data_list_iteration += 1
            case "Name":
                pass

        return text_to_print
    def modify_search_text(self, keyhit):
        if keyhit == "backspace" and len(self.search_bar) > 0:
            self.search_bar = self.search_bar[:-1]
        elif keyhit != "backspace" and len(keyhit) == 1:
            self.search_bar += keyhit
    def assemble_list(self):
        data_info = get_info()
        return data_info
    
        
_002_main_menu = SelectorMenuUI_Format()
_002_main_menu.set_text(lang_text._002_main_menu)