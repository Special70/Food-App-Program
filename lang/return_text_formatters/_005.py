from interfaces.val_storage import val_container

def _self(obj, scroll_direction="null"):
    text_to_print = obj.text   
    
    # Get Specified Data
    data_to_display = val_container.get_list_of_selected_items()
    #print(data_to_display)
    text_to_display = []
    
    text_to_print = text_to_print.replace("%shop_name%", val_container.get_selected_shop())
    
    # Add values to display array
    for i in range(len(data_to_display)):
        text_to_display.append(data_to_display[i+obj.first_index_display])
        if len(text_to_display) >= 7:
            break
    # Max Index (Used to find out the max index for a display for the scrolling option)
    max_index = 0 if len(data_to_display) < 7 else len(data_to_display)-7
    current_index = obj.current_index
    
    if scroll_direction == "up" and current_index > 0:
        obj.current_index -= 1
    elif scroll_direction == "down" and current_index < max_index:
        obj.current_index += 1
    
    for i in range(len(text_to_display)):
        text_to_print = text_to_print.replace("%line"+str(i)+"%", "("+str(text_to_display[i+obj.current_index][2])+"x)"+" "+str(text_to_display[i+obj.current_index][0]+" : $"+text_to_display[i+obj.current_index][1])) 
    
    text_to_print = text_to_print.replace("%up_arrow%", '▲' if current_index > 0 else "")
    text_to_print = text_to_print.replace("%down_arrow%", '▼' if current_index < max_index else "")
    
    text_to_print = text_to_print.replace("%total_price%",f"{sum([item[2]*float(item[1]) for item in data_to_display]):.2f}")
    # Blanking unused placeholders
    for i in range(7):
        text_to_print = text_to_print.replace("%line"+str(i)+"%", "")
    return text_to_print
    
    