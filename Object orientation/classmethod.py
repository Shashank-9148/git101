class BMWcar:
    def __init__(self,name,cc,color) -> None:
        self.name = name
        self.cc = cc
        self.color = color
    
    def x1(cls):
        return cls('X1',1999,'Black')

    def series5(cls):
        return cls('Series5',2998,'White')

    def coupe(cls):
        return cls('Coupe',1499,'Red')

    def display(self):
        print(self.name)
        print(self.cc)
        print(self.color)

def main():
    c1 = BMWcar.x1(BMWcar)
    c2 = BMWcar.series5(BMWcar)
    c3 = BMWcar.coupe(BMWcar)
    c1.display()
    c2.display()
    c3.display()

if __name__ == '__main__':
    main()

        