class Bmwcar:
    def __init__(self,name,color,cc) -> None:
          self.name = name
          self.color = color
          self.cc = cc

    def shifting_gear(self):
             print(self.name,'Gear is shifting')
    
    @staticmethod
    def kms_to_miles(kms):
                print(kms*1.6)

def main():
    c = Bmwcar('BMW','Black',1999)
    c.shifting_gear()  #bmwcar.shifting_gear(c)
    Bmwcar.kms_to_miles(2) #Bmwcar.kms_to_miles(2)
    c.kms_to_miles(2)


if __name__ == '__main__':
   main()