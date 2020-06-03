def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """
    Calculates the number of days between two dates.
    """
    try:
        assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    except AssertionError as e:
        return "Incorrect Input!"

    days = 0

    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    
    return days

def daysInMonth(year, month):
    """
    Returns the number of days in that month
    """
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if isLeapYear(year):
        days[1] = 29

    return days[month-1]

def isLeapYear(year):
    """
    Returns True if the year is a Leap year.
    """
    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def nextDay(year, month, day):
    """
    Adds 1 day to current date
    """
    if day < daysInMonth(year, month):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1

def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """
    Returns True if year1-month1-day-1 is before year2-month2-day2
    """
    if (year1 < year2):
        return True
    if (year1 == year2):
        if (month1 < month2):
            return True
        if (month1 == month2):
            return (day1 < day2)
    return False

def main():
    print(daysBetweenDates(2021, 9, 1, 2021, 10, 1))

if __name__ == "__main__":
    main()
