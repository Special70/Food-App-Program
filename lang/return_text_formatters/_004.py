from interfaces.val_storage import val_container

def _self(self):
    text_to_print = self.text
    selected_product = val_container.get_selected_product()
    
    text_to_print = text_to_print.replace("%product%", str(selected_product[0])+" ($"+str(selected_product[1]+")"))
    total_amount = float(selected_product[1])*self.get_amount()
    text_to_print = text_to_print.replace("%amount%", str(self.get_amount())+" "*(15-len(str(self.get_amount()))))
    text_to_print = text_to_print.replace("%confirm%", " C : Confirm" if self.get_amount() > 0 else "")
    text_to_print = text_to_print.replace("%total_amount%", f"{total_amount:.2f}")
    return text_to_print