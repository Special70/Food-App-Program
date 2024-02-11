import msvcrt

from system_files import system_status

from system_files.sysfunc import dbugprint, arrow_scroll, ScrollBar

key_hit = ""
editor_mode = False

specified_scrollbar = ScrollBar(1)

def initialize_keypress_reader():
    special_key_hit = False 
    dbugprint("[!] Key Presser Function has been executed [!]")
    while (system_status.isRunning):
        if msvcrt.kbhit():
            raw_key_hit = str(msvcrt.getch())
            
            match(raw_key_hit):
                case "b'\\x08'":
                    key_hit = "Backspace_Key"
                    dbugprint("Backspace Key")
                    continue
                case "b'\\r'":
                    key_hit = "Enter_Key"
                    dbugprint("Enter Key")
                    continue

            if "b'\\x" in raw_key_hit:
                special_key_hit = True
                # dbugprint("Special Key Hit!")
                continue
            match(raw_key_hit):  
                case "b'H'":
                    if special_key_hit : 
                        key_hit = "Up_Key"
                        dbugprint("Up Key")
                        arrow_scroll(specified_scrollbar, "up")

                case "b'P'":
                    if special_key_hit : 
                        key_hit = "Down_Key"
                        dbugprint("Down Key")
                        arrow_scroll(specified_scrollbar, "down")
                case "b'K'":
                    if special_key_hit : 
                        key_hit = "Left_Key"
                        dbugprint("Left Key")
                case "b'M'":
                    if special_key_hit : 
                        key_hit = "Right_Key"
                        dbugprint("Right Key")
            if special_key_hit:
                special_key_hit = False
                continue
                    
            key_hit = raw_key_hit[2:3]
            dbugprint(key_hit)