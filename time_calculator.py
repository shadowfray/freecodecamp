#shadowfray
#add time function - freecodecamp.org
'''
This code is compiled for freecodecamp.org assigments. This particular
function, add_time(), takes a time in clock notation, adds another amount
of time, and tells you the new time, while also telling you how many days
have passed.

add_time(start time, added time, start days)

add_time takes a start time like '3:00 PM', and an amount of time for added
time in similar notation, '2:00'. This would add 2 hours to 3 PM to get 5 PM.

start days is off by default, but if given a day of the week it will tell you
what day of the week it ends on after you add the given amount of time.
'''


def add_time(start:str, added:str, week_day=None):
    #days of the week so we can iterate over them later
    weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    #strips the times down to their numberic values
    stime = list((start.split()[0])) #start time
    add_time = list(added) #added time
    meridien = start[-2] #if it is am or pm

    startMin = stime[-2:] #gets the minutes of the start time
    startHour = stime[:(stime.index(':'))] #gets the hours of the start time
    addMin = add_time[-2:] #gets the minutes of the added time
    addHour = add_time[:(add_time.index(':'))] #gets the hours of the added time

    #puts together the pieces to get us the integer values we need to do the math
    #we will be doing all the math in minutes completely for sake of ease
    starting_min = pull_together(startMin)
    starting_hour = pull_together(startHour)
    adding_min = pull_together(addMin)
    adding_hour = pull_together(addHour)

    start_val = 60 * starting_hour + starting_min
    adding_val = 60 * adding_hour + adding_min

    #if it is PM we add 12 hours
    if meridien == 'P':
        start_val += 12 * 60

    final_time_raw = start_val + adding_val

    #Gives us numbers in base 60, as well as fitting the 12 hour clock schedule
    days_changed = final_time_raw // (24 * 60)
    refined_hour = final_time_raw // 60
    final_hour_12 = refined_hour % 12
    final_min = final_time_raw % 60

    if (refined_hour) > 12:
        final_meridian = 'PM'
    else:
        final_meridian = 'AM'

    final_time = str(final_hour_12) + ':' + str(final_min) + ' ' + final_meridian

    days_msg = '' #the message for how many days have passed
    fin_day = '' #in case we don't look at changed week days

    #checks the days if week_days != None
    if week_day != None:
        input_day_txt = week_day.lower()
        day_num = weekdays.index(input_day_txt) #converts our day of the week to a number for the list
        fin_day = weekdays[(day_num + days_changed)%7]

    if days_changed == 1:
        days_msg += ' (next day)'
    elif days_changed < 8:
        days_msg += f' {fin_day.capitalize()} ({days_changed} days later)'

    final_time += days_msg
        
    return(final_time)    
        

def pull_together(num_list):
    number = ''
    for i in num_list:
        number += i
    return int(number)

x = add_time('11:00 PM', '47:10')
print(x)
