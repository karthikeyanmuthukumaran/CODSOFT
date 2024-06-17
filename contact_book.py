contacts={}
# SCENERIO ABOUT CONTACT BOOK!!!
def dis_contact():
    print("contact name \t \t contact number")
    for key in contacts:
        print("{} \t \t {}".format(key,contacts.get(key)))


while True:
    print("1.ADD  A CONTACT")
    print("2.SEACH A CONTACT")
    print("3.DISPLAY THE CONTACT")
    print("4.UPDATE A CONTACT")
    print("5.DELETE A CONATCT ")
    
    print("*****CONTACT BOOK*****")
    choice=int(input("enter your choice :"))

    # ADD A NEW CONTACT 
    if choice == 1:
        contact_name=input("enter contact person name :")
        contact_no=int(input("enter contact number :"))
        contacts[contact_name]=contact_no
    
    #SEARCH A CONTACT
    elif choice == 2:
        search_name=input("enter the contact name to be search:")
        if search_name in contacts:
            print(search_name," 's contact number is",contacts[search_name])
        else:
            print("search name not found in contact!!")
    
    #DISPLAY CONTACT
    elif choice == 3:
        if not contacts:
            print("empty contact book")
        else:
            dis_contact()
    
    #UPDATE CONTACT
    elif choice == 4:
        upd_name=input("enter contact name to b edited :")
        if upd_name in contacts:
            ph_num=input("enter the number")
            contacts[upd_name]=ph_num
            print(" contact updated ")
            dis_contact()
        else:
            print("conatct name not found")

    #DELETE CONTACT
    elif choice== 5:
        del_contact=input("enter the contact you want to delete :")
        if del_contact in contacts:
            contacts.pop(del_contact)
            dis_contact()
        else:
            print("contact name not found")
     

    else:
        print("invalid choice!!!, please enter the valid choice to perform !!!")