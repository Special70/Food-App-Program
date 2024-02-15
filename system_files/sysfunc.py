from system_files.config import debug_mode

# if True, the program is running. Once it becomes False, main functions will cease to run.
is_program_running = True

def get_program_status():
    return is_program_running

def kill_program():
    global is_program_running
    is_program_running = False

# Checks what menu is in display right now
current_display_ui = "Front Menu"

def change_current_display(specified_menu):
    global current_display_ui
    current_display_ui = specified_menu

def get_current_display():
    return current_display_ui

# Customized debug print function
def dbugprint(*text):
    if debug_mode: print(''.join(text))
    