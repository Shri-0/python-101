# Use the interpreter to calculate how many seconds are in a year.
# Then write the code in this script file below this line.

import math

SECONDS = 60
MINUTES = 60
HOURS_DAY = 24
DAYS_WEEK = 7
WEEKS_MONTH = 4.34521
MONTHS = 12

ONEDAYTIME = SECONDS * MINUTES * HOURS_DAY
TOTALTIME = DAYS_WEEK * WEEKS_MONTH * MONTHS

#print(int(ONEDAYTIME))
#print(float(TOTALTIME))

total = str(int(round(ONEDAYTIME * TOTALTIME)))

print(str("There are "  + total +  " seconds in a year"))


#Type in 'python3' and use interpretor there to figure out calculation
