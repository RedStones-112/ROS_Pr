def multiply(x, y):
    return (x*y)
def divide(x, y):
    if y == 0 :
        print("0으로 나눌 수 없습니다")
    else:
         return (x/y)
def main():
    x = float(input("첫번째 숫자"))
    y = float(input("두번째 숫자"))
    mul = multiply(x,y)
    div = divide(x,y)
    print(str(x), "*" , str(y), "=", str(mul))
    print(x, "/" ,y, "=", div)
if __name__ == "__main__":
    main()
