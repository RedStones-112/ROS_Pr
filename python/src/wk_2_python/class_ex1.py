
class Person:
    def __init__(self,sex, name, age):
        self.sex = sex
        self.name = name
        self.age = age
    def info(self):
        print(self.sex)
        print(self.name)
        print(self.age)



def main():
    P1 = Person("F","lili",20)
    P1.info()

if __name__ == "__main__":
    main()




