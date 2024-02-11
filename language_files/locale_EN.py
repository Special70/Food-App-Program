# Main Page (Section 001)
from interfaces import _001_front_menu

lang001_main = '\n'.join([
    f"-----------------------------",
    f"Welcome to TastyPal!",
    f"",
    f"{_001_front_menu.scroll_list.scroll_bar[0]} Open",
    f"{_001_front_menu.scroll_list.scroll_bar[1]} Exit",
    f"-----------------------------"
])