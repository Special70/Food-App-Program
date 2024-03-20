
class InstanceInfo: # Class object used to store values that needs to be carried over to the next UI
    def __init__(self):
        # Stores selected items
        self.seller_of_items = ""
        self.list_of_selected_items = [] # Format: [[Name, Price, Amount]]
        # Store previous menu
        self.previous_menu = ""
        self.selected_shop = ""
    def get_selected_shop(self):
        return self.selected_shop
    def get_list_of_selected_items(self):
        return self.list_of_selected_items
    def get_seller_of_items(self):
        return self.seller_of_items
    def get_previous_menu(self):
        return self.previous_menu
    
    def select_shop(self, shop):
        self.selected_shop = shop
    def select_product(self, product, amount=0):
        self.selected_product = [product[0], product[1], amount]
    def set_seller_of_items(self, shop):
        self.seller_of_items = shop
    def set_previous_menu(self, name):
        self.previous_menu = name
        
    def add_item_to_list_of_selected_items(self, item): # item arg contains the list of product, price, amount
        self.list_of_selected_items.append([item[0], item[1], item[2]])
        
val_container = InstanceInfo()