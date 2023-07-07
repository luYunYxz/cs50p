
def f (*args,**kwargs):
    print("positions : ",args)
    print("kwPositions : " , kwargs)


f(12,32,12,23)
f(glass=12,slary=23,knut=12)