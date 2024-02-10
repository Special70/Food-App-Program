import msvcrt

from system_files import system_status

from system_files.sysfunc import dbugprint

key_hit = ""
editor_mode = False

'''
Notes:
- msvcrt prints something twice on specific keys. So a specific system is need to do proper checks.

'''

def initialize_keypress_reader():
    special_key_hit = False 
    dbugprint("[!] Key Presser Function has been executed [!]")
    while (system_status.isRunning):
        if msvcrt.kbhit():
            raw_key_hit = str(msvcrt.getch())
            if raw_key_hit == "b'\\x00'":
                special_key_hit = True
                continue
            match(raw_key_hit):
                case "b'\\x08'":
                    dbugprint("Backspace Key")
                    continue
                case "b'\\r'":
                    dbugprint("Enter Key")
                    continue
                
                case "b'H'":
                    if special_key_hit : 
                        dbugprint("Up Key")
                        special_key_hit = False
                        continue
                case "b'P'":
                    if special_key_hit : 
                        dbugprint("Down Key")
                        special_key_hit = False
                        continue
                case "b'K'":
                    if special_key_hit : 
                        dbugprint("Left Key")
                        special_key_hit = False
                        continue
                case "b'M'":
                    if special_key_hit : 
                        dbugprint("Right Key")
                        special_key_hit = False
                        continue
                case _:
                    if special_key_hit : 
                        special_key_hit = False
                        continue
                    
            key_hit = raw_key_hit[2:3]
            dbugprint(key_hit)
            
