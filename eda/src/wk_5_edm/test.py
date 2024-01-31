

# temperature = 28
# onboard = [0,0,1,1,1,1,1]

# t1 = 18
# t2 = 26
# a = 10
# b = 8

######################


# temperature = -10
# onboard = [0,0,0,0,0,1,0]

# t1 = -5
# t2 = 5
# a = 5
# b = 1

###################

# temperature = 11
# onboard = [0,1,1,1,1,1,1,0,0,0,1,1]

# t1 = 8
# t2 = 10
# a = 10
# b = 1

##############

# temperature = 11
# onboard = [0,1,1,1,1,1,1,0,0,0,1,1]

# t1 = 8
# t2 = 10
# a = 10
# b = 100


######################################
######################################
######################################

temperature = 40
temperature_in = temperature
onboard = [0,1,1,1,1,1,1,0,0,0,1,1]

t1 = 8.8
t2 = 39.5
a = 40.5
b = 50
#############################

answer = 0

if abs(temperature - t1) >= abs(temperature - t2):
    boundary_temp = t2
    target_temp = t1
else:
    boundary_temp = t1
    target_temp = t2



for i in range(len(onboard)):
    status = "off"
    now = onboard[i]
    try:
        next = onboard[i+1]
    except:
        next = None



    if now == 1 and next == 1 and abs(temperature_in - boundary_temp) <= 1: # 
        if a/2 <= b:
            status = "a"
        else:
            status = "b"
    
    elif now == 1 and next == 0 and abs(temperature_in - boundary_temp) <= 1: # 사용자 없는구간 진입
        pass
    
    elif now == 1 and next == None: # 끝날때  
        pass
    
    elif now == 0:
        lenth = onboard[i:].index(1)
        if lenth <= int(abs(boundary_temp - temperature_in) + 0.5):
            status = "a"
        
    



    if status == "a":
        temperature_in += (target_temp - temperature_in) / abs(
            target_temp - temperature_in)
    elif status == "b":
        pass
    elif status == "off":
        try:
            temperature_in += (temperature - temperature_in) / abs(
                temperature - temperature_in)
        except:
            pass

    print(temperature_in, onboard[i:])



###### int(abs(lenth / 2) + 0.5) # 정상적인 반올림방식 




    
        
print(answer)






























# temper_in = temperature
# if temperature < t1:
#     target_t = t1
    
# elif temperature > t2:
#     target_t = t2


# while 1:
#     c = 0
#     val1 = 0
#     val2 = 0
#     if len(onboard) <= 1:
#         break
#     now = onboard[0]
#     board_next = abs(now - 1)
    
#     try: # 길이 구하기
#         lenth = len(onboard[:onboard.index(board_next)])
#         if lenth == len(onboard):
#             lenth -= 1
#         del(onboard[:onboard.index(board_next)])

#     except:
#         lenth = len(onboard)
#         del(onboard[:])
#     # print(temper_in)
#     if b >= a/2: # 절반이하
#         val1 = int((lenth - abs(temper_in - target_t)) / 
#                     2 + 0.5) * a
#         try: #다음길이
#             next_lenth = len(onboard[:onboard.index(0)])

#         except:
#             next_lenth = 0
#         # (다음길이 > abs(외부온도 - 현재온도) or 다음길이 <= 1) and 
#         #(길이 - abs(현재온도 - 경계온도)) % 2 != 0 and b < a:
#         if (next_lenth > abs(temperature - temper_in) or next_lenth <=1) and (lenth - abs(temper_in - target_t)) % 2 != 0 and b < a:
#             val1 -= a
        
        
#         # 재난방
#         if  (temper_in == temperature or (abs(
#             temper_in - temperature) <= int((lenth / 2) + 0.5))) and (
#                 now == 0):
#             val2 = abs(temperature - target_t) * a

#         if val1 <= 0:
#             val1 = val2 + 1
#         elif val2 <= 0:
#             val2 = val1 + 1
        

#         if val1 < val2:
#             answer += val1
#         else:
#             answer += val2
                
#         print(val1, val2, answer, onboard, lenth)
#         temper_in = target_t + c
        
        
#     else: # 절반초과
#         if temper_in >= t1 and temper_in <= t2:
#             val1 = b * lenth
#         if temper_in == temperature or (abs(
#             temper_in - temperature) <= int((lenth / 2)+0.5)):
#             val2 = abs(temperature - target_t) * a
#         if val1 <= 0 and val2 <= 0:
#             pass
#         elif val1 <= 0:
#             val1 = val2+1
#         elif val2 <=0:
#             val2 = val1+1
        
#         print(val1, val2, answer, onboard, lenth)
        
#         if val1 < val2:
#             answer += val1
#         else:
#             answer += val2
#             del(onboard[0])
#         temper_in = target_t

            
        

       






