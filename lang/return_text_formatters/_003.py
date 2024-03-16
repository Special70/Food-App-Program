from system_files.food_data_reader import get_info
from interfaces.val_storage import val_container
from system_files.algorithms.quicksort import algorithm as quicksort

def _self(obj):
    text_to_print = obj.text
        
    # Get Specified Data
    data_to_display = []
    text_to_display = []
    data_list = get_info("shop products",targetkey=val_container.get_selected_shop())
    
    # Filter Data based on search bar input
    data_list = [element for element in data_list if obj.get_search_bar_value().lower() in element[0].lower()]
    # If Sort Enabled:
    if obj.sort_mode == "Name":
        data_to_display = sorted(data_list)
    elif obj.sort_mode == "Price":
        before_sort = data_list
        quicksort(before_sort, 0, len(before_sort)-1)
        data_to_display = before_sort
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
        text_to_print = text_to_print.replace("%line"+str(i)+"%", str(text_to_display[i][0]+" : $"+text_to_display[i][1])) 
        
    text_to_print = text_to_print.replace("%text%", obj.search_bar)
        
    text_to_print = text_to_print.replace("%up_arrow%", '▲' if obj.first_index_display > 0 else "")
    text_to_print = text_to_print.replace("%down_arrow%", '▼' if obj.first_index_display+7 < len(data_to_display) else "")
    text_to_print = text_to_print.replace("%namesort%", "←" if obj.sort_mode == "Name" else " ")
    text_to_print = text_to_print.replace("%pricesort%", "←" if obj.sort_mode == "Price" else " ")
    text_to_print = text_to_print.replace("%display_selected_shop%", val_container.get_selected_shop())
    if val_container.get_list_of_selected_items():
        text_to_print += "====|              |   Selected Products: "+str(len(val_container.get_list_of_selected_items()))+"\n"
        text_to_print += "====|              |   From Shop: "+val_container.get_seller_of_items()+"\n"
        text_to_print += "====|==============|=========================================="+"\n"
        text_to_print += "====| Press Shift+V to view selected products"+"\n"
    # Blanking unused placeholders:
    #print(val_container.get_list_of_selected_items())
    for i in range(7):
        text_to_print = text_to_print.replace("%line"+str(i)+"%", "")
    # =======================================================================
    obj.set_number_of_values_displayed(len(data_to_display))
    obj.export_displayed_values(data_to_display)
        
    return text_to_print