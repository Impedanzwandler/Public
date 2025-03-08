#defining variables, importing stuff
import time
glass = 0
tank = 0
help = 0
tank_valve = 0
user = 0



#functions
def water_question():
    global help
    while True:
        help = input("Will you water them? Y/N ").strip().lower()
        if help in["ja", "j", "yes", "y", "true", "t"]:
            print(f"I am so happy, that you want to help {user} to drink more water. Let's continue!")
            return True
            break
        elif help in ["nein", "n", "no", "false", "f"]:
            print(f"Without your help, {user} dies of thirst! Good bye. D':")
            return False
        else:
            print("Invalid input. Please enter 'Y' or 'N'. ")
            
def check_glass():
    while True:
        glass = int(input(f"place holder for sensor. Please provide a glass for {user}!(Sensor is given between 200 and 400)"))
        if glass < 200:
            print(f"Please provide a glass for {user}.")
            return False
        elif glass > 400:
            print(f"Please provide an empty glass for {user}.")
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
        
def user_drinking():
    while True:
        time.sleep(2)
        if not check_glass():
            print(f"{user} drank thier water.")
        else:
            print(f"{user}, drink your water!")
            user_needs_water()
            

def user_needs_water():
    check_tank()
    check_glass()
    fill_glass()
        

#greeting and instructions
print("Welcome to 'not a cactus'.")
user = input ("Please tell me your name.")
print(f"{user} is always thirsty.")
water_question()
if help:
    print(" ")
    print("Instructions:")
    print(f"{user} needs to drink two liters of water a day.") 
    print("Your glass fits 200ml. Whenever it's empty, 'not a cactus' refills it.")
    print(f"If you forget to drink your water, 'is not a cactus' will remind you to drink it.")

#filling empty glass
user_needs_water()

#Checking if user drinks his water and annoy him, if not.
user_drinking()
    