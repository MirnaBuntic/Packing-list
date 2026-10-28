print("Start your holiday preparations the easy way - with a packing list :)")

#Instruktioner till användaren
print("\nType 'add' to add an item.")
print("Type 'delete' to delete an item.")
print("Type 'print' to print out the list.")
print("Type 'exit' to close the program.")


packingList = []

#Kör en while-loop som jag sätter till True så att den alltid kör.
while True:
   
    chooseOption = input("\nWhat do you want to do?").lower() #Använder .lower() för att göra alla bokstäver små, så att brukarens text alltid matchar kommandot.

    #Lägg till i listan
    if chooseOption == 'add':
   
        while True:
            newItem = input("Add something to the list and type 'done' when you are done adding.").lower() 
            
            if newItem == 'done':
                break

            else:
                packingList.append(newItem)
                print(f"'{newItem}' has been added to the list.")

    #Tabort från listan
    elif chooseOption == 'delete':

        while True:
            deleteItem = input("Delete something from the list and type 'done' when you are done deleting.").lower()

            if deleteItem == 'done':
                break

            elif deleteItem in packingList:
                packingList.remove(deleteItem)
                print(f"'{deleteItem}' has been removed from the list.")

            else:
                print(f"'{deleteItem}' is not in the list.")

    #Om brukaren har valt 'print'.
    elif chooseOption == 'print':
        print("This is your packing list: ", packingList)

    #Om brukaren har valt 'exit'.
    elif chooseOption == 'exit':
        exit()

    #Om inget av ovanstående tester är True så printas ett meddelande till brukaren med instruktioner.
    else:
        print("You must type either 'add', 'delete', 'print' or 'exit' to continue.")


