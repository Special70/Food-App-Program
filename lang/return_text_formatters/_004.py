from interfaces.val_storage import val_container

def _self(self):
    text_to_print = self.text
    
    text_to_print = text_to_print.replace("%product%", str(self.get_selected_product()[0])+" ($"+str(self.get_selected_product()[1])+")")
    total_amount = float(self.get_selected_product()[1])*self.get_selected_product()[2]
    text_to_print = text_to_print.replace("%amount%", str(self.get_selected_product()[2])+" "*(15-len(str(self.get_selected_product()[2]))))
    text_to_print = text_to_print.replace("%confirm%", " ENTER : Confirm" if self.get_selected_product()[2] > 0 else "")
    text_to_print = text_to_print.replace("%total_amount%", f"{total_amount:.2f}")
    return text_to_print