# 崔浩然
# 时间:2021/7/29 15:25
score=int(input('请输入一个成绩'))
#判断
if score>=90 and score<=100:
    print('A级')
elif score>=80 and score<=89:
    print('B级')
elif  score >= 70 and score <= 79:
    print(' C级')
elif score>=60 and score<=69:
    print('D级')
elif score>=0 and score<=59:
    print('E级')
else:
    print('对不起，成绩有误，不在成绩的有效范围内')
