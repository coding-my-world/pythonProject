# 崔浩然
# 时间:2021/8/9 8:48
with open('img.png','rb') as src_file:
    with open('copylogo2.png','wb') as target_file:
        target_file.write(src_file.read())