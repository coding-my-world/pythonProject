# 崔浩然
# 时间:2021/8/8 22:03
src_file=open('img.png','rb')
target_file=open('copylogo.png','wb')
print(target_file.write(src_file.read()))
target_file.close()
src_file.close()