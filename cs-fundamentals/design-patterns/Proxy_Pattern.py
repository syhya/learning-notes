from abc import ABCMeta, abstractmethod

class Subject(metaclass=ABCMeta):
    @abstractmethod
    def get_content(self):
        pass

    @abstractmethod
    def set_content(self):
        pass


class RealSubject(Subject):
    def __init__(self, filename):
        self.filename = filename
        f = open(filename, "r")
        print("读取文件内容")
        self.content = f.read()
        f.close()

    def get_content(self):
        return self.content

    def set_content(self, content):
        f = open(self.filename, "w")
        f.write(content)
        f.close()



class VirtualProxy(Subject):
    def __init__(self, filename):
        self.filename = filename
        self.subj = None

    def get_content(self):
        if not self.subj:
            self.subj = RealSubject(self.filename)
        return self.subj.get_content()

    def set_content(self, content):
        if not subj:
            self.subj = RealSubject(self.filename)
        return self.subj.set_content(content)

class ProtectedProxy(Subject):
    def __init__(self, filename):
        self.subj = RealSubject(filename)

    def get_content(self):
        return self.subj.set_content()

    def set_content(self, content):
        raise PermissionError("无写入权限")

# subj = RealSubject("test.txt")
# subj.get_content()


subj1 = VirtualProxy("test.txt")
print(subj1.get_content())

subj2 = ProtectedProxy("test.txt")
subj2.set_content("abc")



