class LangObj:
    def __init__(self, length):
        self.bar = ['►']+[' ']*(length-1)
        self.text = None
    def get_val(self, targetIndex):
        return self.bar[targetIndex]
    def set_text(self, stringVal):
        self.text = stringVal
    def get_text(self):
        return '\n'.join(self.text)

_001_front_menu = LangObj(2)

_001_front_menu.set_text([f"============================",
                            f"Welcome to TastyPal!",
                            f"============================",
                            f"{_001_front_menu.bar[0]} Open",
                            f"{_001_front_menu.bar[1]} Exit"])
