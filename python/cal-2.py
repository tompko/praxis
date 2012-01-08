import sys
import datetime
from praxis import jdn

months = ["", "January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
day_months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def format_month(year, month, day=-1):
    """Format a calendar for a given month, highlight the day if given"""
    week_header = " Mo Tu We Th Fr Sa Su "
    spaces = len(week_header) - len(months[month])
    right = spaces / 2
    left = spaces - right
    month_str = " " * left + months[month] + " " * right
    ret = [month_str, week_header]
    line = " "
    curr_day = jdn(year, month, 1) % 7

    for i in range(curr_day):
        line += "   "

    for i in range(day_months[month]):
        if i + 1 == day:
            line = line[:-1] + "[%2i]" % (i+1)
        else:
            line += "%2i " % (i+1)
        curr_day += 1
        if curr_day == 7:
            ret.append(line)
            line = " "
            curr_day = 0

    for i in range(curr_day, 7):
        line += "   "
    ret.append(line)

    return ret

def print_help():
    print """usage: cal-2.py [-h] [-3] [month] [year]

cal -h         : Print this message
cal -3         : Print a three-month calendar for the prior month,
                 current month and next month
cal year       : Print a twelve-month calendar for the specified year
cal month year : Print a calendar for the specified month and year

"""

if __name__ == "__main__":
    if len(sys.argv) == 1:
        #Called with no arguments
        today = datetime.date.today()
        cal = format_month(today.year, today.month, today.day)
        for c in cal:
            print c
    if len(sys.argv) == 2:
        #Called with one argument, -3, -h, or the year
        if sys.argv[1] == "-3":
            today = datetime.date.today()
            last_month = (today.year, today.month-1, -1)
            next_month = (today.year, today.month+1, -1)
            if last_month[1] == 0:
                last_month = (today.year-1, 12, -1)
            if next_month[1] == 13:
                next_month = (today.year+1, 1, -1)
            last_month = format_month(*last_month)
            this_month = format_month(today.year, today.month, today.day)
            next_month = format_month(*next_month)

            print "\n".join(["    ".join(z) for z in zip(last_month, this_month, next_month)])
        elif sys.argv[1] == "-h":
            print_help()
        else:
            try:
                year = int(sys.argv[1])
            except:
                print_help()
                sys.exit(1)
            cal = []
            for i in range(12):
                cal.append(format_month(year, i+1))
            cal = [cal[i*3:i*3+3] for i in range(4)]
            for c in cal:
                print "\n".join(["    ".join(z) for z in zip(*c)])
                print ""
    elif len(sys.argv) == 3:
        #Called with two arguments the month and the year
        try:
            month = int(sys.argv[1])
            year = int(sys.argv[2])
            cal = format_month(year, month)
            for c in cal:
                print c
        except:
            print_help()
            sys.exit(1)
