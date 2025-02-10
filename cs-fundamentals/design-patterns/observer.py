from abc import  ABCMeta, abstractmethod


# 抽象订阅者
class Observer(metaclass=ABCMeta):
    @abstractmethod
    # notice 是一个Notice类的对象
    def update(self, notice):
        pass


# 抽象发布者
class Notice:
    def __init__(self):
        self.observers = []

    def attach(self, obs):
        self.observers.append(obs)

    def detach(self, obs):
        self.observers.remove(obs)

    def notify(self):
        for obs in self.observers:
            obs.update(self)


# 具体发布者
class StaffNotice(Notice):
    def __init__(self, company_info = None):
        super().__init__()
        self._company_info = company_info

    @property
    def company_info(self):
        return self._company_info

    @company_info.setter
    def company_info(self, info):
        self._company_info = info
        # 推送
        self.notify()


# 具体的订阅者
class Staff(Observer):
    def __init__(self):
        self.company_info = None

    def update(self, notice):
        self.company_info = notice.company_info


# Client
notice = StaffNotice("初始公司信息")
s1 = Staff()
s2 = Staff()
notice.attach(s1)
notice.attach(s2)
notice.company_info = "公司加班！"
print(s1.company_info)
print(s2.company_info)
notice.detach(s2)
notice.company_info = "公司放假！"
print(s1.company_info)
print(s2.company_info)