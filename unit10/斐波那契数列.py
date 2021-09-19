# 崔浩然
# 时间:2021/8/6 10:27
def fib(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

print(fib(6))

#输出这个数列的前六位上的数字
for i in range(1,7):
    print(fib(i),end='\t')