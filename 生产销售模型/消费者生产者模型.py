'''
    厨师，造汉堡，每造一个向篮子扔一个，当篮子已经满了时候，停个3秒，判断是否已满，没满，造汉堡
    6个顾客都有10000元，每个汉堡5元。6个人同时抢，当篮子汉堡不够，稍等3秒，然后继续判断是否还有直到钱花完为止。
'''


from threading import Thread
import time

hambuge = 500


class cook(Thread):
    def run(self) -> None:
        global hambuge
        while True:
            if hambuge < 500:
                hambuge = hambuge + 1
            elif hambuge == 500:
                time.sleep(3)
                break


class shopper (Thread):
    shoppername = ''
    count = 0
    money = 100

    def run(self) -> None:
        global hambuge
        while True:
            if self.money > 0:
                if hambuge > 0:
                    hambuge = hambuge - 1
                    self.money -= 5
                    print(self.shoppername, '买了一个汉堡,还剩', self.money, '元')
                    self.count += 1
                else:
                    time.sleep(3)
            else:
                print(self.shoppername, "买了", self.count, '个汉堡')
                break


b1 = shopper()
b1.shopername = '顾客1'
b2 = shopper()
b2.shoppername = '顾客2'
b3 = shopper()
b3.shoppername = '顾客3'
b4 = shopper()
b4.shoppername = '顾客4'
b5 = shopper()
b5.shoppername = '顾客5'
b6 = shopper()
b6.shoppername = '顾客6'


b1.start()
b2.start()
b3.start()
b4.start()
b5.start()
b6.start()
