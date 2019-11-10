class Address:
    def __init__(self,street,city):
        self.street = street
        self.city = city
    def __str__(self):
        return self.street + '-' + self.city
class Proson:
    def __init__(self, name, address):
        self.name = name
        self.address = address
    def introduce(self):
        print( self.name , '@' , self.address)

    def __str__(self): # ham chuyen oject to string
        return self.name
# ----------------
address = Address('123 Ba dinh', 'Ha Noi')
pers1 = Proson('Nguyen van a',address)
pers1.introduce()
print (pers1)





#---------- function define ---------------
def function(self):
    print ('')
    return 0
# -----------------------------------------