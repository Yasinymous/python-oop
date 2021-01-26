from user import User
from database import Data

Data.create_table()

#User.Add_User('xxxx','axxxx',30)
User.List_User()
User.Delete_User(5)
User.List_User()

