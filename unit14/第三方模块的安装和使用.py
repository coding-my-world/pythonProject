# 崔浩然
# 时间:2021/8/8 18:17
import schedule
import time
def job():
    print('哈哈------')

schedule.every(3).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)
    print('1')