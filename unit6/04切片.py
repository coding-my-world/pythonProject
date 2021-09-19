# 崔浩然
# 时间:2021/7/31 10:07
lst=[10,20,30,40,50,60,70,80]
#start=1,stop=6,step=1(左闭右开）
print(lst[1:6:1])
print(lst[1:6:2])
#start=1,stop=6, step=2
print (lst[1:6:2])
#stop=6,step=2, start采用默认
print (lst[:6:2])
#start=1，step=2，stop采用默认
print(lst[1::2])

print('------------step步长为负数的情况--')
print('原列表:',lst)
print(lst[::-1])
#start=7,stop省略step=-1
print(lst[7::-1])
#start=6,stop=0,step=-2
print(lst[6:0:-2])
