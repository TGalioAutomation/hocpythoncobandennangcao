class Product:
    def __init__(self,code,name,price):
        self.code = code
        self.name = name
        self.price = price
    def getname(self):
        print self.name
        self.pr(self.name)
    def setname(self,newname):
        self.name = newname
    def pr(self,comment):
        print comment
class Sale:
    def __init__(self, product,qty):
        self.product = product
        self.qty = qty
class Basket:
    def __init__(self,sales,date):
        self.sale = sales
        self.date = date
# ----------------------------------------------
p = Product("P001",'Sua vinamilk 5x200ml',270000)
s =Sale(p,2)
print s.product.name, s.qty
basket = Basket([s],'9/11/2019')
print basket.sale[0].product.name
#-------------------------------------------------