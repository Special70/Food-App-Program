from msvcrt import kbhit, getch
from system_files.sysfunc import is_program_running, dbugprint

key_hit = ""

def initialize_keyhit_reader():
    dbugprint("[!] initialize keyhit reader! ")
    global key_hit

    special_key_hit = False # Other keys such as arrow keys make the msvcrt library run twice
    special_key_tag = None
    
    while is_program_running:
        if kbhit():
            raw_key_hit = str(getch())
            # Back and Enter key checks:
            if raw_key_hit == "b'\\x08'":
                dbugprint("Backspace Key")
                continue
            elif raw_key_hit == "b'\\r'":
                dbugprint("Enter Key")
                continue

            if "b'\\x" in raw_key_hit:
                special_key_hit = True
                special_key_tag = raw_key_hit
                continue

            # Check for arrow keys and other characters that may cause the method to run twice
            if special_key_hit:
                match(special_key_tag, raw_key_hit):
                    case "b'\\xe0'", "b'H'":
                        dbugprint("Up Key Press")
                    case "b'\\xe0'", "b'P'":
                        dbugprint("Down Key Press")
                    case "b'\\xe0'", "b'K'":
                        dbugprint("Left Key Press")
                    case "b'\\xe0'", "b'M'":
                        dbugprint("Right Key Press")
                raw_key_hit = ""
                special_key_hit = False
                continue

            key_hit = raw_key_hit[2:3]
            dbugprint(raw_key_hit)