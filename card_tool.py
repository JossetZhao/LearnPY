"""
#!shebang???

"""
card_list = []

def show_menu():

    #TODO show menu
    print("+" * 50)
    print("Welcome to contact management system!")
    print("")
    print("1. Add a new contact")
    print("2. Show all contacts")
    print("3. Find a contct")
    print("")
    print("0. Exit")
    print("+" * 50)

def new_card():
    """Add a new contact"""
    print("-" * 50)
    print("Add new contact")

    #1. inform user type in contact info
    """批量修改变量名：光标放在变量名任意字母中间，右键，rename symbol，直接回车，所有变量名都改了，shift+enter，可多选可全选"""
    name = input("enter name")
    phone = input("enter phone")
    email = input("enter email")
    #2. use 1 build a contact dict
    card_dict = {"name":name,
                 "phone":phone,
                 "email":email}
    #3. add cintact dict into card_list
    card_list.append(card_dict)

    print(card_list)
    #4. inform user success
    print("%s's contact has been successfully added." % name)

def show_all():
    """Show all contacts"""
   
    print("-" * 50)
    print("Show all contacts")

    #whether there is any record，if not，inform user and return to menu
    if len(card_list) == 0:
        print("No records, try add new contact")

        return #return后面没有内容：到调用函数的位置执行 后面的code不会被执行

    #iteration 
    for name in ["name", "phone", "email"]:
        print(name, end="\t\t")

    print("") #增加换行

    print("=" * 50)

    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t" % (card_dict["name"],card_dict["phone"],card_dict["email"]))
def find_one():
    """Find a contct"""
    print("-" * 50)
    print("Find a contact")

    #1. inform user to type in name they want to find
    find_name = input("Enter the name of contact you want to find: ")
    #2. iterate card list find the name, if not found, inform user not found
    for card_dict in card_list:

        if card_dict["name"] == find_name:

            print("Found it")

            print("name\t\tphone\t\temail\t\t")
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t" % (card_dict["name"],card_dict["phone"],card_dict["email"]))

            # delete or change when find the record 
            deal_card(card_dict)
            break

    else:

        print("Didn't find %s." % find_name)   

def deal_card(find_dict):
    #print(find_dict)

    action_str = input("Select [1] Modify [2] Delete [0] Return")
    
    if action_str == "1":
        #name_mod = input_card_info(find_dict["name"], "name_mod")
        find_dict["name"] = input_card_info(find_dict["name"], "name_mod")
        find_dict["phone"] = input_card_info(find_dict["phone"], "phone_mod")
        find_dict["email"] = input_card_info(find_dict["email"], "email_mod")
    
        print("%s's contact has been modifoed!" % find_dict["name"])
    elif action_str == "2":
        
        card_list.remove(find_dict)
        print("%s's contact has been deleted!" % find_dict["name"])

def input_card_info(dict_value, tip_msg):
    """

    """

    #1. inform user type in content
    result_str = input(tip_msg)

    #2. check whether user typed in, if yes, return result
    if len(result_str) > 0:
        
        return result_str

    #3. if not, return origin value in dict
    else:
        return dict_value