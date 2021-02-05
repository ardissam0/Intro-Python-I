"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

import sys
import calendar
from datetime import datetime

#how many arguments are passed into the program?

month = datetime.today().month
year = datetime.today().year

if len(sys.argv) > 1:
    month = int(sys.argv[1])
if len(sys.argv) > 2:
    year = int(sys.argv[2])

print(calendar.month(year, month))

#OR

#if len(sys.argv) == 1
#then no argumens were passed in
#if len(sys.argv) == 2
#then 1 arguments was passed in
#if len(sys.argv) == 3
#then 2 arguments were passed in

# l = len(sys.argv)

# # print(datetime.now().month)
# # print(datetime.now().year)

# #print for current date and time
# if l == 1:
#   month = datetime.now().month
#   year = datetime.now().year

# elif l == 2:
#   month = int(sys.argv[1])
#   year = datetime.now().year

# elif l == 3:
#   month = int(sys.argv[1])
#   year = int(sys.argv[2])

# else:
#   print("Usage: cal.py [month] [year]")
#   #exit the program
#   sys.exit(0)

# #how do we render the calendar?
# cal = calendar.TexCalendar()
# #print out the calendar
# cal.prmonth(year, month)
