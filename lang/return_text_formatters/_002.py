def _self(obj):
    text_to_print = obj.text
        
    # Get Specified Data
    data_to_display = []
    text_to_display = []
    if obj.display_values == "Shops":
        data_list = obj.get_data_list()
    elif obj.display_values == "Products":
        data_list = obj.get_data_list("products and shop info")
    
    # Filter Data based on search bar input
    if len(obj.search_bar) > 0:
        if obj.display_values != "Products":
            data_list = [element for element in data_list if obj.get_search_bar_value().lower() in element.lower()]
        else:
            data_list = [data_list[i] for i in range(len(data_list)) if obj.get_search_bar_value().lower() in data_list[i][0].lower()]
        
    # If Name Sort Enabled:
    if obj.sort_mode == "Name":
        data_to_display = sorted(data_list)
        #data_list_with_shop_name = sorted(data_list_with_shop_name)
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
    text_to_print = text_to_print.replace("%selector_shops%", "←" if obj.display_values == "Shops" else " ")
    text_to_print = text_to_print.replace("%selector_products%", "←" if obj.display_values == "Products" else " ")
    text_to_print = text_to_print.replace("%productdisplay0%", "====|              |   From Shop: "+str(data_to_display[obj.selector_bar.index('►')+obj.first_index_display][1]) if (obj.get_current_scroll_column() == "selector_bar" and obj.display_values == "Products") else "")
    text_to_print = text_to_print.replace("%productdisplay1%", "==============================================================" if (obj.get_current_scroll_column() == "selector_bar" and obj.display_values == "Products") else "")
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