import string

text = "GitHub is where people build software. More than 150 million people use GitHub to discover, fork, and contribute to over 420 million projects."
text = text.lower()
clean = text.translate(str.maketrans("", "", string.punctuation))
word = clean.split()
print(word)
counts = {}
for w in word:
    if w in counts:
        counts[w] = counts[w]+1
    else:
        counts[w] = 1
print(counts)
for w, n in counts.items():
    print(w, "出现", n, "次")
