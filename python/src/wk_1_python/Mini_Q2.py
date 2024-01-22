def main():
    fruits = ["사과","바나나","체리","포도","오렌지"]
    target = "체리"
    for i in fruits:
        if i == target:
            continue
        else:
            print("과일 :",i)
if __name__ =="__main__":
    main()