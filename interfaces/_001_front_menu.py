from language_files import locale_EN as lang
from system_files.sysfunc import arrow_scroll, refresh_text, ScrollBar


scroll_list = ScrollBar(2)

def self():
    global scroll_list
    global text_to_print
    text_to_print = lang.lang001_main
    refresh_text()
    while True:
        pass