class glass:
    __a = ""
    __b = ""
    __c = ""
    __d = ""

    def seta(self, a):
        self.__a = a
    def geta(self):
        return self.__a

    def setb(self, b):
        self.__b = b
    def getb(self):
        return self.__b

    def setc(self, c):
        if c < 0:
            print("输入非法")
        else:
            self.__c = c
    def getc(self):
        return self.__c

    def setd(self, d):
        if d < 0:
            print("输入非法")
        else:
            self.__d = d
    def getd(self,d):
        return self.__d

    def neng(self):
        print(self.__a, "的", self.__b, "水杯能存放", self.__c, "分米高容纳", self.__d, "升的液体")

i = glass()
#属性
i.seta("蓝色")
i.setb("不锈钢")
i.setc(5)
i.setd(3)
#行为或功能
i.neng()