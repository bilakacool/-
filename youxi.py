# coding=utf-8

from tkinter import *
import pickle
from tkinter import messagebox
import os
import random
import time
import MySQLdb as mysql


def shouye(zhanghao='游客'):
    """游戏首页"""
    root = Tk()
    root.title('猜拳小游戏')
    root.geometry('200x200')

    def a1():
        root.destroy()
        denglu()

    def a2():
        root.destroy()
        zhuce()

    def a3():
        root.destroy()
        kaishi('游客')

    def a4():
        if zhanghao == '游客':
            messagebox.showinfo(title='猜拳小游戏', message='最近没有登录账号！')
        else:
            root.destroy()
            kaishi(zhanghao)

    def a5():
        root.quit()

    Button(root, text='登陆账号', command=a1).place(x=30, y=30, anchor='nw')
    Button(root, text='注册账号', command=a2).place(x=120, y=30, anchor='nw')
    Button(root, text='游客模式', command=a3).place(x=30, y=75, anchor='nw')
    Button(root, text='快速登陆', command=a4).place(x=120, y=75, anchor='nw')
    Button(root, text='退出游戏', command=a5).place(x=75, y=120, anchor='nw')

    root.mainloop()


def denglu():
    """登录账号"""
    root = Tk()
    root.title('登录账号')
    root.geometry('200x200')

    def a1():
        zhanghao = e1.get()
        mima = e2.get()
        a = (zhanghao, mima)

        with open('yonghu.yonghu', 'rb') as c:
            yong = pickle.load(c)

        if a not in yong.items():
            return messagebox.showinfo(title='登录账号', message='账号或密码错误！')
        messagebox.showinfo(title='登录账号', message='账号 %s 登录成功！' % zhanghao)
        root.destroy()
        kaishi(zhanghao)

    def a2():
        root.destroy()
        shouye()

    Label(root, text='用户名：').place(x=30, y=30, anchor='nw')
    Label(root, text='密码：').place(x=30, y=75, anchor='nw')

    e1 = Entry(root, width=10)
    e1.place(x=100, y=30, anchor='nw')
    e2 = Entry(root, show='*', width=10)
    e2.place(x=100, y=75, anchor='nw')

    Button(root, text='登录', command=a1).place(x=30, y=120, anchor='nw')
    Button(root, text='返回首页', command=a2).place(x=100, y=120, anchor='nw')

    root.mainloop()


def zhuce(long=6):
    """注册账号"""
    root = Tk()
    root.title('注册账号')
    root.geometry('200x220')

    def a1():
        zhanghao = e1.get()
        mima = e2.get()
        mima2 = e3.get()

        if 'yonghu.yonghu' not in os.listdir(os.getcwd()):
            yong = {}

            with open('yonghu.yonghu', 'wb') as c:
                pickle.dump(yong, c)

        with open('yonghu.yonghu', 'rb') as c:
            yong = pickle.load(c)

        if zhanghao in yong.keys():
            return messagebox.showinfo(title='注册账号', message='用户名已存在！')

        if len(zhanghao) > long:
            return messagebox.showinfo(title='注册账号', message='用户名过长 请重新输入！')

        if zhanghao == '' or mima == '' or mima2 == '':
            return messagebox.showinfo(title='注册账号', message='请输入用户名和密码！')

        if mima != mima2:
            return messagebox.showinfo(title='注册账号', message='两次密码不一致！')

        yong[zhanghao] = mima
        with open('yonghu.yonghu', 'wb') as c:
            pickle.dump(yong, c)

        messagebox.showinfo(title='注册账号', message='用户 %s 注册成功，密码为 %s ！' % (zhanghao, mima))
        root.destroy()
        shouye()

    def a2():
        root.destroy()
        shouye()

    Label(root, text='用户名：').place(x=30, y=30, anchor='nw')
    Label(root, text='密码：').place(x=30, y=75, anchor='nw')
    Label(root, text='确认密码：').place(x=30, y=120, anchor='nw')

    e1 = Entry(root, width=10)
    e1.place(x=100, y=30, anchor='nw')
    e2 = Entry(root, show='*', width=10)
    e2.place(x=100, y=75, anchor='nw')
    e3 = Entry(root, show='*', width=10)
    e3.place(x=100, y=120, anchor='nw')

    Button(root, text='注册', command=a1).place(x=30, y=165, anchor='nw')
    Button(root, text='返回首页', command=a2).place(x=100, y=165, anchor='nw')

    root.mainloop()


