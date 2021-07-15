class Person:
              def _init_(self,name,age):
                            self.name=name
                            self.age=age
                            def my_function(self):
                                          print('Hello my name is '+self.name)
                                          print('I am'+self.age+'year old.')

p1=Person('John',36)
p2=Person('Jean',23)
p2.age=24
p1.my_function()
p2.my_function()
