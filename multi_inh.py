class A:
    def process(self):
        print("processing in class A")

class B(A):
    def process(self):
        print("Processing in class B")
        super().process()
class C(A):
    def process(self):
        print("Processing in class C")
        
class D(B,C):
    def process(self):
        print("Processinf in class D")
       # super().process() #call the next class in the MRO

d = D()
d.process()