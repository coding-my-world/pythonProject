# 崔浩然
# 时间:2021/9/26 14:19
# 功能:模拟多任务协程
import time
import asyncio
async def request(url):
    print('正在下载',url)
    #在异步协程中如果出现了同步模块相关的代码就无法实现异步
    #time.sleep(2)
    #当在asyncio中遇到阻塞操作必须进行手动挂起
    await asyncio.sleep(2)
    print('下载完毕',url)
start=time.time()
urls = [
    'www.baidu.com',
    'www.sougou.com',
    'www.bilibili.com'
]

#任务列表：存放多个任务对象
stasks =[]
for url in urls:
    c=request(url)
    task = asyncio.ensure_future(c)
    stasks.append(task)

loop=asyncio.get_event_loop()
#需要将任务列表封装到wait中
loop.run_until_complete(asyncio.wait(stasks))
print(time.time()-start)
