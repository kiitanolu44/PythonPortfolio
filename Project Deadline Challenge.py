# Ask a user to enter the deadline for their project
# tell them how mant days they have to complete the project
# for extra credit, give the answer as a combination of weeks and days
#  (hint: you will need some of the math functions from module 4)

import datetime
currentDate = datetime.date.today()

# Months list, total days in each month
months = {
    1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 
    7:31, 8:31, 9:30, 10:31, 11:30, 12:31
}

# funtion to check if a year is a leap year or not
def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

userInput = input('Please enter the deadline date for your project deadline  or important event date in the format mm/dd/yyyy. ')
projectDeadlineDay = datetime.datetime.strptime(userInput, '%m/%d/%Y').date()

days = projectDeadlineDay - currentDate
print(days.days)

days = int(input("If you would like the remaining project time in years, months & weeks, re-enter the number of days remaining "))
print('note: input value must be greater than 1 day. ')

years = days // 365
days = days % 365
months = days // 30
days = days % 30
weeks = days // 7

print("Year(s) : ")
print(years)

print("Month(s) : ")
print(months)

print("Week(s) : ")
print(weeks)

print("Day(s) : ")
print(days)

