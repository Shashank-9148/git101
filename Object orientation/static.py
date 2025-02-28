#program without static variable

class Citizen:
    def __init__(self,name,age,gender,state,nationality) -> None:
             self.name = name
             self.age = age
             self.gender = gender
             self.state = state
             self.nationality = nationality

    def display(self):
          print(self.name)
          print(self.age)
          print(self.gender)
          print(self.state)
          print(self.nationality) 

def main():
       rohit = Citizen('Rohit',23,'M','Kar','Indian')
       smitha = Citizen('Smitha',22,'F','Kar','Indian')
       rita = Citizen('Rita',24,'F','Kar','Indian')

       rohit.display()
       smitha.display()
       rita.display()

if __name__ =='__main__':
       main()


#using static variable
class Citizen:
    nationality = 'Indian'  #static variable
    def __init__(self,name,age,gender,state) -> None:
              self.name = name
              self.age = age
              self.gender = gender
              self.state = state
              

    def display(self):
         print(self.name)
         print(self.age)
         print(self.gender)
         print(self.state)
         print(self.nationality)
def main():
       r = Citizen('Rohit',27,'M','Kar')
       s = Citizen('Smitha',24,'F','Kar')
       v = Citizen('Vidya',25,'F','Kar')
       r.display()
       s.display()
       v.display()

if __name__ == '__main__':
       main()              
                      