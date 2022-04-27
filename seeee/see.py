import tkinter as tk  # 使用Tkinter前需要先导入
import json
import time
import threading
from multiprocessing import Process
import sys
import matplotlib.pyplot as plt


now=0

# print(sys.argv[0])

jj=[]
with open("json/"+str(sys.argv[1]),'r') as f:
    jj=json.load(f)
# with open("json/车流_低强度.json",'r') as f:
#     jj=json.load(f)


print("数据读取成功")

step=[]
average_speed=[]
wait_time=[]
paidui_car=[]
jam_num=[]

for jjj in jj:
    step.append(jjj['time'])
    average_speed.append(jjj['data']['average_speed'])
    paidui_car.append(jjj['data']['paidui_car'])
    jam_num.append(jjj['data']['jam_num'])

plt.ion()  # 必须打开交互模式

def thread_it(func):
    '''将函数打包进线程'''
    # 创建
    t = threading.Thread(target=func)
    # 守护 !!!
    t.setDaemon(True)
    # 启动
    t.start()
    # 阻塞--卡死界面！
    # t.join()

#
# def tu():
#     while True:
#         time.sleep(1)
#         plt.cla()  # 清除旧图
#         plt.plot(time[:now],average_speed[:now])  # 绘制新图
#         plt.plot(time[:now], paidui_car[:now])
#         plt.plot(time[:now], jam_num[:now])
#         plt.pause(1)  # 使用pause 而不是show来显示 0.01是一个延迟时间
#
#
# t=Process(target=tu)
# t.start()





# 第1步，实例化object，建立窗口window
window = tk.Tk()

# 第2步，给窗口的可视化起名字
window.title('My Window')

# 第3步，设定窗口的大小(长 * 宽)
window.geometry('1000x1000')  # 这里的乘是小x

# 第4步，在图形界面上创建 500 * 200 大小的画布并放置各种元素
canvas = tk.Canvas(window, height=800, width=800)
# cars=tk.Canvas(window,bg='red',height=1000, width=1000)
# 说明图片位置，并导入图片到画布上
# image_file = tk.PhotoImage(file='pic.gif')  # 图片位置（相对路径，与.py文件同一文件夹下，也可以用绝对路径，需要给定图片具体绝对路径）
# image = canvas.create_image(250, 0, anchor='n',image=image_file)        # 图片锚定点（n图片顶端的中间点位置）放在画布（250,0）坐标处
# 定义多边形参数，然后在画布上画出指定图形
x0, y0, x1, y1 = 400, 400, 150, 150
w=10
d=400
l=1
# line = canvas.create_line(x0-50, y0-50, x1-50, y1-50)                   # 画直线
# oval = canvas.create_oval(x0+120, y0+50, x1+120, y1+50, fill='yellow')  # 画圆 用黄色填充
# arc = canvas.create_arc(x0, y0+50, x1, y1+50, start=0, extent=180)      # 画扇形 从0度打开收到180度结束
# rect = canvas.create_rectangle(330, 30, 330+20, 30+20)                  # 画矩形正方形
line1=canvas.create_line(x0-w,0,x0-w,y0*2)
line2=canvas.create_line(x0+w,0,x0+w,y0*2)
line3=canvas.create_line(0,y0-w,x0*2,y0-w)
line4=canvas.create_line(0,y0+w,x0*2,y0+w)
line5=canvas.create_line(x0,0,x0,y0*2,dash=(4,4))
line6=canvas.create_line(0,y0,x0*2,y0,dash=(4,4))
canvas.pack()
# img=tk.PhotoImage(file='car.bmp')

def move():
    global now
    # for one in jj:
    #     poss = one['data']['xy']
    #     for pos in poss:
    #         time.sleep(0.1)
    #         # cars.clipboard_clear()
    #         u = int(pos[0]) + d
    #         v = int(pos[1]) + d
    #         # print(u, ",", v)
    #         car = canvas.create_rectangle(u-1,v-1,u+1,v+1)
    #     canvas.pack()
    while now<len(jj):
        now+=1

        # plt.cla()  # 清除旧图
        # plt.plot(time[:now], average_speed[:now])  # 绘制新图
        # plt.plot(time[:now], paidui_car[:now])
        # plt.plot(time[:now], jam_num[:now])
        # plt.pause(1)  # 使用pause 而不是show来显示 0.01是一个延迟时间

        canvas.delete(tk.ALL)
        poss=jj[now]['data']['xy']
        line1 = canvas.create_line(x0 - w, 0, x0 - w, y0 * 2)
        line2 = canvas.create_line(x0 + w, 0, x0 + w, y0 * 2)
        line3 = canvas.create_line(0, y0 - w, x0 * 2, y0 - w)
        line4 = canvas.create_line(0, y0 + w, x0 * 2, y0 + w)
        line5 = canvas.create_line(x0, 0, x0, y0 * 2, dash=(4, 4))
        line6 = canvas.create_line(0, y0, x0 * 2, y0, dash=(4, 4))
        for pos in poss:
            # cars.clipboard_clear()
            u = pos[0] + d
            v = pos[1] + d
            print(u, ",", v)

            car = canvas.create_rectangle(u - 2, v - 2, u + 2, v + 2)
            # car=canvas.create_image(u,v,img=img)
        canvas.pack()
        time.sleep(0.1)



def thread_it(func):
    '''将函数打包进线程'''
    # 创建
    t = threading.Thread(target=func)
    # 守护 !!!
    t.setDaemon(True)
    # 启动
    t.start()
    # 阻塞--卡死界面！
    # t.join()


# b = tk.Button(window,text='move',command=lambda :thread_it(move)).pack()

b = tk.Button(window,text='go',command=lambda :thread_it(move)).pack()

window.mainloop()

#
#
# for one in jj:
#     poss=one['data']['xy']
#     for pos in poss:
#         time.sleep(1)
#         # cars.clipboard_clear()
#         u=int(pos[0])+d
#         v=int(pos[1])+d
#         print(u,",",v)
#         car = canvas.create_rectangle(u-1,v-1,u+1,v+1)
#         canvas.pack()
