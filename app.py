from datetime import datetime
import daysbetweendates

MESSAGES = {'start_year': 'Please enter start year ({}): '.format(datetime.now().year),
            'start_month': 'Please enter start month ({}): '.format(datetime.now().month),
            'start_day': 'Please enter start day ({}): '.format(datetime.now().day),
            'end_year': 'Please enter end year ({}): '.format(datetime.now().year), 
            'end_month': 'Please enter end month ({}): '.format(datetime.now().month),
            'end_day': 'Please enter end day ({}): '.format(datetime.now().day)}
MONTHS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def getInput(message, date_type, year=datetime.now().year, month=datetime.now().month):
    """
    Prompt the user for an input.
    """
    while True:
        try:
            value = int(input(message))
            if value > 0:
                if date_type == 'year':
                    return value
                elif date_type == 'month':
                    if value in MONTHS:
                        return value
                    else:
                        print("Wrong Input!")
                elif date_type == 'day':
                    if value > 0 and value <= daysbetweendates.daysInMonth(year, month):
                        return value
                    else:
                        print("Wrong Input!")
            else:
                print("Wrong Input!")
        except Exception as e:
            print("Wrong input")

def main():
    start_year = getInput(MESSAGES['start_year'], 'year')
    start_month = getInput(MESSAGES['start_month'], 'month')
    start_day = getInput(MESSAGES['start_day'], 'day', start_year, start_month)
    end_year = getInput(MESSAGES['end_year'], 'year')
    end_month = getInput(MESSAGES['end_month'], 'month')
    end_day = getInput(MESSAGES['end_day'], 'day', end_year, end_month)
    days = daysbetweendates.daysBetweenDates(start_year, start_month, start_day, end_year, end_month, end_day)

    print('Number of Days: {}'.format(days))


if __name__ == "__main__":
    main()