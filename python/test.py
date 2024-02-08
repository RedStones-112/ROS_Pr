

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]	


################################
answer = []
################################
def percent(order):
    if order.count("%") >= 1:
        order += " "
        order_list = order.split("%")
        result = ""

        for val in order_list:
            
            try:
                if val.count(" ") == 0:
                    result = val + "*0.01"
                elif val != order_list[-1]:
                    result = "(" + result + val[:val.rfind(" ")] + ")" + f"""*(1{val[val.rfind(" ")+1]}({val[val.rfind(" ")+2:]}*0.01))"""
                    
                elif val == order_list[-1]:
                    result += val

            except:
                pass
            print(result)
    else:
        result = order
    return result
test = """5000.0.0"""

result = percent(test)

print(test.find(" "), test.count("."))
