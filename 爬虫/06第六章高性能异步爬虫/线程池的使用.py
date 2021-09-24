# 崔浩然
# 时间:2021/9/25 9:20
# 功能：使用线程池
import time
from multiprocessing.dummy import Pool
#使用线程池线程串行方式执行
start_time = time.time()
def get_page(str):
    print("正在下载：",str)
    time.sleep(2)
    print('下载成功：',str)

name_list = ['xiaozi','aa','bb','cc']

#实例化一个线程池对象
pool=Pool(4)
#将列表中每一个列表元素传递给get——page进行处理
pool.map(get_page,name_list)

end_time=time.time()
print(end_time-start_time)
