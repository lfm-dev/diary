#!/usr/bin/python3
import os
from components.new_entry import new_entry
from components.get_usr_input import USR_ARGS, PARSER
from components.settings import SETTINGS

#TODO export entry as pdf with pandoc: pandoc entry_name.md --pdf-engine=xelatex -o entry_name.pdf
#TODO add categories
#TODO print table

def main():
    os.chdir(SETTINGS['diary_path'])

    if USR_ARGS.new_entry:
        new_entry()

    else:
        PARSER.print_help()

if __name__ == '__main__':
    main()
