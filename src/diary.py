#!/usr/bin/python3
import os
from new_entry import new_entry
from get_usr_input import USR_ARGS
from settings import SETTINGS

#TODO export entry as pdf with pandoc: pandoc entry_name.md --pdf-engine=xelatex -o entry_name.pdf

def main():
    os.chdir(SETTINGS['diary_path'])
    if USR_ARGS.new_entry:
        new_entry()

if __name__ == '__main__':
    main()
