def average_weight_(height, sex):
    height /= 100
    if sex == "male":
        return round(height*height*22,2)
    elif sex == "female":
        return round(height*height*21,2)
    else:
        print("성별을 다시 입력해주세요")
        return 1
def obesity_(weight,height,sex):
    average_weight = average_weight_(height,sex)
    return int(weight / average_weight * 100)

def main():
    weight = 40
    height = 166
    sex = "male"
    print(f"표준체중은 {average_weight_(height, sex)}kg")
    print(f"비만도는 {obesity_(weight, height, sex)}% 입니다.")
if __name__ == "__main__":
    main()