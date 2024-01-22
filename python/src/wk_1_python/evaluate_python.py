def evaluate_python_skill(level):
    if (level == '상'):
        print("상")
    elif (level == '중'):
        print("중")
    elif (level == '하'):
        print("하")
    else:
        print("잘못된 입력")
def main():
    python_skill = input("상 중 하 입력")
    evaluate_python_skill(python_skill)
    
if __name__ == "__main__":
    main()