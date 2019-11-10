# Xay dung mot hinh chu nhat Rect gom 4 properties:
# x1y1: toa do goc trai phia tren hinh chu nhat
# x2y2: toa do phai phia duoi hinh chu nhat
# Xay dung cac phuong thuc cho doi tuong Rect de tinh:
# + kich thuoc ve ngang cua hinh vhu nhat
# + kich thuoc ve doc hinh chu nhat
# + Dien tinh hinh chu nhat
# + tinh hinh chu nhat con giao nhau cua 2 hinh chu nhat co phan giao)
#######################################################################

# time work 2 hour - 11/10/2019

class Rect:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self._with = 0
        self._hight = 0
        self.S = 0
        # can check x,y truoc do yeu cau ban ve vi tri 2 diem ro rang
        if self.check_input():
            self.calculator_with_hight()
            self.calculator_S()
            self.print_result()
    # --------------------------------------------
    def check_input(self):
        if self.x1 > self.x2:
            print('Error import x1 > x2')
            return False
        if self.y1 < self.y2:
            print('Error import y1 < y2')
            return False
        return True

    # --------------------------------------------
    def calculator_with_hight(self):
        self._with = self.x2 - self.x1
        self._hight = self.y1 - self.y2

    # --------------------------------------------
    def calculator_S(self):
        self.S = self._hight*self._with

    # --------------------------------------------
    def print_result(self):
        print("info Rect: ")
        print('With: ',self._with,'\nHight: ',self._hight,'\nS= ',self.S)
# ---------------/ TINH GIAO /--------------------------
class calculator_Intersect_S(Rect):
    def __init__(self, rect1, rect2):
        self.rect1 = rect1
        self.rect2 = rect2
    def check_phuthuoc(self):
        if self.rect1.x2 <

# Rect( x1, y1, x2, y2)
CN1 = Rect(x1=4,y1=10,x2=5,y2=2)
CN2 = Rect(x1=3,y1=7,x2=5,y2=2)
calculator_In = calculator_Intersect_S(CN1,CN2)

