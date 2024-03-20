import argparse

def get_args():
    parser = argparse.ArgumentParser(prog='diary', description='Manage your digital diary')
    parser.add_argument('-e', '-entry', action='store_true', dest='new_entry', help='write new entry')
    parser.add_argument('-d', '-date', metavar='', dest='date', help='change date of writing')
    args = parser.parse_args()
    return args, parser

USR_ARGS, PARSER = get_args()
