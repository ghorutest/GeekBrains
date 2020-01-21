import sys
from sys import argv


def salary_count():
    """Returns full payout"""
    try:
        hours, s_in_hour, premium = map(float, argv[1:])
    except ValueError:
        print('<1_getopt.py> hours | salary-in-hour | premium (all 3 args - numbers)')
        sys.exit(2)

    return hours * s_in_hour + premium


print(f'Full payout = {salary_count()}')
