def main():
    numbers = [7,5,4,2,9,3]
    target = 4
    for i in numbers:
        if i == target:
            print(i,"를 찾았습니다!")
            break
        else:
            print(i)

if __name__ == "__main__":
    main()