import random#랜덤모듈에서 sample 함수를 사용하기위해 선언

def main():
    person = [list(range(1,31)), random.sample(range(1,51),30)]#이중 리스트를 활용 첫번째 리스트에는 학생들의 번호 두번째 리스트에는 1이상 51미만인 리스트에서 겹치지않게 30개를 선택헌 2,30 이중리스트
    pick = 0#당첨된 사람의 수를 알기위한 변수
    for i in range(len(person[0])):#첫번째리스트인 학생들의 숫자 개수만큼(30개) 반복하는 for문
        if 10 <= person[1][i] <= 17:#10이상 17이하일경우 당첨결과변수를 "당첨"으로 변경 그리고 pick변수 +1
            result = "당첨"
            pick+=1
        else:
            result = ""#아닐경우 결과변수 비우기
        
        print(f"[{result}] {i}번학생 (좋아하는 숫자 : {person[1][i]} )")#각 학생의 결과 출력
    print("총 당첨 인원 :",pick)#총 당첨인원 출력
if __name__ == "__main__":
    main()