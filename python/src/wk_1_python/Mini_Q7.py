
def sarch_only_study(study_group,dinner_group):
    result = []
    # 결과값 리스트 생성, 초기화
    for i in study_group:
        #더 큰 그룹인 study 그룹을 기준으로 반복문 생성(모든 학생을 비교해보기 위해)
        if (study_group.count(i) != dinner_group.count(i)) and result.count(i) == 0:
            #만약 스터디 그룹의 i 갯수가 디너그룹의 i 개수와 같지 않으며 결과 리스트의 i개수가 0이라면  (두 그룹의 개수가 같지않다면 빠진 학생이 있는것이고
            #                                                                          결과 리스트의 i개수가 0이 아니라면 이미 추가되었기에)
            result.append(i)
            #결과 리스트에 i 추가
        else:
            continue

    return result
    #결과 리턴

def main():
    study_group = ["윤하","동규","동규","진우","겸희","재혁"]#리스트 생성
    dinner_group = ["윤하","동규","겸희","재혁"]
    print(f"스터디그룹 :{study_group}")
    print(f"저녘그룹 :{dinner_group}")#각각의 리스트 출력
    print("저녘을 먹지 못한 학생",sarch_only_study(study_group,dinner_group))#결과값 출력
    

if __name__ == "__main__":
    main()