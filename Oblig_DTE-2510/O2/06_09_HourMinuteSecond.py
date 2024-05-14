# Timer, minutter, sekunder (Liang 6.9extra).
# Fra oppgaven: Note that a zero is padded to hour, minute, and 
# second if any of these values is a single digit (dette stemmer ikke i mitt tilfelle) *

def format(seconds):
    seconds = seconds % (24 * 3600) # use 24 hour format
    hours = int(seconds / 3600) # one option is to isolate hours 
    seconds = seconds % 3600
    minutes = seconds // 60 # another option is whole number division
    seconds = seconds % 60
    return(hours,minutes,seconds)

total_seconds = int(input("enter seconds: "))

hours,minutes,seconds = format(total_seconds)

print(f"The hours, minutes, and seconds for total seconds {total_seconds} is {hours:02d}:{minutes:02d}:{seconds:02d}") #* formaterer selv
#print(f"The hours, minutes, and seconds for total seconds {total_seconds} is {hours}:{minutes}:{seconds}") # adds no leading zeroes as stated

