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
    def Add_User(name, last_name, age):     
        print(Data.Control_Data_UID()) 
        new_uid = int(Data.Control_Data_UID())
        new_user = User(new_uid,name,last_name,age)
        print ('uid {}, name {}, last_name {}, age {}'.format(new_user.uid, new_user.name, 
                                                        new_user.last_name, new_user.age))   
        Data.Add_Data(new_user)                                             
        return new_user

'''

    def Delete_User(self, uid):

    def List_User(self):

    def Print_User(self, uid):

    def Search_User(self, uid):    
'''

