# �޺�Ȼ
# ʱ��:2021/8/14 9:37
def fun():
    num=int(input('������һ��ʮ���Ƶ�����'))#��str����ת����int����
    print(num,'�Ķ�������Ϊ:', bin(num)) #��һ��д����ʹ���˸����ɱ��λ�ò���
    print(str(num)+'�Ķ�������Ϊ:'+bin(num)) #�ڶ���д����ʹ��"+"��Ϊ���ӷ��q(+�����Ҿ�Ϊstr����)
    print('%s�Ķ�������Ϊ:%s'% (num, bin(num)))#������д������ʽ���ַ���
    print('{0}�Ķ�������Ϊ:(1}'.format(num, bin(num)))#������д������ʽ���ַ���
    print(f'{num}�Ķ�������Ϊ:{bin(num)}')#������д������ʽ���ַ���
    print('-------------------------------------------------')
    print(f'{num}�İ˽�����Ϊ:{oct(num)}')
    print(f'{num}��ʮ��������Ϊ:{hex (num)}')
if __name__ =='__main__':
    while True:
        try:
            fun()
            break
            break
        except:
            print('ֻ����������')
            fun()