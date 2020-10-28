#! /usr/bin/env python3

#Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.
#
#The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.
#
#It is much easier to understand with an example:
#
#format_duration(62)    # returns "1 minute and 2 seconds"
#format_duration(3662)  # returns "1 hour, 1 minute and 2 seconds"
#For the purpose of this Kata, a year is 365 days and a day is 24 hours.
#
#Note that spaces are important.
#
#Detailed rules
#The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive integer and one of the valid units of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.
#
#The components are separated by a comma and a space (", "). Except the last component, which is separated by " and ", just like it would be written in English.
#
#A more significant units of time will occur before than a least significant one. Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.
#
#Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.
#
#A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.
#
#A unit of time must be used "as much as possible". It means that the function should not return 61 seconds, but 1 minute and 1 second instead. Formally, the duration specified by of a component must not be greater than any valid more significant unit of time.

def format_duration(time):
    # trivial cases
    if time < 0:
        print("not a valid input")
        return
    if time == 0:
        return "now"

    # time conversion
    secs = [time % 60, 'second']
    mins = [time // 60 % 60, 'minute']
    hrs = [time // (60*60) % 24, 'hour']
    days = [time // (60*60*24) % 365, 'day']
    years = [time // (60*60*24*365), 'year']
    collection = [years, days, hrs, mins, secs]
    
    for unit in collection: 
        if unit[0] > 1:
            unit[1] = unit[1] + 's'
        else:
            continue
    collection = [x for x in collection if x[0] != 0]

    result = ""
    
    amount = len(collection)
    for unit in collection:
        if amount > 2: 
            result = f"{result}{unit[0]} {unit[1]}, "
            amount = amount - 1
        elif amount == 2:
            result = f"{result}{unit[0]} {unit[1]} and "
            amount = amount - 1
        elif amount == 1:
            result  = f"{result}{unit[0]} {unit[1]}"

    return result



# testing
print(format_duration(3662))





