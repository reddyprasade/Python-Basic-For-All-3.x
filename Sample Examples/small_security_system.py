 # List of users 

known_users = ["Paweł", "Michał", "Julia", "Alice", "Ela", "Miłosz", "Zdzisław", "John", "Filip", "Jakub", "Kuba", "Robert", "Karol", "Carol"]

print(len(known_users))


while True:
    print("Hi! My name is Bob and I am the security system robot.")
    name = input("What is your name?: ").strip().capitalize()   # Capitalize function is used to make the programme sure that user can put a name starting with a small letter.
 
    if name in known_users:
        print("Hello {}!".format(name))
        
        remove = input("Would you like to be removed from the system (yes/no)?: ").lower() # No matter if user write 'yes' or 'no' with lower or capitalized letter

        if remove == "yes":
            print(known_users)
            known_users.remove(name)
            print(known_users)
        elif remove == "no":
            print("No problem, I did not want you to leave anyway.")

    else:
        print("I think I have not seen you on the list {}".format(name))
        add_me = input("Would you like to be added to the system (yes/no)?: ").strip().lower()
        if add_me == "yes":
            known_users.append(name)
        elif add_me == "no":
            print("No worries. You will not be on the list.")
            
        

