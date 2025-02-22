from abc import ABCMeta, abstractmethod


class Handler(metaclass=ABCMeta):
    @abstractmethod
    def handle_leave(self, day):
        pass


class GeneralManger(Handler):
    def handle_leave(self, day):
        if day <= 10:
            print("总经理准假%d天" % day)
        else:
            print("不能请假")


class DepartmentManger(Handler):
    def __init__(self):
        self.next = GeneralManger()

    def handle_leave(self, day):
        if day <= 5:
            print("部门经理准假%d天" % day)
        else:
            print("部门经理职权不足")
            self.next.handle_leave(day)


class ProjectManger(Handler):
    def __init__(self):
        self.next = DepartmentManger()

    def handle_leave(self, day):
        if day <= 3:
            print("项目经理准假%d天" % day)
        else:
            print("项目经理职权不足")
            self.next.handle_leave(day)


# Client
day = 7
h = ProjectManger()
h.handle_leave(day)


