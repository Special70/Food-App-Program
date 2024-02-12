class ScrollBar:
    def __init__(self, length):
        self.bar = [' ' for x in range(length)]
        self.bar[0] = '►'

def arrow_scroll(obj, direction):
    if direction == "up" and obj.bar.index('►') != 0:
        obj.bar[obj.bar.index('►')], obj.bar[obj.bar.index('►')-1] = ' ', '►'
    if direction == "down" and obj.bar.index('►') != len(obj.bar)-1:
        obj.bar[obj.bar.index('►')], obj.bar[obj.bar.index('►')+1] = ' ', '►'

_001_front_menu_scroll = ScrollBar(2)
_001_front_menu = '\n'.join([f"============================",
                            f"Welcome to TastyPal!",
                            f"============================",
                            f"{_001_front_menu_scroll.bar[0]} Open",
                            f"{_001_front_menu_scroll.bar[1]} Exit"])
