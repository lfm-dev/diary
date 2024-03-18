import os
import sys
import datetime
from diary import DIARY_DIR_PATH, USR_ARGS
from utils import launch_text_editor

def chdir_to_entry_year_dir(entry_year):
    if not os.path.isdir(os.path.join(DIARY_DIR_PATH, entry_year)):
        os.mkdir(entry_year)
    os.chdir(entry_year)

def get_entry_title():
    new_entry_title = ''
    with open('tmp.md', encoding='utf-8') as new_entry_file:
        for line in new_entry_file:
            if line.startswith('#'):
                new_entry_title = line.strip('#').strip()
                new_entry_title = ('_').join(new_entry_title.split()) # remove extra spaces between words
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

    return f'{year}-{month}-{day}', str(entry_date.year)

def new_entry():
    entry_date, year = get_entry_date()
    chdir_to_entry_year_dir(year)
    launch_text_editor('tmp.md')

    if os.path.isfile('tmp.md') and os.path.getsize('tmp.md') == 0: # empty file
        os.remove('tmp.md')

    if not os.path.isfile('tmp.md'): # user exited without saving
        sys.exit(0)

    new_entry_title = get_entry_title()
    new_entry_filename = f'{entry_date}{"-" if new_entry_title else ""}{new_entry_title}.md'
    os.rename('tmp.md', new_entry_filename.lower())
