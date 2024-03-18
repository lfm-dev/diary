import os
from diary import MARKDOWN_EDITOR_CMD

def launch_text_editor(filename):
    os.system(f'{MARKDOWN_EDITOR_CMD} {filename}')
