
class Rectangle:
    def __init__(self,W ,H ):
        self.W = W
        self.H = H
    def surface(self):
        return self.W * self.H
    def round(self):
        return self.W*2 + self.H*2



def main():
    R = Rectangle(30, 50)
    print(R.surface())
    print(R.round())

if __name__ == "__main__":
    main()






