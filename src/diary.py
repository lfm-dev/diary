#!/usr/bin/python3
import os
from get_usr_input import get_args
from new_entry import new_entry

#TODO export entry as pdf with pandoc: pandoc entry_name.md --pdf-engine=xelatex -o entry_name.pdf

MARKDOWN_EDITOR_CMD = 'micro'
DIARY_DIR_PATH = '/path/to/dir'
USR_ARGS, PARSER = get_args()

def main():
    os.chdir(DIARY_DIR_PATH)
    if USR_ARGS.new_entry:
        new_entry()

if __name__ == '__main__':
    main()
