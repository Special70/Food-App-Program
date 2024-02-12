from system_files.config import debug_mode

# if True, the program is running. Once it becomes False, main functions will cease to run.
is_program_running = True

# Checks what menu is in display right now
current_display_ui = "Front Menu"

# Customized debug print function
def dbugprint(*text):
    if debug_mode: print(''.join(text))