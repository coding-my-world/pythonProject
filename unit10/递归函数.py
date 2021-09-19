# 崔浩然
# 时间:2021/8/6 10:23

def fac(n):
    if n==1:
        return 1
    else:
        return n*fac(n-1)

print( fac(6))