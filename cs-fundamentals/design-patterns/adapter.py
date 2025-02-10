from abc import ABCMeta, abstractmethod


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


class BankPay:
    def cost(self, moneny):
        print("银联支付%d元." % moneny)


class ApplePay:
    def cost(self, moneny):
        print("苹果支付%d元." % moneny)


# 法一： 类适配器:使用多继承
class NewBankPay(Payment, BankPay):
    def pay(self, money):
        self.cost(money)

# 法二 ： 对象适配器： 使用组合
class PaymentAdapter(Payment):
    def __init__(self, payment):
        self.payment = payment

    def pay(self, money):
        self.payment.cost(money)


p = NewBankPay()
p.pay(100)


p1 = PaymentAdapter(ApplePay())
p1.pay(200)

# 组合：在一个类里放入另外一个类的对象

# class A:
#     pass
#
# class B:
#     def __init__(self):
#         self.a = A()