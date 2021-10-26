from matplotlib import colors
import matplotlib.pyplot as plt
import numpy as np
from numpy.core.fromnumeric import shape

'''
xpoints = np.array([0,6])   # x的取值范围是0-6
ypoints = np.array([0,100])  #y的取值范围是0-100
# 以上就是从(0,0)到(6,100)的直线


# x的值 默认是从 0开始

#  plot() 函数是绘制二维图形的最基本函数。用于绘制点和线
plt.plot(xpoints,ypoints)

# 这个参数代表只绘制两个实心点
# plt.plot(xpoints,ypoints,'o')

plt.plot(xpoints,ypoints,'v')

plt.xlabel('x-lable')
plt.ylabel('y-lable')
plt.title('Title')
# plt.grid()   #网格线
# plt.grid(axis='x')   #只在x方向上有线
plt.grid(color = 'r',linestyle = '--',linewidth = 0.5)

plt.show()
'''

'''
# 创建一些测试数据 -- 图1
x = np.linspace(0, 2*np.pi, 400)
y = np.sin(x**2)

# 创建一个画像和子图 -- 图2
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title('Simple plot')

# 创建两个子图 -- 图3
f, (ax1, ax2) = plt.subplots(1, 2, sharey=True)
ax1.plot(x, y)
ax1.set_title('Sharing Y axis')
ax2.scatter(x, y)

# 创建四个子图 -- 图4
fig, axs = plt.subplots(2, 2, subplot_kw=dict(projection="polar"))
axs[0, 0].plot(x, y)
axs[1, 1].scatter(x, y)

# 共享 x 轴
plt.subplots(2, 2, sharex='col')

# 共享 y 轴
plt.subplots(2, 2, sharey='row')

# 共享 x 轴和 y 轴
plt.subplots(2, 2, sharex='all', sharey='all')

# 这个也是共享 x 轴和 y 轴
plt.subplots(2, 2, sharex=True, sharey=True)

# 创建10 张图，已经存在的则删除
fig, ax = plt.subplots(num=10, clear=True)

plt.show()
'''

'''
# 散点图
x，y：长度相同的数组，也就是我们即将绘制散点图的数据点，输入数据。
s：点的大小，默认 20，也可以是个数组，数组每个参数为对应点的大小。
c：点的颜色，默认蓝色 'b'，也可以是个 RGB 或 RGBA 二维行数组。
marker：点的样式，默认小圆圈 'o'。
'''

# x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# y = np.array([1, 4, 9, 16, 7, 11, 23, 18])
# # 图标大小顺序
# sizes = np.array([20,50,100,200,500,1000,60,90])
# # 颜色顺序
# colors = np.array(["red","green","black","orange","purple","beige","cyan","magenta"])
# plt.grid(axis='x')
# plt.xlabel('x-lable')
# plt.ylabel('y-lable')
# plt.scatter(x, y, s=sizes,c = colors)
# plt.show()




# 使用随机数来设置散点图：
# 随机数生成器的种子
# np.random.seed(19680801)

# N = 50
# x = np.random.rand(N)
# y = np.random.rand(N)
# colors = np.random.rand(N)
# area = (30 * np.random.rand(N))**2  # 0 to 15 point radii

# plt.scatter(x, y, s=area, c=colors, alpha=0.5) # 设置颜色及透明度

# plt.figure(figsize=(20,8),dpi=100)



# plt.show()




'''
# 柱状图   plt.bar()
x：浮点型数组，柱形图的 x 轴数据。
height：浮点型数组，柱形图的高度。
width：浮点型数组，柱形图的宽度。
bottom：浮点型数组，底座的 y 坐标，默认 0
'''

# x = np.array(["Runoob-1", "Runoob-2", "Runoob-3", "C-RUNOOB"])
# y = np.array([12, 22, 6, 18])

# # 水平方向柱状图
# # plt.bar(x,y)  

# # 垂直方向的柱形图可以使用 barh() 方法来设置
# # color 参数可是数组，这样就可以对应柱状图对应颜色
# plt.barh(x,y,color = ['black','r','blue','green'],height=[0.1,0.4,0.9,0.2])

# plt.show()





'''
饼状图    plt.pie()
explode：数组，表示各个扇形之间的间隔，默认值为0。
labels：列表，各个扇形的标签，默认值为 None。
colors：数组，表示各个扇形的颜色，默认值为 None。
autopct：设置饼图内各个扇形百分比显示格式，%d%% 整数百分比，%0.1f 一位小数， 
        %0.1f%% 一位小数百分比， %0.2f%% 两位小数百分比。
radius：：设置饼图的半径，默认为 1。
'''

y = np.array([35, 25, 25, 15])

plt.pie(
    y,labels=['A','B','C','D'], # 设置饼图标签
    colors=['b','r','g','w'], # 设置饼图颜色
    explode=(0,0.2,0,0), # 第二部分突出显示，值越大，距离中心越远
    autopct='%.2f%%', # 格式化输出百分比
    radius=3
)
plt.title='Test-Pie'
plt.savefig("./save.png")
plt.show()