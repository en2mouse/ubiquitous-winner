# Ubiquitous Winner

## 本项目是个人测试项目，用来记录学习过程和进展

##### day1：

一、你实际走过的路
阶段 0 最初给的是一份"偏硬核"的计划，但你当时看不懂代码、术语也陌生。所以这条路被现场调整成了从零手把手——事实证明这个调整是对的，你一路跑通到了最后。
1. 环境地基（D2 / D3）
从淘宝镜像装 Git 2.55.0，逐步选对安装选项
建 venv、激活、pip install requests、导出 requirements.txt
配身份、生成 SSH 密钥、加到 GitHub、建仓库 ubiquitous-winner、首次 push
用 PyCharm（非 VS Code）写代码
踩过的坑都变成了经验：PowerShell 执行策略拦激活脚本（改用 Git Bash）、"w" 模式清空了 README（学会 git checkout 还原 + 文件三模式 r/w/a）。
2. Python 从零（第 0–12 节）
按"复制 → 运行 → 看结果 → 逐行讲"的节奏，一节一节啃：
二、你现在已经掌握的技能清单
打勾确认你都会了（✅ = 已实战跑通）：
在 PyCharm 里写 .py 并运行
建/激活 venv、pip install、requirements.txt
Git 提交循环：add → commit → push，SSH 免密
变量、运算、字符串拼接
if / else 分支
for / while 循环
定义函数、理解形参 / 实参
列表的增删查、索引从 0
字典的键值存储与遍历
字符串清洗（lower / strip / split）
文件读写（知道 r/w/a 区别，不再误删文件）
用"字典当计数器"做词频统计
清洗英文文本（变小写 + 去标点）
中文按"字"统计的思路
完成一个端到端小项目并推上 GitHub
三、你的第一个作品
词频统计小项目（ubiquitous-winner 仓库里）
输入：article.txt（一段英文）
处理：读入 → 变小写 → 去标点 → 按空格分词 → 字典计数
输出：result.txt（每个词及其出现次数）
交付：git push 到 GitHub，公开可看
这项目的价值：它跑通了真实工作的基本套路 读数据 → 处理 → 产出 → 版本管理，是"我会用 Python 解决实际问题"的硬证据。
四、阶段 0 结业标准（你已达成 ✅）
能在 PyCharm 独立写出并运行一个 30 行以内的小程序
能用自己的话解释：变量、循环、函数、列表、字典
能独立完成一次 git add/commit/push
有一个推上 GitHub 的练手项目


