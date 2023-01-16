import card_tool
#infinite loop, user decide when to quit loop
while True:

    # TODO show menu(delete when it is done)
    card_tool.show_menu()
    
    action_str = input("enter your selection:")
    print("Your selection is [%s]." % action_str)
    #1,2,3 actions of cards
    if action_str in ["1", "2", "3"]:

        #add
        if action_str == "1":
            card_tool.new_card()

        #show all
        elif action_str == "2":
            card_tool.show_all()
       
        #find
        elif action_str =="3":
            card_tool.find_one()
            

        pass
    #0 exit
    elif action_str == "0":
        print("Welcome back!")
        break

        pass

    #other input inform wrong
    else:
        print("Not an option, select another one.")

        pass