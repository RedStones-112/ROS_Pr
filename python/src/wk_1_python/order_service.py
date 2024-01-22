def point_add(point, money):
    print(f"포인트 충전이 완료되었습니다. 잔액은 {point + money}원 입니다.")
    return point + money
def order(point, total):
    if point >= total:
        print(f"주문이 완료되었습니다. 잔액은 {point - total}원 입니다.")
        return point-total    
    else:
        print(f"잔액이 부족합니다. 잔액은 {point}원 입니다.")
        return point
def order_night(point, total):
    premium = int(total * 0.1)
    if point >= (total + premium):
        print(f"주문이 완료되었습니다. 잔액은 {[point - total]}원 입니다.")
        return premium, point-total-premium
    else:
        print(f"잔액이 부족합니다. 수수료는 {premium} 부족금액은 {total + premium - point}원 입니다.")
        return premium,point
def main():
    point = 0
    point = point_add(point ,30000)
    point = order(point, 17000)
    premium, point = order_night(point, 15000)
if __name__ == "__main__":
    main()