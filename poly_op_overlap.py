class Vector2D:
    def __init__(self,x: float,y: float):
        self.x=x
        self.y=y

    #Overloads'+'
    def __add__(self,other):
        if isinstance(other,Vector2D):
            return Vector2D(self.x + other.x,self.y + other.y)
        return NotImplemented

    #Overloads'=='
    def __eq__(self,other):
        if isinstance(other,Vector2D):
            return self.x == other.x and self.y == other.y
        return False

    #overloads '*' for scalar multiplication: vector * scalar
    def __mul__(self,scalar):
        if isinstance(scalar,(int,float)):
            return Vector2D(self.x*scalar, self.y*scalar)
        return NotImplemented

    #Overloads '*' when the object if on the right: scalar * vector
    def __rmul__(self, scalar):
        return self.__rmul__(scalar)
    

    #Readable representation 
    def __repr__(self):
        return f"Vector2D({self.x},{self.y})"

    #usage 
v1=Vector2D(2,3)
v2=Vector2D(5,7)

print(v1+v2)
print(v1*3)
print(4*v1)
print(v1==v2)