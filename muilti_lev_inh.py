class A:
    def showA(self):
        print("class A")


class B(A):
    def showB(self):
        print("class B")


class C(B):
    def showC(self):
        print("class C")


class D(C):
    def showD(self):
        print("class D")


obj = D()

obj.showA()
obj.showB()
obj.showC()
obj.showD()