from interfaces.val_storage import val_container
from system_files.algorithms.quicksort import algorithm as quicksort
from system_files.sysfunc import dbugprint

def _self(obj):
    text_to_print = obj.text
        
    # Get Specified Data
    data_to_display = []
    text_to_display = []
    if obj.display_values == "Shops":
        data_list = obj.get_data_list()
    elif obj.display_values == "Products":
        data_list = obj.get_data_list("products and shop info")
    
    # Only display the currently selected shop
    if val_container.get_seller_of_items() != "":
        data_list = [val_container.get_seller_of_items()]
    
    # Filter Data based on search bar input
    if len(obj.search_bar) > 0:
        if obj.display_values != "Products":
            data_list = [element for element in data_list if obj.get_search_bar_value().lower() in element.lower() and data_list == val_container.get_selected_shop()]
        else:
            data_list = [data_list[i] for i in range(len(data_list)) if obj.get_search_bar_value().lower() in data_list[i][0].lower()]
        
    # If Name Sort Enabled:
    if obj.sort_mode == "Name":
        data_to_display = sorted(data_list)
    else:
        data_to_display = data_list
    
    
    # Add values to display array
    for i in range(len(data_to_display)):
        text_to_display.append(data_to_display[i+obj.first_index_display][0] if obj.display_values == "Products" else data_to_display[i+obj.first_index_display])
        if len(text_to_display) >= 7:
            break
    obj.set_selector_bar_length(len(data_to_display))
    # Writing placeholders
    for i in range(len(obj.side_bar)): 
        text_to_print = text_to_print.replace("%side"+str(i)+"%", obj.get_side_bar(i))

    for i in range(len(obj.selector_bar)): 
        text_to_print = text_to_print.replace("%selector"+str(i)+"%", obj.get_selector_bar(i))
        
    for i in range(len(text_to_display)):
        text_to_print = text_to_print.replace("%line"+str(i)+"%", text_to_display[i])
        
    text_to_print = text_to_print.replace("%text%", obj.search_bar)
        
    text_to_print = text_to_print.replace("%up_arrow%", '▲' if obj.first_index_display > 0 else "")
    text_to_print = text_to_print.replace("%down_arrow%", '▼' if obj.first_index_display+7 < len(data_to_display) else "")
    text_to_print = text_to_print.replace("%possible_results_text%","Possible Results : "+str(obj.get_selector_bar_length()))
    text_to_print = text_to_print.replace("%namesort%", "←" if obj.sort_mode == "Name" else " ")
    text_to_print = text_to_print.replace("%selector_shops%", "←" if obj.display_values == "Shops" and obj.get_what_values_displayed() != "Shops" else " ")
    text_to_print = text_to_print.replace("%selector_products%", "←" if obj.display_values == "Products" else " ")
    if (obj.get_current_scroll_column() == "selector_bar" and obj.display_values == "Products"):
        text_to_print += "====|              |   From Shop: "+str(data_to_display[obj.selector_bar.index('►')+obj.first_index_display][1])+"\n"
        text_to_print += "====|              |=========================================="+"\n"
    if val_container.get_list_of_selected_items():
        text_to_print += "====|              |   Selected Products: "+str(len(val_container.get_list_of_selected_items()))+"\n"
        text_to_print += "====|              |   From Shop: "+val_container.get_seller_of_items()+"\n"
        text_to_print += "====|==============|=========================================="+"\n"
        text_to_print += "====| Press Shift+V to view selected products"+"\n"
    # Searchbar Guide
    textguide = ""
    if obj.side_bar[0] == '►':
        textguide = "Hit Characters to type. Hit Backspace to press delete" 
    elif obj.side_bar[1] == '►':
        textguide = "Hit ENTER to go back"
    elif obj.side_bar[2] == '►':
        textguide = "Hit ENTER to toggle Name-Sorting Mode"
    elif obj.side_bar[3] == '►':
        textguide = "Hit ENTER to view available shops"
    elif obj.side_bar[4] == '►':
        textguide = "Hit ENTER to view available products across shops"
    elif obj.scroll_column == 'right' and obj.display_values == "Shops":
        textguide = "Hit ENTER to view available products in the target shops"
    text_to_print = text_to_print.replace("%searchbar_guide%", textguide)
    # Blanking unused placeholders:
    for i in range(7):
        text_to_print = text_to_print.replace("%line"+str(i)+"%", "")
    # =======================================================================
    obj.set_number_of_values_displayed(len(data_to_display))
    obj.export_displayed_values(data_to_display)
        
    return text_to_print