import sys
import re

args = sys.argv[1:]


def date_validator(date):
    is_date_format = bool(re.match('([0-9]{2}-{1}){2}[0-9]{4}$'))

#truncate the file name and collect all args passed in cli
def main():
    #initiate variables
    start_date = start_time = end_date = end_time = None

    #re-assign to args passed
    if len(args) == 1:
        end_date = args[0]
    elif len(args) == 4:
        start_date, start_time, end_date, end_time = args
    else:
        print('No Arguments supplied')
    