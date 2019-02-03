def greet_coworkers(message):
    more_people = input("Is there another person to greet? Type y for yes and n for no.") 
    more_people = more_people.lower() 

    while (more_people == "y"):
        name = input("What is your coworker's name?")
        print(message, name + "!") # instead of using a hard coded message, we use the passed in one
        more_people = input("Is there another person to greet? Type y for yes and n for no.") 
        more_people = more_people.lower() 
