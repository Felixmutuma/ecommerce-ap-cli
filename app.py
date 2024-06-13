from cli import auth, user, admin
from data import database

def main():
    database.initialize_db()
    
    while True:
        print("** WELCOME TO KAMJANJA T-SHIRTS HUB!***")
        print("1. CREATE ACCOUNT")
        print("2. LOGIN AS A USER")
        print("3. LOGIN AS ADMIN")
        print("4. QUIT")


        choice = input("Choose an option: ")
        
        if choice == '2':
            email = input("Email: ")
            password = input("Password: ")
            user_data = auth.authenticate_user(email, password)
            if user_data:
                print("**LOGIN SUCCESSFULL***")
                while True:
                    print("1. View all T-Shirts on the store")
                    print("2. Purchase a T-Shirt")
                    print("3. Rate a T-Shirt")
                    print("4. Logout")
                    user_choice = input("Choose an option: ")
                    
                    if user_choice == '1':
                        tshirts = user.view_tshirts()
                        for tshirt in tshirts:
                            print(tshirt)
                    elif user_choice == '2':
                        tshirt_id = input("Enter T-Shirt ID: ")
                        user.purchase_tshirt(user_data[0], tshirt_id)
                    elif user_choice == '3':
                        tshirt_id = input("Enter T-Shirt ID: ")
                        rating = input("Enter Rating: ")
                        user.rate_tshirt(tshirt_id, rating)
                    elif user_choice == '4':
                        print('***LOGGED OUT SUCCESSFULLY!***')
                        break
                    else:
                        print("INVALID OPTION")
            else:
                print("**Invalid login credentials.**")
        
        elif choice == '3':
            username = input("Username: ")
            password = input("Password: ")
            admin_data = auth.authenticate_admin(username, password)
            if admin_data:
                print("***LOGIN SUCCESSFUL***")
                while True:
                    print("1. Add T-Shirt")
                    print("2. Update T-Shirt")
                    print("3. Delete T-Shirt")
                    print("4. View All T-Shirts")
                    print("5. Logout")
                    admin_choice = input("Choose an option: ")
                    
                    if admin_choice == '1':
                        name = input("Name: ")
                        color = input("Color: ")
                        size = input("Size: ")
                        price = float(input("Price: "))
                        category = input("Category: ")
                        admin.add_tshirt(name, color, size, price, category)
                    elif admin_choice == '2':
                        tshirt_id = input("Enter T-Shirt ID: ")
                        name = input("Name: ")
                        color = input("Color: ")
                        size = input("Size: ")
                        price = float(input("Price: "))
                        category = input("Category: ")
                        admin.update_tshirt(tshirt_id, name, color, size, price, category)
                    elif admin_choice == '3':
                        tshirt_id = input("Enter T-Shirt ID: ")
                        admin.delete_tshirt(tshirt_id)
                    elif admin_choice == '4':
                        tshirts = admin.view_all_tshirts()
                        for tshirt in tshirts:
                            print(tshirt)
                    elif admin_choice == '5':
                        print('***LOGGED OUT SUCESSFULLY***')
                        break
                    else:
                        print("Invalid option.")
            else:
                print("**INVALID CREDENTIALS**")
        elif choice == "1":
            name = input("Name: ")
            email = input("Email: ")
            password = input("Password: ")
            dob =  (input("D.O.B: "))
            user.create_user(name,email,password,dob)

        elif choice =='4':
            print('**GOODBYE***')
            break
        else:
            print("Invalid choice.")
            

if __name__ == "__main__":
    main()
