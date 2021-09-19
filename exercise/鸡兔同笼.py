# 崔浩然
# 时间:2021/9/14 20:01
# 功能：鸡兔同笼
print('鸡兔同笼问题求解：')
head = input('亲输入头的个数：')
feet = input('亲输入脚的个数：')
print('鸡和兔子的头个数一共为%s'%(head))
print('鸡和兔子的脚个数一共为：%s'%(feet))
chicken=int((feet-2*head)/2)
print('兔子的个数为：%d')%int(chicken)
print('鸡的个数为：%d')%int(head-chicken)


