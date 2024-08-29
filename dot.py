class Dog:
    def __init__(self,name,age,breed,colour):
        self.name=name
        self.age=age
        self.breed=breed
        self.colour=colour


    def bark(self):
        return "Woof!"

    def walk(self) :
        return f"{self.name} who is {self.colour} sits down"   

fido =Dog("lasssie",3,"german","yellow")   
print(fido.breed)       

print(fido.walk())