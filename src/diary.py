#!/usr/bin/python3
import os
from new_entry import new_entry
from constants import DIARY_DIR_PATH, USR_ARGS

#TODO export entry as pdf with pandoc: pandoc entry_name.md --pdf-engine=xelatex -o entry_name.pdf

def main():
    os.chdir(DIARY_DIR_PATH)
    if USR_ARGS.new_entry:
        new_entry()

if __name__ == '__main__':
    main()
