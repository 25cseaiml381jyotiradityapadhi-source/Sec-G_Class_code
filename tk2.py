class car:
   def __init__(self,model,make):
     self.make = make
     self.model = model

   def get_data(self):
    return f"Make: {self.make}, Model: {self.model}"

class DatabaseConnection:
   # Default constructor
   def __init__(self):
       self.status = "Disconnected"
       self.port = 5432


   def connect(self):
       self.status = "Connected"
       print(f"status: {self.status} on port {self.port}")
   def __del__(self):
    print(f"")
    
if __name__ == "__main__":
    new_car = car("Camry","Toyota")
    print(new_car.get_data())
    db = DatabaseConnection()
    db.connect()