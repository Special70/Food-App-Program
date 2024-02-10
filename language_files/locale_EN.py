# Main Page (Section 001)
from interfaces import _001_front_menu

lang001_main = '\n'.join([
    f"-----------------------------",
    f"Welcome to TastyPal!",
    f"",
    f"{_001_front_menu.selector[0]} Open",
    f"{_001_front_menu.selector[1]} Exit",
    f"-----------------------------"
])