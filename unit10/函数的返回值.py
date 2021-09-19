# 崔浩然
# 时间:2021/8/6 9:48

#函数返回多个值时，结果为元组
def fun(num):
    odd=[] #存奇数
    even=[]#存偶数
    for i in num:
        if i%2:
            odd.append(i)
        else:
            even.append(i)
    return odd,even

print(fun([10,29,34,23,44,53,55]))