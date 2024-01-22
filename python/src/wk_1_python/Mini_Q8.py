
def simulation(completion,pace):
    #주어진 리스트를 토대로 걸리는 날짜(결과값)을 구하는 함수 
    result = [0,0,0]
    complet_day = 0
    while 100 >= min(completion):
        complet_day+=1
        for i in range(len(pace)):
            completion[i] += pace[i]
            if completion[i] >= 100 and result[i] == 0:
                result[i] = complet_day
    return result

def print_result(result):
    print("서비스는")
    complit_num = 0
    result.append(-1)#342
    list_days = []
    for i in range( len(result)-1):
        list_days.append(result[i])
        if result[i] < result[i+1] or i+1 == len(result)-1: 
            print(f" {max(list_days)}일차에 {i+1-complit_num}가지")##
            list_days = []
            complit_num += i+1-complit_num
        
    print("완성될 예정입니다.")

def main():
    completion = [41,55,70]
    pace = [25,13,25]#리스트 생성, 초기화
    result = simulation(completion, pace)
    #결과값 구하는 함수 호출
    print_result(result)
    #결과출력 함수

if __name__ == "__main__":
    main()