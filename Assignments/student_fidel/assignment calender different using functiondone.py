
def calender(best):
    if (yr1 != yr2):
        sum = yr1 - yr2
        return str(int(sum)) + ' years gone'
    else:
        if (yr1 == yr2):
            return 'they year are the same'
    if (mth1 != mth2):
        sum = mth1 - mth2
        return str(int(sum)) + ' months gone'
    else:
        if (mth1 == mth2):
            return 'the month are the same'
    if (day1 != day2):
        sum = day1 - day2
        return str(int(sum)) + ' days left'
    else:
        if (day1 == day2):
            return 'the days are the same'
print('calculate this calender?')
yr1 = int(input('enter the first year: '))
mth1 = int(input('enter the first month: '))
day1 = int(input('enter the fisrt day: '))
yr2 = int(input('enter the second year: '))
mth2 =int(input('enter the second month: '))
day2 = int(input('enter the second day: '))
calender('best')

    