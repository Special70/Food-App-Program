from system_files.sysfunc import is_program_running

from lang.locale_EN import _001_front_menu


def _self():
    print(_001_front_menu)
    while is_program_running:
        pass