from lang import locale_EN as lang_text

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
        self.selector_bar = ['►']+[' ']*(bar_length-1)
        self.text = ""
        self.search_bar = ""
    def get_selector_bar_val(self, targetIndex):
        return self.selector_bar[targetIndex]
    def set_text(self, stringVal):
        self.text = '\n'.join(stringVal)
    def get_text(self):
        text_to_print = self.text
        for i in range(len(self.selector_bar)): # Writing placeholders
            text_to_print = text_to_print.replace("%side"+str(i)+"%", self.get_selector_bar_val(i))
        text_to_print = text_to_print.replace("%text%", self.search_bar)
        if self.get_selector_bar_val(0) == '►':
            text_to_print = text_to_print.replace("%searchbar_guide%", "Type characters to type. Hit Backspace to remove characters")
        else:
            text_to_print = text_to_print.replace("%searchbar_guide%", "")
        return text_to_print
    def modify_search_text(self, keyhit):
        if keyhit == "backspace" and len(self.search_bar) > 0:
            self.search_bar = self.search_bar[:-1]
        elif keyhit != "backspace" and len(keyhit) == 1:
            self.search_bar += keyhit
        
_002_main_menu = SelectorMenuUI_Format()
_002_main_menu.set_text(lang_text._002_main_menu)