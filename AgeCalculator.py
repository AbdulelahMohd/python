import datetime
today = datetime.date.today()
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
day = int(input("Enter a day: "))
birthday = datetime.date(year, month, day)
age =  today.year - birthday.year
if (today.month , today.day) < (birthday.month, birthday.day):
    age -=1
    print ("Your age is: ", age)
