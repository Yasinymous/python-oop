from user import User
from database import Data

db = 'user_db.db'

Data.create_table(db)
on = True
while (on==True):
    try:
        print('1.Add User(1)\n2.Delete User(2)\n3.List User(3)\n4.Off(4)')
        operation = int(input('Operation(1/2/3/4):')) 
        print('\n')
    except ValueError:
       print("Not an integer! Try again.")
       continue
    else:
        if(operation==4):
            print("Exiting...")
            on = False
        elif(operation==1):
            User.Add_User(db)
        elif(operation==2):
            User.Delete_User(db)
        elif(operation==3):
            User.List_User(db)
        else:
            print('Wrong Operations!!!')
        break 



        
