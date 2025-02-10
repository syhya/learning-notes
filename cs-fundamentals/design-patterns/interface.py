# 继承
# class Payment:
#     def pay(self, money):
#         raise NotImplementedError

from abc import ABCMeta, abstractmethod
# 接口： 若干抽象方法的集合。
# 作用：限制实现接口的类必须按照接口给定的调用方式实现这些方法；对高层模型隐藏了类的内容实现。


class Payment(metaclass=ABCMeta):
    # abstract class
    @abstractmethod
    def pay(self, money):
        pass


class Alipay(Payment):
    def pay(self, money):
        print("支付宝支付%d元." % money)


class WechatPay(Payment):
    def pay(self, money):
        print("微信支付%d元." % money)


p = Alipay()
p.pay(100)

p = WechatPay()
p.pay(100)


class User:
    def show_name(self):
        pass


class VIPUser(User):
    def show_name(self):
        pass


u = User()


def show_user(u):
    res = u.show_name()


class LandAnimal(metaclass=ABCMeta):
    @abstractmethod
    def walk(self):
        pass

class WaterAnimal(metaclass=ABCMeta):
    @abstractmethod
    def swim(self):
        pass


class SkyAnimal(metaclass=ABCMeta):
    @abstractmethod
    def fly(self):
        pass


class Tiger(LandAnimal):
    def walk(self):
        print("老虎走路")


# 继承不同的接口
class Frog(LandAnimal, WaterAnimal):
    def walk(self):
        pass

    def swim(self):
        pass