class LangObj:
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

_001_front_menu = LangObj(2)

_001_front_menu.set_text([f"============================",
                            f"Welcome to TastyPal!",
                            f"============================",
                            f"%0% Open",
                            f"%1% Exit"])
