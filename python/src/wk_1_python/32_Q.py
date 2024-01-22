import random
Id = list(range(1,21))# 1부터 20까지 리스트 생성
random.shuffle(Id) # 리스트 셔플
print("치킨 당첨자 : ",Id[0])# 리스트 첫번째 
print("커피 당첨자 : ",Id[1:4])#리스트 두번째부터 4번째까지
print("축하합니다")
