def add(x, y):
    return (x+y)
def subtract(x, y):
    return (x-y)
def main():
    x = int(input("첫번째 숫자"))
    y = int(input("두번째 숫자"))
    total = add(x,y)
    sub = subtract(x,y)
    print(str(x), "+" , str(y), "=", str(total))
    print(x, "-" ,y, "=", subtract)
if __name__ == "__main__":
    main()
