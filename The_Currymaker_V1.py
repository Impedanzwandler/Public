#initializing variables
is_curry = 0
is_gravy = 0
is_protein = 0
is_veggies = 0
is_onions = 0
is_garlic = 0
is_ginger = 0
liquids = 0
is_liquids = 0
is_salt = 0
is_pepper = 0
is_coriander = 0
is_cumin = 0
is_paprika = 0
is_tumeric = 0
is_cardamon = 0
is_chili = 0
is_nutmeg = 0
is_cinnamon = 0

#start of programm
print("Welcome to the currymaker!")
print("This programm will help you to dose your spices for an Indian style curry or gravy.")

#curry_function
def get_curry_inputs():
        while True:
            try:
                is_protein = int(input("Please type the amout of meat or legumes in grams:"))
                if is_protein < 0:
                    print("Please enter a postive number.")
                    continue
                break
            except ValueError:
                print("Your input is invalid. Please make sure to only use natural numbers.")

        while True:
            try:
                is_veggies = int(input("Please type the amount of vegetables in grams:"))
                if is_veggies < 0:
                    print("Please enter a postive number.")
                    continue
                break
            except ValueError:
                print("Your input is invalid. Please make sure to only use natural numbers.")

        if is_veggies == 0 and is_protein > 0:
            print("Some vitamines won't hurt you. :)")
                

 #checking if input is valid.
        if is_protein + is_veggies == 0:
            print("You cannot make curry out of love and air.")
        else:
            print(f"You use {is_protein} grams worth of protein and {is_veggies} grams worth of vegetables for your curry.")
#checking if amounts are plausible
        if is_protein + is_veggies > 20000:
            print("I don't know, if this recipe is suited for industrial amounts.¯\_(ツ)_/¯")
        if is_protein + is_veggies > 10000:
            print("Make sure to provide a pot, that is large enough.")
        return is_protein, is_veggies
            

while True:
#input curry or gravy
    choice = input("Please type 'curry' or 'gravy' to make a decision: ").lower().strip()
    is_curry = (choice == "curry") 
    is_gravy = (choice == "gravy")

#check valid input
    if not (is_curry or is_gravy):
        print("Invalid input! Please type either 'curry' or 'gravy'!")
    else:
        print(f"You picked {'curry'if is_curry else 'gravy'}")

#calculation of curry; call of curry function
    if is_curry:
        is_protein, is_veggies = get_curry_inputs()
   
    
#proceed calculation of bulbous plants and ginger, part of is_curry and is_gravy calculation
    while True:
        try:
            is_onions = int(input("Please type the amount of onions in grams:"))
            if is_onions < 0:
                print("Please enter a postive number.")
                continue
            break
        except ValueError:
            print("Your input is invalid. Please make sure to only use natural numbers.")

    if is_onions == 0:
        print("There's no way to make curry without onions!ò_ó")
    if is_onions > 20000 and is_protein + is_veggies > 20000:
        print("You do want to push the limits, don't you?")
    if is_onions > 20000 and is_protein + is_veggies < 20000:
        print("I don't know, if this recipe is suited for industrial amounts. ¯\_(ツ)_/¯")

    while True:
        try:          
            is_garlic = int(input("Please provide the amout of garlic cloves:"))
            if is_garlic < 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Your input is invalid. Please make sure to only use natural numbers.")

    if is_garlic > 10 <50 < 200:
        print("That much?")
    if is_garlic  > 50 <200:
        print("I hope you live on a desert island, otherwise I'm sorry for your fellow humans.")
    if is_garlic > 200:
         print("Lord, have mercy...")

    while True:
        try:
            is_ginger = int(input("Please provide the amout of ginger you want to use in cm:"))
            if is_ginger < 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Your input is invalid. Please make sure to only use natural numbers.")

        if is_ginger > 20:
            print("I though you wanted to make a dish, not a tea.")

#calculations of Liquids needed
    liquids = is_protein + is_onions + is_veggies
    is_liquids = 2 * liquids
    print(f"You need {is_liquids} ml of liquids. You can use broth, coconutmilk, cream or water to your liking. :)")

#calculations of spices
    
    is_salt = liquids * 0.01
    is_pepper = liquids * 0.02
    is_coriander = liquids * 0.02
    is_cumin = liquids * 0.02
    is_paprika = liquids * 0.02
    is_tumeric = liquids * 0.02
    is_cardamon = liquids * 0.02
    is_chili = liquids * 0.01
    is_nutmeg = liquids * 0.02
    is_cinnamon = liquids * 0.02

    print("You'll need")
    print(f"{is_salt} grams worth of salt,")
    print(f"{is_pepper} grams worth of pepper,")
    print(f"{is_coriander} grams worth of coriander,")
    print(f"{is_cumin} grams worth of cumin,")
    print(f"{is_paprika} grams worth of paprika,")
    print(f"{is_tumeric} grams worth of tumeric,")
    print(f"{is_cardamon} grams worth of cardamon,")
    print(f"{is_chili} grams worth of chili,")
    print(f"{is_nutmeg} grams worth of nutmeg,")
    print(f"and {is_cinnamon} grams worth of cinnamon.")
    print("These amounts are recommendations for ground spices. Feel free to adjust them to you liking. :) Have fun, cooking curry. :)")
