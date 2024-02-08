

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]	


################################
answer = []
################################

try:
    print(eval("(5" + "+5+2"))
except SyntaxError as e: #as "()" was never closed:
    if str(e)[:20] == "'(' was never closed":
        print("test")
    print(str(e)[:20])
    