class NoMoreBibim_UdongError(Exception):
    pass
bibim_udong = 30
waiting_no =1
while 1:
    print(f"[남은 우동 : {bibim_udong}]")
    try:
        order = int(input("우동 몇 그릇을 주문하실까요?"))
        if order < 0:
            raise ValueError

        if  order > bibim_udong:
            print("남은 우동보다 주문량이 더 많습니다.")
        else:
            print(f"<대기번호 {waiting_no}> {order} 그릇 주문이 완료되었습니다.")
            waiting_no += 1
            bibim_udong -= order
        if bibim_udong == 0:
            raise NoMoreBibim_UdongError
        
    except ValueError:
        print("수량을 입력해 주세요")
        continue
    
    except NoMoreBibim_UdongError:
        print(("비빔우동이 매진되었습니다."))
        break
    
    
print("오늘의 장사는 여기까지")
    