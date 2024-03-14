#!/usr/bin/python3
import os
import sys
import time
from get_usr_input import get_args

MARKDOWN_EDITOR_CMD = 'micro'
DIARY_DIR_PATH = '/path/to/dir'

USR_ARGS, PARSER = get_args()

def new_entry():
    def chdir_to_current_year_dir():
        current_year = time.localtime().tm_year
        if not os.path.isdir(os.path.join(DIARY_DIR_PATH, str(current_year))):
            os.mkdir(str(current_year))
        os.chdir(str(current_year))

    def launch_text_editor():
        os.system(f'{MARKDOWN_EDITOR_CMD} tmp.md')

    def get_entry_title():
        new_entry_title = ''
        with open('tmp.md', encoding='utf-8') as new_entry_file:
            for line in new_entry_file:
                if line.startswith('#'):
                    new_entry_title = line.strip('#').strip()
                    new_entry_title = (' ').join(new_entry_title.split()) # remove extra spaces between words
                    break
        return new_entry_title

    def get_entry_date():
        year = str(time.localtime().tm_year)[-2:] # only last two digits
        month = str(time.localtime().tm_mon) if len(str(time.localtime().tm_mon)) == 2 else f'0{time.localtime().tm_mon}' # so it always has two digits
        day = str(time.localtime().tm_mday) if len(str(time.localtime().tm_mday)) == 2 else f'0{time.localtime().tm_mday}' # so it always has two digits
        return f'{year}-{month}-{day}'

    chdir_to_current_year_dir()
    launch_text_editor()
    if not os.path.isfile('tmp.md'): # user exited without saving
        sys.exit(0)
    new_entry_title = get_entry_title()
    entry_date = get_entry_date()
    new_entry_filename = f'{entry_date}{"-" if new_entry_title else ""}{new_entry_title.replace(" ", "_")}.md'
    os.rename('tmp.md', new_entry_filename.lower())

def main():
    os.chdir(DIARY_DIR_PATH)
    if USR_ARGS.new_entry:
        new_entry()


if __name__ == '__main__':
    main()
