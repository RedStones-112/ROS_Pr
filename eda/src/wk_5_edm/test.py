

# temperature = 28
# onboard = [0,0,1,1,1,1,1]

# t1 = 18
# t2 = 26
# a = 10
# b = 8
# t = 0
# temperature = -10
# onboard = [0,0,0,0,0,1,0]

# t1 = -5
# t2 = 5
# a = 5
# b = 1
temperature = 11
onboard = [0,1,1,1,1,1,1,0,0,0,1,1]

t1 = 8
t2 = 10
a = 10
b = 1






###### int(abs(lenth / 2) + 0.5) # 정상적인 반올림방식 
answer = -b

temper_in = temperature
if temperature < t1:
    target_t = t1
    
elif temperature > t2:
    target_t = t2


while 1:
    c = 0
    val1 = 0
    val2 = 0
    if onboard == [] or len(onboard) == 1:
        break
    now = onboard[0]
    board_next = abs(now - 1)
    
    try: # 길이 구하기
        lenth = len(onboard[:onboard.index(board_next)])
        del(onboard[:onboard.index(board_next)])
    except:
        lenth = len(onboard)
        del(onboard[:])

    if b >= a/2: # 절반이하
        val1 = int((lenth - abs(temper_in - target_t)) / 
                    2 + 0.5) * a
        try: #다음길이
            next_lenth = len(onboard[:onboard.index(0)])

        except:
            next_lenth = 0
        # (다음길이 > abs(외부온도 - 현재온도) or 다음길이 <= 1) and 
        #(길이 - abs(현재온도 - 경계온도)) % 2 != 0 and b < a:
        if (next_lenth > abs(temperature - temper_in) or next_lenth <=1) and (lenth - abs(temper_in - target_t)) % 2 != 0 and b < a:
            val1 += b - a
        
        # 재난방
        if temper_in == temperature or (abs(
            temper_in - temperature) <= int((lenth / 2)+0.5)):
            val2 = abs(temperature - target_t) * a

        if val1 <= 0:
            val1 = val2 + 1
        elif val2 <= 0:
            val2 = val1 + 1
        if now == 1:# 값처리
            answer += val1
        else:
            if val1 < val2:
                answer += val1
            else:
                answer += val2
        
        temper_in = target_t + lenth % 2
        
    else: # 절반초과
        if temper_in >= t1 and temper_in <= t2:
            val1 = b * lenth
        if temper_in == temperature or (abs(
            temper_in - temperature) <= int((lenth / 2)+0.5)):
            val2 = abs(temperature - target_t) * a
        if val1 <= 0 and val2 <= 0:
            pass
        
        elif val1 <= 0:
            val1 = val2+1
        elif val2 <=0:
            val2 = val1+1
        
        print(val1, val2, answer)
        if now == 1:# 값처리
            answer += val1
        else:
            if val1 < val2:
                answer += val1
            else:
                answer += val2
        temper_in = target_t

            
        

       


    
        
print(answer)












































# if temperature < t1:
#     target_t = t1
    
# elif temperature > t2:
#     target_t = t2



# while 1:
#     c = 0
#     if onboard == [] or len(onboard) == 1:
#         break
#     now = onboard[0]

#     if now == 1: #사람이 있어서 온도유지
#         try:
#             lenth = len(onboard[:onboard.index(0)])
#             del(onboard[:onboard.index(0)])
#         except:
#             lenth = len(onboard)
#             del(onboard[:])

#         val1 = lenth * a
#         val2 = int(abs((lenth - abs(temper_in - target_t)
#                             ) / 2) + 0.5) * b

        

#         temper_in = target_t + c

#     else: # 사람이 없어서 유지할지 재가동할지 선택
#         try:
#             lenth = len(onboard[:onboard.index(1)])
#             del(onboard[:onboard.index(1)])
#         except:
#             lenth = len(onboard)
#             del(onboard[:])

#         # 재난방 비용 계산 1
#         if abs(temper_in - temperature) <= lenth / 2 and temper_in <= t2 and temper_in >= t1:
#             val1 = int(abs((lenth - abs(temper_in - target_t)
#                             ) / 2) + 0.5) * a##########
            
#         # 계산 2
#         else:
#             val1 = abs(target_t - temperature) * a
            

#         # 유지 비용
#         if temper_in <= t2 and temper_in >= t1:
#             val2 = int(abs((lenth - abs(temper_in - target_t)
#                             ) / 2) + 0.5) * b 
#         else:
#             val2 = ((abs(temper_in - target_t) * a) + 
#                     (int(((lenth - abs(temper_in - target_t)) / 2) + 0.5) * b ))
        
#         if int(abs((lenth - abs(temper_in - target_t)))) % 2 != 0 :
#             c = 1
#         else:
#             c = 0


        
        

#         if val2 < val1: # 유지비용과 재난방 비용 비교
#             answer += val2

#         else:
#             answer += val1
#         temper_in = target_t + c


    
        
# print(answer)


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