from interfaces.val_storage import val_container
from system_files.sysfunc import dbugprint
from system_files.keyhit_reader import reset_key_hit_val

def _self(obj, scroll_direction="null"):
    text_to_print = obj.text   
    
    # Get Specified Data
    data_to_display = val_container.get_list_of_selected_items()
    #print(data_to_display)
    text_to_display = []
    
    text_to_print = text_to_print.replace("%shop_name%", val_container.get_selected_shop())
    
    # Max Index (Used to find out the max index for a display for the scrolling option)
    max_index = 0 if len(data_to_display) < 7 else len(data_to_display)-7
    dbugprint(str(f"Max Index: {max_index} | Current Index: {obj.current_index}"))
    
    if scroll_direction == "up" and obj.current_index > 0:
        obj.current_index -= 1
    elif scroll_direction == "down" and obj.current_index < max_index:
        obj.current_index += 1
    
    # Add values to display array
    for i in range(len(data_to_display)):
        text_to_display.append(data_to_display[i+obj.current_index])
        if len(text_to_display) >= 7:
            break
    
    text_to_print = text_to_print.replace("%up_arrow%", '▲' if obj.current_index > 0 else "")
    text_to_print = text_to_print.replace("%down_arrow%", '▼' if obj.current_index < max_index else "")
    
    for i in range(len(text_to_display)):
        text_to_print = text_to_print.replace("%line"+str(i)+"%", "("+str(text_to_display[i][2])+"x)"+" "+str(text_to_display[i][0]+" : $"+text_to_display[i][1])) 
    
    text_to_print = text_to_print.replace("%total_price%",f"{sum([item[2]*float(item[1]) for item in data_to_display]):.2f}")
    val_container.total_price_of_selected_items = sum([item[2]*float(item[1]) for item in data_to_display])
    # Blanking unused placeholders
    for i in range(7):
        text_to_print = text_to_print.replace("%line"+str(i)+"%", "")
    return text_to_print
    
    