# 崔浩然
# 时间:2021/8/14 10:06
import random
rand=random.randint(1,100)
for i in range(1,11):
    num=int(input('在我心中有一个数1-100，猜一下'))
    if num>rand:
        print('bigger')
    elif num<rand:
        print('smaller')
    else:
        print('right')
        break
print(f'一共猜了{i}次')