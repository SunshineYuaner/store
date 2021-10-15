class computer:
    __a = ""
    __b = ""
    __c= ""
    __d= ""
    __e= ""

    def seta(self,a):
        if a<0:
            print("输入非法")
        else:
            self.__a=a
    def geta(self):
        return self.__a

    def setb(self,b):
        self.__b = b
    def getb(self):
        return self.__b

    def setc(self,c):
        self.__c=c
    def getc(self):
        return self.__c

    def setd(self,d):
        if d < 0:
            print("输入非法")
        else:
            self.__d=d
    def getd(self):
        return self.__d

    def sete(self,e):
        self.__e=e
    def gete(self):
        return self.__e

    def neng(self):
        print("电脑屏幕",self.__a,"价格",self.__b,"cpu型号",self.__c,"内存大小",self.__d,"待机时长",self.__e)

i = computer()
i.seta(15.6)
i.setb(5000)
i.setc(4)
i.setd(16)
i.sete(10)

i.neng()
