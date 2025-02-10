class CPU:
    def run(self):
        print("cpu开始运行")

    def stop(self):
        print("cpu停止运行")

class Disk:
    def run(self):
        print("硬盘开始运行")

    def stop(self):
        print("硬盘停止运行")

class Memory:
    def run(self):
        print("内存通电")

    def stop(self):
        print("内存断电")

#  Facade
class Computer:
    def __init__(self):
        self.cpu = CPU()
        self.disk = Disk()
        self.memory = Memory()

    def run(self):
        self.cpu.run()
        self.disk.run()
        self.memory.run()

    def stop(self):
        self.cpu.stop()
        self.disk.stop()
        self.memory.stop()


# client
computer = Computer()
computer.run()
computer.stop()