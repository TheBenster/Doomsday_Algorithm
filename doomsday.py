from random import randrange, choice
class Calendar():
    def random_day(day,  month, year, random_day):
        day = randrange(1,30)

        month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        year = randrange(1900, 1999)
        random_day = print(f'Your date is {choice(month)} {day}, {year}')
        return random_day
    def doomsday_calculation(anchorDay, year):
        yearString = str(year)
        yearLength = len(yearString)
        lastTwo = int(yearString[yearLength - 2: yearLength])
        result = lastTwo / 12
        remain = lastTwo % 12
        leapYear = remain / 4
        doomsday = result + remain + leapYear
        print(year)
        print(int(doomsday))

test = Calendar()

test.doomsday_calculation(year=randrange(1900,1999))

daysDict = { # Numbers signify abstraction of days
    'Sunday' : 0, 'Monday' : 1, 'Tuesday' : 2, "Wednesday": 3, "Thursday" : 4, "Friday": 5, "Saturday" : 6, 'Sunday' : 7 
}

anchorNum = { # Reference doomsday
    2000 : 2, 1900 : 3,
    1800 : 5, 1700 : 0
}

 # last two digits of year


    
'''if year < 2000: # If year is  1900- the anchor day is tuesday (The doomsday for the year 1900 is a tuesday)
    anchorDay = daysDict['Tuesday'] # anchorDay represents the doomsday for that particular year. Ex. 1900 is a tuesday, 1901 is a wednesday
    result =  lastTwo / 12 # Finds how many times 12 goes into lastTwo (last two digits of year)
    remain = lastTwo % 12 # Finds the remainder ex(1962, 60 goes into 12 5 times with a 2 remainder)
    leapYear = remain / 4 # Finds how many times the leap year (4) goes into the remainder
    
    print("12 goes in", int(result)) # int because floating point doesnt matter
    print("The remainder is", remain)
    print("There are", int(leapYear), "Leap years") # int see above

    doomsday = result + remain + leapYear # calculates the doomday for the specific year 
    print("Add", int(doomsday), "frrom anchor of the year")

    seven = doomsday / 7 #disregards 7 (ex. seven days from wednesday is still wednesday)
    answer = anchorDay + seven
    
    print("disregarding weeks this is your sum:", int(answer))

    mainResult = int(anchorDay + answer)
    print(mainResult)
    if mainResult == daysDict['Sunday']:
        print(f'The doomsday for {year} is Sunday')
    elif mainResult == daysDict['Monday']:
        print(f"The dooms day for {year} is Monday")
    elif mainResult == daysDict['Tuesday']:
        print(f"The doomsday for {year} is Tuesday") 
    elif mainResult == daysDict['Wednesday']:
        print(f"The doomsday for {year} is Wednesday")
    elif mainResult == daysDict['Thursday']:
        print(f"the doomsday for {year} is Thursday")
    elif mainResult == daysDict['Friday']:
        print(f"The doomsday for {year} is Friday")
        
    # print(int(answer))

'''

# print(anchorNum[2000])



