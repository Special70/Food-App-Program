from system_files.keyhit_reader import reset_key_hit_val
from system_files.sysfunc import dbugprint

def arrow_scroll(obj, direction):
    print(obj.bar)
    if direction == "up" and obj.bar.index('►') != 0:
        arrow_index = obj.bar.index('►')
        obj.bar[arrow_index], obj.bar[arrow_index-1] = ' ','►'
    if direction == "down" and obj.bar.index('►') != len(obj.bar)-1:
        arrow_index = obj.bar.index('►')
        obj.bar[arrow_index], obj.bar[arrow_index+1] = ' ','►'
    reset_key_hit_val()
    