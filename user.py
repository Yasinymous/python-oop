'''
kullanici ve kullanıcı islemleri bulunuyor.
kullanici veri yapisi
kullanici fonksiyonlari
'''
from database import Data

class User:

    def __init__(self, uid, name, last_name, age):
        self.uid = uid
        self.name = name
        self.last_name = last_name
        self.age = age
    def Add_User(db):   
        print('ADD USER OPERATİON')
        name = input('First Name:')
        last_name = input('Last Name:')
        age = int(input('Age:'))
        new_uid = int(Data.Control_Data_UID(db))
        new_user = User(new_uid,name,last_name,age)
        print ('uid {}, name {}, last_name {}, age {}'.format(new_user.uid, new_user.name, 
                                                        new_user.last_name, new_user.age))   
        Data.Add_Data(new_user,db)  
        print('\n')                                           
        return new_user

    def Delete_User(db):    
        print('DELETE USER OPERATİON')
        uid = int(input('Detele uid:'))
        if True == Data.Search_Data(uid,db):
            Data.Delete_Data(uid,db)
        else:
            print("Not Found!!!")
        print('\n')

    def List_User(db):
        print('LİST USER OPERATİON')
        Data.List_Data(db)
        print('\n')


'''
    def Print_User(self, uid):

    def Search_User(self, uid):    
'''

