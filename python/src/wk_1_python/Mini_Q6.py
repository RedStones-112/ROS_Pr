def make_decimal_list(decimal_list,target):#타겟보다 작은 소수의 리스트 생성
    i = 0
    j = 0
    # 3이하의 숫자일 시 i, j가 선언되지않아 line 8, 10에서 에러발생하므로 초기화  
    for i in range(target-1, 1,-1):
        #타겟은 제외한 소수리스트를 만들어야하기에 target-1 부터 2 까지 -1씩 내려가며 확인
        for j in range(i-1, 1, -1):
            #내려가는 숫자인 i를 i보다 작은 숫자인 j로 나눴을때 나머지값이 0이면 소수가 아니기에 break
            if i%j == 0:
                break
        if j == 2 and i !=4:
            #break 되지않고 끝가지 진행되었으면 j값이 2이기에 j가 2라면 그리고 i가 4가 아니라면 (마지막에 오직 2로만 나뉘어지는 4를 예외처리, 4이외의 2의 배수는 4이상으로 나눠지기에 문제없음)
            decimal_list.append(i)
            #i를 소수 리스트에 추가
    return decimal_list #소수리스트 리턴

def sum_decimal(decimal_list,target):
    #소수 리스트끼리 합쳐 타겟이 나올시 리턴
    for i in decimal_list:
        #소수리스트 값을 하나씩 꺼내오는 i
        for j in decimal_list:
            #소수리스트 값을 하나씩 꺼내오는 j
            if i+j == target and i != j:
                #만약 i + j값이 타겟값이라면
                return i, j
                # i,j 리턴

def main():
    target = 62
    #타겟
    decimal_list =[]
    #소수가 들어갈 리스트 생성
    decimal_list = make_decimal_list(decimal_list, target)
    #소수리스트를 만들어주는 함수 호출
    result = sum_decimal(decimal_list, target)
    # result 값에 답을 담아주는 함수 호출
    if result == None:
        #만약 result가 None 이면 (답이 나오지않아 None값이 나오면 에러가 나지않도록 변경)
        result = []
    print(target, list(result))
    #최종 결과값 출력
    


if __name__ == "__main__":
    main()