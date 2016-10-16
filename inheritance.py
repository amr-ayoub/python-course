class Parent():
    def __init__(self,first,last):
        self.first = first
        self.last = last

    def show_info(self):
        print(self.first)
        print(self.last)
    



class Child(Parent):
    def __init__(self,first,last,toys):
        Parent.__init__(self,first,last)
        self.toys = toys

    def show_info(self):
        #Parent.show_info(self)
        print(self.toys)
    


Amr = Parent("Amr","Ayoub")
#Amr.show_info()


#print(Amr.first)
Yahia = Child("Yahia","Ayoub",3)
Yahia.show_info()

#print(Yahia.last)
#print(Yahia.toys)
