import os
import sys
import datetime
from components.get_usr_input import USR_ARGS
from components.utils import launch_text_editor

def chdir_to_entry_year_dir(entry_year):
    if not os.path.isdir(entry_year):
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
    if not USR_ARGS.date:
        entry_date = datetime.datetime.now()
    elif USR_ARGS.date == 'yesterday':
        entry_date = datetime.datetime.now() - datetime.timedelta(days=1)
    else:
        try:
            entry_date = datetime.datetime.strptime(USR_ARGS.date, '%d-%m-%y')
        except ValueError:
            print('wrong date format, use %d-%m-%y (e.g. 01-01-24)')
            sys.exit(1)

    year = str(entry_date.year)[-2:] # only last two digits
    month = str(entry_date.month) if len(str(entry_date.month)) == 2 else f'0{entry_date.month}' # so it always has two digits
    day = str(entry_date.day) if len(str(entry_date.day)) == 2 else f'0{entry_date.day}' # so it always has two digits

    return f'{year}-{month}-{day}', str(entry_date.year)

def make_tmp_markdown():
    with open('tmp.md', 'w', encoding='utf-8') as tmp:
        tmp.write('# Entry title\n[category]\n\nIf you quit the text editor without making any changes, this entry will not be saved.')

def new_entry():
    entry_date, year_str = get_entry_date()
    chdir_to_entry_year_dir(year_str)
    make_tmp_markdown()
    launch_text_editor('tmp.md')

    new_entry_title = get_entry_title()
    if new_entry_title == 'Entry_title':
        os.remove('tmp.md')
        sys.exit(0)

    new_entry_filename = f'{entry_date}{"-" if new_entry_title else ""}{new_entry_title}.md'
    os.rename('tmp.md', new_entry_filename.lower())
