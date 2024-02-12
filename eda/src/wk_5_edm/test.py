

temper_out = 28
temper_in = temper_out
on_board = [0,0,1,1,1,1,1]

t1 = 18
t2 = 26
a = 10 # 온도상승 비용
b = 8 # 온도유지 비용
t = 0
###### int(abs(lenth / 2) + 0.5) # 정상적인 반올림방식 
answer = 0



if temper_out < t1:
    target_t = t1
    
elif temper_out > t2:
    target_t = t2



while 1:
    c = 0
    if on_board == [] or len(on_board) == 1:
        break
    now = on_board[0]

    if now == 1: #사람이 있어서 온도유지
        try:
            lenth = len(on_board[:on_board.index(0)])
            del(on_board[:on_board.index(0)])
        except:
            lenth = len(on_board)
            del(on_board[:])

        val1 = lenth * b
        val2 = int(abs((lenth - abs(temper_in - target_t)) / 2) + 0.5) * a
        if int(abs((lenth - abs(temper_in - target_t)))) % 2 != 0 :
            c = 1
        else:
            c = 0
            
        if val2 < val1: # 유지비용과 재난방 비용 비교
            answer += val2

        else:
            answer += val1

        temper_in = target_t + c

    else: # 사람이 없어서 유지할지 재가동할지 선택
        try:
            lenth = len(on_board[:on_board.index(1)])
            del(on_board[:on_board.index(1)])
        except:
            lenth = len(on_board)
            del(on_board[:])

        # 재난방 비용 계산 1
        if abs(temper_in - temper_out) <= lenth / 2 and temper_in <= t2 and temper_in >= t1:
            val1 = int(abs((lenth - abs(temper_in - target_t)) / 2) + 0.5) * a##########
            
        # 계산 2
        else:
            val1 = abs(target_t - temper_out) * a
            

        # 유지 비용
        if temper_in <= t2 and temper_in >= t1:
            val2 = int(abs((lenth - abs(temper_in - target_t)) / 2) + 0.5) * b 
        else:
            val2 = ((abs(temper_in - target_t) * a) + 
                    (int(((lenth - abs(temper_in - target_t)) / 2) + 0.5) * b ))
        
        if int(abs((lenth - abs(temper_in - target_t)))) % 2 != 0 :
            c = 1
        else:
            c = 0


        
        

        if val2 < val1: # 유지비용과 재난방 비용 비교
            answer += val2

        else:
            answer += val1
        temper_in = target_t + c


    
        
print(answer)


# 0 -> 1
#       다음 사용자 입장전 기간동안 유지비용이 재난방비용보다 비싼가? 
#               계속유지
#               정지후 재난방
#               ! 특이 경우 
# 1 -> 0
#       유지 (20 21 20 21)




# 유지비용이(b) 재난방(a) 비용보다 비쌀경우



#에어컨의 소비전력은 현재 실내온도에 따라 달라집니다. 
#에어컨의 희망온도와 실내온도가 다르다면 매 분 전력을 a만큼 소비하고, 
#희망온도와 실내온도가 같다면 매 분 전력을 b만큼 소비합니다. 
#에어컨이 꺼져 있다면 전력을 소비하지 않으며, 
#에어컨을 켜고 끄는데 필요한 시간과 전력은 0이라고 가정합니다.


#