def kaishi(zhanghao, defen=3, changci=10, liansheng=0, gaolian=0):
    """开始游戏"""
    defen = [defen]
    gaofen = [defen[0]]
    changci = [changci]
    liansheng = [liansheng]
    gaolian = [gaolian]

    root = Tk()
    root.title('用户： %s' % zhanghao)
    root.geometry('500x500')

    def a1():
        v5.set('')
        cai('3')

    def a2():
        v5.set('')
        cai('1')

    def a3():
        v5.set('')
        cai('2')

    def cai(wanjia):
        global name1, name2
        nonlocal defen, changci, liansheng, gaolian, gaofen
        jiqiren = random.randint(1, 3)

        if wanjia == '3':
            name1 = 'shi.png'
        elif wanjia == '1':
            name1 = 'bu.png'
        elif wanjia == '2':
            name1 = 'jian.png'
        image_file1 = PhotoImage(file=name1)
        canvas.create_image(0, 0, anchor='nw', image=image_file1)
        root.update_idletasks()

        if jiqiren == 3:
            name2 = 'shi.png'
        elif jiqiren == 1:
            name2 = 'bu.png'
        elif jiqiren == 2:
            name2 = 'jian.png'
        image_file2 = PhotoImage(file=name2)
        canvas.create_image(205, 0, anchor='nw', image=image_file2)
        root.update_idletasks()

        if (wanjia == '3' and jiqiren == 2) or (wanjia == '1' and jiqiren == 3) or (wanjia == '2' and jiqiren == 1):
            v5.set(v5.get() + '胜利了！')
            liansheng[0] += 1
            defen[0] += liansheng[0]

            if liansheng[0] > gaolian[0]:
                gaolian[0] = liansheng[0]
            if defen[0] > gaofen[0]:
                gaofen[0] = defen[0]

            if liansheng[0] > 1:
                v5.set(v5.get() + '恭喜获得%d连胜！' % liansheng[0])
            v5.set(v5.get() + '本场得分加%d分！' % liansheng[0])
            changci[0] -= 1
            v6.set('剩余场次：%d' % changci[0])
            v1.set('当前得分：%d' % defen[0])
            v2.set('当前连胜：%d' % liansheng[0])
            v3.set('最高得分：%d' % gaofen[0])
            v4.set('最高连胜：%d' % gaolian[0])

        elif wanjia == str(jiqiren):
            v5.set(v5.get() + '平局！')
            v2.set('当前连胜：0')
            changci[0] -= 1
            v6.set('剩余场次：%d' % changci[0])
        else:
            v5.set(v5.get() + '失败了！')
            defen[0] -= 1
            liansheng[0] = 0
            changci[0] -= 1
            v6.set('剩余场次：%d' % changci[0])
            v1.set('当前得分：%d' % defen[0])
            v2.set('当前连胜：%d' % liansheng[0])
            v3.set('最高得分：%d' % gaofen[0])
            v4.set('最高连胜：%d' % gaolian[0])

        if defen[0] <= 0:
            messagebox.showinfo(title='猜拳小游戏', message='好菜啊，分数用光了！')
            mingzi = str(zhanghao)
            gaofen = str(gaofen[0])
            gaolian = str(gaolian[0])
            a = bangdan(mingzi, gaofen + '分', gaolian + '连胜')
            if a == 0:
                messagebox.showinfo(title='猜拳小游戏', message='数据库无法连接，游戏记录无法保存！')
            else:
                messagebox.showinfo(title='猜拳小游戏', message='游戏记录已保存！')
            root.destroy()
            shouye()

        if changci[0] == 0:
            messagebox.showinfo(title='猜拳小游戏', message='所有场次进行完毕！')
            mingzi = str(zhanghao)
            gaofen = str(gaofen[0])
            gaolian = str(gaolian[0])
            a = bangdan(mingzi, gaofen + '分', gaolian + '连胜')
            if a == 0:
                messagebox.showinfo(title='猜拳小游戏', message='数据库无法连接，游戏记录无法保存！')
            else:
                messagebox.showinfo(title='猜拳小游戏', message='游戏记录已保存！')
            root.destroy()
            shouye(zhanghao)
        time.sleep(1)

    def a4(shuliang=10):
        data = bang(shuliang)
        if data == 0:
            paihang = '无法连接数据库，榜单无法展示'
        elif data == 1 or data == ():
            paihang = '排行榜暂无成绩'
        else:
            bang1 = '排行榜仅展示前%s名成绩\n\n'
            bang2 = '名次排行\t\t玩家名字\t\t最高得分\t\t最高连胜'
            bang3 = ''
            n = 1
            for i in data:
                bang3 += '\n第%d名'%n
                n += 1
                for k in i:
                    bang3 += '\t\t%s'%k
            paihang = bang1 + bang2 + bang3

        root = Tk()
        root.title('排行榜')
        root.geometry('450x300')
        Label(root, text=paihang, width=55, height=15).place(x=30, y=0, anchor='nw')

    def a5():
        a = messagebox.askquestion(title='结束游戏', message='结束游戏将无法保存成绩，确认结束游戏吗')
        if a == 'yes':
            root.destroy()
            shouye(zhanghao)

    v1 = StringVar()
    v2 = StringVar()
    v3 = StringVar()
    v4 = StringVar()
    v5 = StringVar()
    v6 = StringVar()

    v1.set('当前得分：%d' % defen[0])
    v2.set('当前连胜：%d' % liansheng[0])
    v3.set('最高得分：%d' % gaofen[0])
    v4.set('最高连胜：%d' % gaolian[0])
    v6.set('剩余场次：%d' % changci[0])

    Label(root, textvariable=v1).place(x=10, y=10, anchor='nw')
    Label(root, textvariable=v2).place(x=110, y=10, anchor='nw')
    Label(root, textvariable=v3).place(x=270, y=10, anchor='nw')
    Label(root, textvariable=v4).place(x=370, y=10, anchor='nw')

    Label(root, text='游戏公告：').place(x=10, y=55, anchor='nw')
    Label(root, textvariable=v5, bg='white', width=50).place(x=80, y=55, anchor='nw')
    Label(root, textvariable=v6).place(x=10, y=100, anchor='nw')

    canvas = Canvas(root, bg='YellowGreen', height=100, width=305)
    canvas.place(x=80, y=170, anchor='nw')
    canvas.create_text(60, 50, text=zhanghao, font=('Arial', 20))
    canvas.create_text(153, 50, text='VS', font=('Arial', 20))
    canvas.create_text(245, 50, text='电脑', font=('Arial', 20, 'bold'))

    Button(root, text='石头', font=('Arial', 20), bg='red', command=a1).place(x=82, y=320, anchor='nw')
    Button(root, text='布', font=('Arial', 20), bg='green', command=a2).place(x=206, y=320, anchor='nw')
    Button(root, text='剪刀', font=('Arial', 20), bg='yellow', command=a3).place(x=302, y=320, anchor='nw')

    Button(root, text='排行榜', command=a4).place(x=150, y=420, anchor='nw')
    Button(root, text='结束游戏', command=a5).place(x=250, y=420, anchor='nw')

    root.mainloop()


def bangdan(mingzi, gaofen, gaolian):
    """存入榜单"""
    try:
        db = mysql.connect('localhost', 'root', '123456', 'game', charset='utf8')
    except:
        return 0
    cursor = db.cursor()
    try:
        cursor.execute('select * from caiquan')
    except:
        cursor.execute('create table caiquan (name varchar(10), fen varchar(10), sheng varchar(10))')
    cursor.execute('insert into caiquan values("%s","%s","%s")'%(mingzi,gaofen,gaolian))
    db.commit()
    db.close()
    return 1


def bang(shuliang):
    """读取榜单"""
    try:
        db = mysql.connect('localhost', 'root', '123456', 'game', charset='utf8')
    except:
        return 0
    cursor = db.cursor()
    try:
        cursor.execute('select * from caiquan')
    except:
        return 1
    cursor.execute('select * from caiquan order by fen desc,sheng desc limit %d'% shuliang)
    data = cursor.fetchall()
    db.close()
    return data

if __name__ == '__main__':
    shouye()
