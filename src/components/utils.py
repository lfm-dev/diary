import os
from components.settings import SETTINGS

def launch_text_editor(filename):
    os.system(f'{SETTINGS["text_editor"]} {filename}')
