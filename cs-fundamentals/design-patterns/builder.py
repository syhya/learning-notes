from abc import ABCMeta, abstractmethod

class Player:
    def __init__(self, face=None, body=None, leg=None, arm=None):
        self.face = face
        self.body = body
        self.leg = leg
        self.arm = arm

    def __str__(self):
        return "%s, %s, %s, %s" % (self.face, self.body, self.leg, self.arm)


class PlayerBuilder(metaclass=ABCMeta):
    @abstractmethod
    def build_face(self):
        pass

    @abstractmethod
    def build_body(self):
        pass

    @abstractmethod
    def build_leg(self):
        pass

    @abstractmethod
    def build_arm(self):
        pass

class SexGirlBuilder(PlayerBuilder):
    def __init__(self):
        self.player = Player()

    def build_face(self):
        self.player.face = "漂亮脸"

    def build_body(self):
        self.player.body = "苗条"

    def build_arm(self):
        self.player.arm = '漂亮胳膊'

    def build_leg(self):
        self.player.leg = '长腿'


class Monster(PlayerBuilder):
    def __init__(self):
        self.player = Player()

    def build_face(self):
        self.player.face = " 怪脸"

    def build_body(self):
        self.player.body = "强壮"

    def build_arm(self):
        self.player.arm = '长胳膊'

    def build_leg(self):
        self.player.leg = '大腿'

# 控制组装顺序


class PlayerDirector:
    def build_player(self, builder):
        builder.build_body()
        builder.build_face()
        builder.build_arm()
        builder.build_leg()
        return builder.player


builder = SexGirlBuilder()
director = PlayerDirector()
p = director.build_player(builder)
print(p)