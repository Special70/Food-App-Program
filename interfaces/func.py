from system_files.keyhit_reader import reset_key_hit_val
from system_files.sysfunc import dbugprint

def arrow_scroll(obj, attribute, direction):
    if direction == "up" and getattr(obj, attribute).index('►') != 0:
        arrow_index = getattr(obj, attribute).index('►')
        getattr(obj, attribute)[arrow_index], getattr(obj, attribute)[arrow_index-1] = ' ','►'
    if direction == "down" and getattr(obj, attribute).index('►') != len(getattr(obj, attribute))-1:
        arrow_index = getattr(obj, attribute).index('►')
        getattr(obj, attribute)[arrow_index], getattr(obj, attribute)[arrow_index+1] = ' ','►'
    reset_key_hit_val()
    