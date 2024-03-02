#!/usr/bin/python3
import os
import time

MARKDOWN_EDITOR_CMD = 'micro'
DIARY_DIR_PATH = '/path/to/dir'

def new_entry():
    def chdir_to_current_year_dir():
        current_year = time.localtime().tm_year
        if not os.path.isdir(os.path.join(DIARY_DIR_PATH, str(current_year))):
            os.mkdir(current_year)
        os.chdir(str(current_year))

    def get_entry_title():
        new_entry_title = ''
        with open('tmp.md', encoding='utf-8') as new_entry_file:
            for line in new_entry_file:
                if line.startswith('#'):
                    new_entry_title = line.strip('#').strip()
                    new_entry_title = (' ').join(new_entry_title.split()) # remove extra spaces between words
                    break
        return new_entry_title

    chdir_to_current_year_dir()
    os.system(f'{MARKDOWN_EDITOR_CMD} tmp.md')
    new_entry_title = get_entry_title()
    year = str(time.localtime().tm_year)[-2:] # only last two digits
    month = str(time.localtime().tm_mon) if len(str(time.localtime().tm_mon)) == 2 else f'0{time.localtime().tm_mon}' # so it always has two digits
    day = str(time.localtime().tm_mday) if len(str(time.localtime().tm_mday)) == 2 else f'0{time.localtime().tm_mday}' # so it always has two digits
    new_entry_filename = f'{year}-{month}-{day}{"-" if new_entry_title else ""}{new_entry_title.replace(" ", "_")}.md'
    os.rename('tmp.md', new_entry_filename)

def main():
    os.chdir(DIARY_DIR_PATH)
    new_entry()


if __name__ == '__main__':
    main()
