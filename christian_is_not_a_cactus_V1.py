#defining variables, importing stuff
import time
glass = 0
tank = 0
help = 0
tank_valve = 0



#functions
def water_question():
    global help
    while True:
        help = input("Will you water him? Y/N ").strip().lower()
        if help in["ja", "j", "yes", "y", "true", "t"]:
            print("I am so happy, that you want to help Christian to drink more water. Let's continue!")
            return True
            break
        elif help in ["nein", "n", "no", "false", "f"]:
            print("Without your help, Christian dies of thirst! Good bye. D':")
            return False
        else:
            print("Invalid input. Please enter 'Y' or 'N'. ")
            
def check_glass():
    while True:
        glass = int(input("place holder for sensor. Please provide a glass for Christian!(Sensor is given between 200 and 400)"))
        if glass < 200:
            print("Please provide a glass for Christian.")
            return False
        elif glass > 400:
            print("Please provide an empty glass for Christian.")
            return False
        else:
            print("Glass successfully provided.")
            return True
            
def check_tank():
    while True:
        tank = int(input("place holder for sensor. Tank's full at 2000."))
        if tank < 200:
            print("The watertank's empty. Please fill the tank.")
        else:
            print("There's enough water in the tank.")
            return True
        

def fill_glass():
    if check_glass and check_tank: 
        global tank_valve 
        tank_valve = 1
        print("Glass is getting filled.")
        
def christian_drinking():
    while True:
        time.sleep(2)
        if not check_glass():
            print("Christian drank his water")
        else:
            print("Christian, drink your water!")
            christian_needs_water()
            

def christian_needs_water():
    check_tank()
    check_glass()
    fill_glass()
        

#greeting and instructions
print("Welcome to 'Christian is not a cactus'.")
print("Christian is always thirsty.")
water_question()
if help:
    print(" ")
    print("Instructions:")
    print("Christian needs to drink two liters of water a day.") 
    print("His glas fits 200ml. Whenever it's empty, refill it.")
    print("If Christian forgets to drink his water, 'Christian is not a cactus' will remind him to drink it.")

#filling empty glass
christian_needs_water()

#Checking if Christian drinks his water and annoy him, if not.
christian_drinking()
    