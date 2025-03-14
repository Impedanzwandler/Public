import os

# Pathsetting
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

#test Python
import os
print(os.getcwd()) 

#=================================================================================================

#defintion of variables
the_thing = 0
start_date = 0
end_date = 0
duration = 0

#prepping moduls
from datetime import datetime

#=================================================================================================

#greeting
print("Hello Stranger!")
print("Ever wondered what lasted longer than your failed marriage, your last relationship or maybe your college education?")
print("Fear not. This programm will provide you with a funny list of things that lasted longer.")
#=================================================================================================

#functions, getting inputs
def get_thing_input():
    global the_thing
    the_thing = input("Please provide the time in your life, that you want to compare: My ")
    print(f"So you would like to compare your {the_thing} to stuff that happened in the world?")
    
def get_start_input():
    global the_thing
    global start_date    
    while True:
        try:
            start_date = input(f"When did your {the_thing} start? Please provide the date in YYYY-MM-DD: ")
            start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
            print(f"I see. Your {the_thing} started at {start_date}.")
            break
        except ValueError:
            print("Please provide a valid date in the format YYYY-MM-DD.")
        
def get_end_input():
    global the_thing
    global end_date
    while True:
        try:
            end_date = input(f"When did your {the_thing} end? Please provide the date in YYYY-MM-DD: ")
            end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
            break
        except ValueError:
            print("Please provide a vaild date in the format YYYY-MM-DD. Don't forget the '-'!")
        
def compare_dates():
    global the_thing
    global start_date
    global end_date
    
    while True:
        if end_date > start_date:
            print(f"Your {the_thing} ended at {end_date}.")
            break
        else:
            print(f"Your end date cannot be befor your starting date. :)" )
                     
            
def read_compare_list(file_path):
    events = []
    with open(file_path, "r") as fobj:
        for line in fobj:
            parts = line.strip().split(" ", 2)
            if len(parts) == 3:
                event_start_date = datetime.strptime(parts[0], '%Y-%m-%d').date()
                event_end_date = datetime.strptime(parts[1], '%Y-%m-%d').date()
                title = parts[2]
                events.append((event_start_date, event_end_date, title))
    return events

def compare_with_events (start_date, end_date, events):
    print(f"\ncomparing your {the_thing} with the event list. :D")
    found = False
    longer_events = []
    
    for event_start_date, event_end_date, title in events:
        if start_date >= event_start_date and end_date <= event_end_date:
            longer_events.append(f"{title} - {event_start_date} to {event_end_date}")
            found = True
            
    if found:
        print(f"The following lasted longer than your {the_thing}:")
        for event in longer_events:
            print(event)
    else:
        print(f"Nothing on the list lasted longer. Maybe you'd like to add your {the_thing} to the list. :D")
        print("It was an honor playing with you tonight.")

#=================================================================================================

#start of programm - get inputs

get_thing_input()
get_start_input()
get_end_input()
compare_dates()

#starting comparisons

duration = end_date - start_date
print(f"Your {the_thing} lasted for {duration.days} days.")


#open file - compare
try:
    events = read_compare_list("compare_list.txt") #importing list
except FileNotFoundError:
    print:("File 'compare_list.txt' is missing. Please provide the list.")
    
compare_with_events(start_date, end_date, events)

    