import string

# 只读模式打开，不会改动原文件
with open("article.txt", "r", encoding="utf-8") as f:
    text = f.read()

# 清洗：变小写 + 去标点
text = text.lower()
clean = text.translate(str.maketrans("", "", string.punctuation))

# 分词 + 字典计数
words = clean.split()
counts = {}
for w in words:
    if w in counts:
        counts[w] = counts[w] + 1
    else:
        counts[w] = 1

# 把结果写进 result.txt（这是全新文件名，不会覆盖任何东西）
with open("result.txt", "w", encoding="utf-8") as f:
    f.write("总词数：" + str(len(words)) + "\n")
    for w, n in counts.items():
        f.write(w + " : " + str(n) + "\n")

print("统计完成，结果已写入 result.txt")