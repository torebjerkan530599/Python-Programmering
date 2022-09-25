# Timer, minutter, sekunder (Liang 6.9extra)

def format(seconds):
    seconds = seconds % (24 * 3600) # use 24 hour format
    hours = int(seconds / 3600) # one option to isolate hours 
    seconds = seconds % 3600
    minutes = seconds // 60 # another option is whole number division
    seconds = seconds % 60
    remainin_sec = seconds
    #return(hours,minutes,remainin_sec)

    # Assignment says: Note that a zero is padded to hour,
    # minute, and second if any of these values is a single
    # digit.

    # This doesn't happen in my case. To test,
    # comment in return statement on line 12
    # also comment in two last statements in program

    str_hour = str(hours)
    str_min = str(minutes)
    str_sec = str(remainin_sec)
    if(hours < 10):
         str_hour = "0"+str_hour
    if(minutes < 10):
         str_min = "0"+str_min
    if(remainin_sec < 10):
        str_sec = "0"+str_sec
    return str_hour+":"+str_min+":"+str_sec


total_seconds = int(input("enter seconds: "))

print("The hours, minutes, and seconds for total seconds",total_seconds, "is", format(total_seconds)) #use with leading zero solution if any time-value is below 10

# For testing with the return statement on line 12
# hours,minutes,seconds = format(total_seconds)
# print("The hours, minutes, and seconds for total seconds ",total_seconds," is ", hours,":",minutes,":",seconds)


