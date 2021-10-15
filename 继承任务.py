# 定义手机类
# class oldPhone:
#     __pp = ""
#
#     def setpp(self,pp):
#         self.__pp =pp
#     def getpp(self):
#         return  self.__pp
#
#     def call(self,name):
#         print("正在给",name,"打电话...")
#
# class newPhone(oldPhone):
#     def call1(self,name):
#         oldPhone.__pp = "华为"
#         print("品牌为：", oldPhone.__pp, "的手机很好用...")
#         print("语音拨号中...")
#         super().call(name)
#
# i = newPhone()
# i.call1("圆圆")


# 定义厨师类
# 父类
# class cook:
#     __name = ""
#     __old = 0
#
#     def setName(self,name):
#         self.__name = name
#     def getName(self):
#         return self.__name
#
#     def setOld(self,old):
#         if old < 0 and old >100:
#             print("输入非法")
#         else:
#             self.__old = old
#     def getOld(self):
#         return self.__old
#
#     def cooker(self):
#         print("蒸饭没有方法，该怎么搞怎么搞")
#
# # 子类
# class cook1(cook):
#     def cooker1(self):
#         print("炒菜没有方法，该怎么搞怎么搞")
#
# # 子类的子类
# class cook2(cook1):
#     def cook3(self):
#         super().cooker1()
#         print("该怎么搞怎么搞,炒菜没有方法")
#         cook.__name = "张三"
#         cook.__old = 16
#         print(cook.__name,cook.__old,"蒸饭炒饭")
#
# # 子类的子类
# i2 = cook2()
# i2.cook3()


# # 人类
class people:
    old = 0
    gender = ""
    name = ""


# 工人类
class worker(people):
    def work(self):
        print("工人", self.name, self.gender, self.old, "岁,职责就是干活")


# 学生类
class student(people):
    sNumber = ""

    def study(self):
        print("学生", self.name, self.gender, self.old, "岁,", "学号:", self.sNumber, "喜欢学习和唱歌")


# 工人类
i1 = worker()
i1.old = 21
i1.gender = "男"
i1.name = "张三"
i1.work()

# 学生类
i2 = student()
i2.old = 20
i2.gender = "女"
i2.name = "李四"
i2.sNumber = "201905030136"
i2.study()
