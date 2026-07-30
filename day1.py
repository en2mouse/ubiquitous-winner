print("hello world")
print(1+1)
name = '小明ming'
age = 20+1+10
print(name)
print("我的年龄是",age)
a = 10
b = 3
print(a+b)
print(a-b)
print(a/b)
print(a//b)
print(a*b)
print(a%b)
text = "abc"
print(text + "123")
#print(text + 3)
print(7 % 3)
print(15//4)
score =50
if score > 60:
    print("及格")
else:
    print("不及格")

fruits = ["苹果", "香蕉", "橙子"]
for f in fruits:
    print(f)
count = 1
while count < 3:
    print("地", count, "慈")
    count = count+1
def greet(name):
    print("hello,", name)
greet("alon")
greet("miya")
num = [10, 20 ,30]
print(num[0])
print(num[2])
print(len(num))
num.append(40)
print(num)
num[0] = 99
print(num)
num.remove(30)
print(num)
person = {"name": "jenny", "age": 20, "city": "NewYork"}
print(person["name"])
print(person["age"])
person["age"] = 33
person["gender"] = "male"
print(person)
for k, v in person.items():
    print(k, "=", v)
s = "Hello,World"
print(s.strip())
print(s.lower())
print("World" in s)
print("World" in s.lower())
print(s.split("o"))
with open("README.md", "a", encoding="utf-8") as f:
    f.write("今天学了python基础\n")
    f.write("????\n")
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)