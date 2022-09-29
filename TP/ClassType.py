class Hello:
    def world(self) -> int:
        return 7


class World:
    pass


hello: "World" = Hello()
world: "World" = World()


# def foo(ins: Hello) -> int:
#     return ins.world()


# print(foo(hello))
# print(foo(world))

# * class type 심화

from typing import Optional

# 클래스 안에서는 자신을 가리키려면 콤마를 사용해야 함
class Node:
    def __init__(self, data: int, node: Optional["Node"]):
        self.data = data
        self.Node = node


node2 = Node(12, None)

node1 = Node(27, node2)

node0 = Node(30, node1)

print(node0.data)
