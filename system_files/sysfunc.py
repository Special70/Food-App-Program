import os

# Toggle Debug Mode
debug_mode = True

# For saving text when running refres_text()
text_to_print = "None"

# Scrollbar Obj
class ScrollBar:
    def __init__(self, length=100):
        self.scroll_bar = ['►']
        self.scroll_bar.extend([' '*length])

def dbugprint(text):
    if debug_mode:
        print(text)

def refresh_text():
    os.system('cls')
    print(text_to_print)

def arrow_scroll(scroll_obj, direction):
    if direction == "up" and scroll_obj.scroll_bar.index('►') != len(scroll_obj.scroll_bar)-1:
        dbugprint("[arrow_scroll] Move arrow up")
        scroll_obj.scroll_bar[scroll_obj.scroll_bar.index('►') + 1] = '►'
        scroll_obj.scroll_bar[scroll_obj.scroll_bar.index('►')] = ' '
    if direction == "down" and scroll_obj.scroll_bar.index('►') != 0:
        dbugprint("[arrow_scroll] Move arrow down")
        scroll_obj.scroll_bar[scroll_obj.scroll_bar.index('►') - 1] = '►'
        scroll_obj.scroll_bar[scroll_obj.scroll_bar.index('►')] = ' '
    refresh_text(text_to_print)