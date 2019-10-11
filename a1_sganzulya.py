#!/usr/bin/env python3
###################################
#program:a1_sganzulya.py
#Author: Steve Ganzulya
#Author ID: Sganzulya
#Date created: 09/23/2019
####################################
import sys
import os

def dbda():
    """
	Function: 
		Date Before/ Date After/ difference 
	
	Explanation:
		This function simply takes in a date & calls the before/after or get_difference function 			calculating from the arguments that you've inputted such as two dates, a + step counter  or  - step counter 

	example: 
		2018/01/01 500 --step ------- 2018/01/01 -500 --------2018/01/01 2018/01/02
    """

    if len(sys.argv) == 3 or len(sys.argv) == 4 and sys.argv.count("--step"):
        if len(sys.argv) == 3 and len(sys.argv[1]) == 10 and len(sys.argv[2]) == 10:
            date1 = sys.argv[1]
            date2 = sys.argv[2]
            if valid_date(date1) and valid_date(date2):
                print(get_difference(date1,date2))
       
        else:
            step = True if len(sys.argv) == 4 else False

            if (step == False or sys.argv[3] == "--step"):
                today = sys.argv[1]
                days = sys.argv[2]
            elif (sys.argv[1] == "--step"):
                today = sys.argv[2]
                days = sys.argv[3] 
            else:
                today = sys.argv[1]
                days = sys.argv[3]
        
            if valid_date(today):
                try:
                    if int(days) > 0:
                        after(today,days,step)
                    else:
                        days = abs(int(days))
                        before(today,days,step)
                except:
                    print ("Error: invalid days entered")
    else:
        usage()

def get_difference(date1,date2):
    """
        Function: 
		Get-Difference 
	
	Explanation:
		This function simple takes two dates which you've given it, and calculates the 	difference between the two dates outputting a string number of days between the two dates. Splits the string you input (yyyy/mm/dd) into day month & year, makes sure the bigger date is the second number just so you have a positive value at the end

	example: 
		2018/01/01 2018/01/02
		output : 1
	

    """
    str_year, str_month, str_day = date1.split('/')
    year1 = int(str_year)
    month1 = int(str_month)
    day1 = int(str_day)

    str_year, str_month, str_day = date2.split('/')
    year2 = int(str_year)
    month2 = int(str_month)
    day2 = int(str_day)
    
    if (year2 < year1 or year2 == year1 and month2 < month1 or year2 == year1 and month2 == month1 and day2 < day1):
        year2 = year2 + year1
        year1 = year2 - year1
        year2 = year2 - year1
        month2 = month2 + month1
        month1 = month2 - month1
        month2 = month2 - month1
        day2 = day2 + day1
        day1 = day2 - day1
        day2 = day2 - day1
     
    mon_max = days_in_mon(year1)
    count = 0

    while not(year2 == year1 and month2 == month1 and day2 == day1):
        day1 = day1 + 1 # next day
        if day1 > mon_max[month1]:
            day1 = 1 # if tmp_day > this month's max, reset to 1
            month1 = month1 + 1
       
        if month1 > 12:
            month1 = 1
            year1 = year1 + 1
            mon_max = days_in_mon(year1)

        count = count + 1

    return count


def after(today,days,step):
    """
        Function: 
		After 
	
	Explanation:
		This function simple returns the next date from the date that you started, and runs in a loop untill the days variable is completed. & if the steps function was one of the arguments it will output everytime it calculates the date for every step.
	example: 
		2018/01/01 3 --step
		output : 2018/01/01
			2018/01/02
			2018/01/03
			2018/01/04
    """
    str_year, str_month, str_day = today.split('/')
    year = int(str_year)
    month = int(str_month)
    day = int(str_day)

    mon_max = days_in_mon(year)

    for x in range(int(days)):
        day = day + 1 # next day
        if day > mon_max[month]:
            day = 1 # if tmp_day > this month's max, reset to 1
            month = month + 1
       
        if month > 12:
            month = 1
            year = year + 1
            mon_max = days_in_mon(year)

        if step == True:
            print(str(year)+"/"+str(month).zfill(2)+"/"+str(day).zfill(2))
    if step == False:
        print(str(year)+"/"+str(month).zfill(2)+"/"+str(day).zfill(2))  



def before(today,days,step):
    """
        Function: 
		Before 
	
	Explanation:
		This function simple returns the previous date from the date that you started, and runs in a loop untill the days variable is completed. & if the steps function was one of the 	arguments it will output everytime it calculates the date for every step.
	example: 
		2018/01/01 -3 --step
		output : 2018/01/01
			2017/12/31
			2017/12/30
			2017/12/29
    """
    str_year, str_month, str_day = today.split('/')
    year = int(str_year)
    month = int(str_month)
    day = int(str_day)
       
    mon_max = days_in_mon(year)

    for x in range(int(days)):
        day = day - 1 # previous day
        if day < 1:
            month = month - 1
            if month < 1:
                month = 12
                year = year - 1
            mon_max = days_in_mon(year)
            day = mon_max[month]

        if step == True:
            print(str(year)+"/"+str(month).zfill(2)+"/"+str(day).zfill(2))
    if step == False:
        print(str(year)+"/"+str(month).zfill(2)+"/"+str(day).zfill(2))  


def usage():
    """
        Function: 
		usage 
	
	Explanation:
		Prints usage str statement if something incorrect was inputted as the arguments
    """

    print("The correct usage of this script is YYYY/MM/DD & number of days(+/-#) --step or YYYY/MM/DD YYYY/MM/DD")

def days_in_mon(year):
    """
        Function: 
		Days in month 
	
	Explanation:
		This function contains a set of month:max number of days variable that simply contains all the int's for the max number of days per month & for feburary it calculates it based on year using the leap year function, returns list of days per month based on year
		
    """
    feb_max = 29 if leap_year(year) else 28
    return { 1:31, 2:feb_max, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
 
def leap_year(year):
    lyear = year % 4
    leapYear = True if lyear == 0 else False
 
    lyear = year % 100
    if lyear == 0:
        leapYear = False

    lyear = year % 400
    if lyear == 0:
        leapYear = True

    return leapYear

def valid_date(today):
    """
        Function: 
		Valid Date 
	
	Explanation:
		This function takes in the date argument & calculates if it's 10 digits long, and calculates if month is greater than maximum number of months per year or less & returns wrong month entered, checks days per month using the daysinmon function returns either true or false if date if real or unusable 

    """
    try:
        if len(today) != 10:
            print ("Error: wrong date entered")
            return False
        else:
            str_year, str_month, str_day = today.split('/')
            year = int(str_year)
            month = int(str_month)
            day = int(str_day)

            mon_max = days_in_mon(year)
            if (month > 12 or month < 1) :
                print("Error: wrong month entered")
                return False
            elif (day > mon_max[month] or day < 1):
                print("Error: wrong day entered")
                return False
            else:
                return  True
    except:
        print ("Error: wrong date entered")
        return False

if __name__ == '__main__':
    if len(sys.argv) == 3 or len(sys.argv) == 4 and sys.argv.count("--step"):
        dbda()
    else:
        usage()

