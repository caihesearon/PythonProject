# 导入pyplot模块
import matplotlib.pyplot as plt
# 导入numpy模块
import numpy as np
# x坐标采样点生成
x = np.arange(0,11,0.2)
# 计算对应x的正弦值
y = np.sin(x)
# 控制图形格式为蓝色带星的虚线
plt.plot(x,y,'b--')
# 显示图形
# plt.show()


# 创建一个字典数据
animal_speed={'dog':(48,'#7199cf'),
                           'cat': (45, '#4fc4aa'),
                           'cheetah': (120, '#e1a7a2')}
# 获取动物的名字
animals = animal_speed.keys()
# 使用推导式获取动物的速度以及对应的颜色(通过索引区分)
speeds = [x[0] for x in animal_speed.values()]
colors = [x[1] for x in animal_speed.values()]
# 设置x横轴3个点（3个动物)
x = np.arange(3)
# 定义每个柱宽为0.3
bar_width = 0.3
# 创建柱状图bar(x横轴,y纵轴,bar宽度[,描边线透明])
bars = plt.bar(x, speeds, width=bar_width)
# 显示
plt.grid(linestyle='--') # linestyle参数为背景网格线的样式
plt.show()
