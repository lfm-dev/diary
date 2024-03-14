#!/usr/bin/python3
import os
import sys
import datetime
from get_usr_input import get_args

MARKDOWN_EDITOR_CMD = 'micro'
DIARY_DIR_PATH = '/path/to/dir'

USR_ARGS, PARSER = get_args()

def new_entry():
    def chdir_to_current_year_dir():
        current_year = datetime.datetime.now().year
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
        if USR_ARGS.date:
            if USR_ARGS.date == 'yesterday':
                entry_date = datetime.datetime.now() - datetime.timedelta(days=1)

            else:
                try:
                    entry_date = datetime.datetime.strptime(USR_ARGS.date, '%d-%m-%y')
                except ValueError:
                    print('wrong date format, use %d-%m-%y (e.g. 01-01-24)')
                    sys.exit(1)

        else:
            entry_date = datetime.datetime.now()

        year = str(entry_date.year)[-2:] # only last two digits
        month = str(entry_date.month) if len(str(entry_date.month)) == 2 else f'0{entry_date.month}' # so it always has two digits
        day = str(entry_date.day) if len(str(entry_date.day)) == 2 else f'0{entry_date.day}' # so it always has two digits
        return f'{year}-{month}-{day}'

    chdir_to_current_year_dir()
    entry_date = get_entry_date()
    launch_text_editor()
    if not os.path.isfile('tmp.md'): # user exited without saving
        sys.exit(0)
    new_entry_title = get_entry_title()
    new_entry_filename = f'{entry_date}{"-" if new_entry_title else ""}{new_entry_title.replace(" ", "_")}.md'
    os.rename('tmp.md', new_entry_filename.lower())

def main():
    os.chdir(DIARY_DIR_PATH)
    if USR_ARGS.new_entry:
        new_entry()


if __name__ == '__main__':
    main()
