from tkinter import *
from random import *
from datetime import datetime
from PIL import ImageTk, Image
import itertools

def moon1():
    global iw4, iw3, iw2, bz2, k, iw1, ivit, izam, itof, isn, korzina, d, wh1, wh2
    k += 1
    bs['image'] = sun
    bs['command'] = sun1
    l1['image'] = md1
    br['bg'] = ser
    bl['bg'] = ser
    br['command'] = rd
    bl['command'] = ld
    br['activebackground'] = ser
    bl['activebackground'] = ser
    iw4 = PhotoImage(file='wd4.png')
    iw3 = PhotoImage(file='w3d.png')
    iw2 = PhotoImage(file='w2d.png')
    iw1 = PhotoImage(file='pit2.png')
    ivit = PhotoImage(file='vitd.png')
    izam = PhotoImage(file='zam1d.png')
    itof = PhotoImage(file='tof1d.png')
    isn = PhotoImage(file='sn1d.png')
    korzina = PhotoImage(file='korzd.png')
    d = PhotoImage(file='zakd.png')
    wh1 = '#343434'
    wh2 = '#ABB8C3'
def sun1():
    global iw4, iw3, iw2, bz2, k, iw1, ivit, izam, itof, isn, korzina, d, wh1, wh2
    k -= 1
    bs['image'] = moon
    bs['command'] = moon1
    l1['image'] = m1
    br['bg'] = wh
    bl['bg'] = wh
    br['command'] = r
    bl['command'] = l
    br['activebackground'] = wh
    bl['activebackground'] = wh
    iw4 = PhotoImage(file='w4.png')
    iw3 = PhotoImage(file='w3.png')
    iw2 = PhotoImage(file='w2.png')
    #iw1 = PhotoImage(file='pit1.png')
    ivit = PhotoImage(file='vitl.png')
    izam = PhotoImage(file='zam1.png')
    itof = PhotoImage(file='tof1.png')
    isn = PhotoImage(file='sn1.png')
    korzina = PhotoImage(file='korz.png')
    d = PhotoImage(file='zak.png')
    wh1 = 'white'
    wh2 = 'black'
def r():
    l1['image'] = m2
    br['command'] = r1


def r1():
    l1['image'] = m3
    br['command'] = r2


def r2():
    l1['image'] = m1
    br['command'] = r


def l():
    l1['image'] = m3
    bl['command'] = l11


def l11():
    l1['image'] = m2
    bl['command'] = l2


def l2():
    l1['image'] = m1
    bl['command'] = l

def rd():
    l1['image'] = md2
    br['command'] = r1d


def r1d():
    l1['image'] = md3
    br['command'] = r2d


def r2d():
    l1['image'] = md1
    br['command'] = rd


def ld():
    l1['image'] = md3
    bl['command'] = l11d


def l11d():
    l1['image'] = md2
    bl['command'] = l2d


def l2d():
    l1['image'] = md1
    bl['command'] = ld


def b1():
    def korz1():
        def chek():
            ch = Toplevel(wk)
            ch.geometry('345x600+200+50')
            ch.resizable(False, False)
            ch.title('Чек')
            ch.configure(bg=wh)
            dat = datetime.today()
            dat1 = dat.strftime('%Y.%m.%d')
            tim = dat.strftime('%H:%M:%S')
            n = randrange(100000, 999999)
            n1 = randrange(100000000, 999999999)
            n2 = randrange(1_000_000_000, 9999999999)
            h = f'''ООО "ПРЕМЬЕР ЗАЛ"
Екатеринбург, ул. Сулимова, 50
Кассовый чек №{n}
________________________________________________________________________'''
            lch = Label(ch, text=h, bg=wh)
            lch.pack()
            kon = f'''_______________________________________________________________________
   ИНН: {n1}                          ФП: {n2} 
 Кассир: Иванов И.И.
       Дата: {dat1}                          Время: {tim}
'''
            for o in cs:
                if o > 0:
                    cs1.extend(str(o))
            for i in range(len(g1)):
                g3 = f'''{g2[i]}'''
                cs2 = f'''                         {cs1[i]}
            {g2[i][-6:]}  *  {cs1[i]} = {int(g2[i][-6:-2]) * int(cs1[i])}p.'''
                lk1 = Label(ch, text=g3, bg=wh, font=('Calibri', '10'))
                lk1.place(x=2, y=100 + 50 * i)
                lc = Label(ch, text=cs2, bg=wh, font=('Calibri', '10'))
                lc.place(x=200, y=100 + 50 * i)
            lck = Label(ch, text=kon, bg=wh, justify='left')
            lck.place(x=0, y=82 + 50 * len(g1))
            ch.grab_set()
            ch.mainloop()

        global g, cs, lc1
        wk = Toplevel()
        wk.resizable(False, False)
        wk.geometry('400x600+200+50')
        wk.iconbitmap('ic.ico')
        wk.title('Корзина')
        lk = Label(wk, image=korzina)
        lk.place(x=-2, y=-2)
        lp = Label(wk, width=0, height=0, bg='#58C893')
        lp.pack()
        cs = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16]
        g1 = set(g)
        g2 = list(g1)
        cs = list(cs)
        cs1 = list()
        s = 0
        for o in cs:
            if o > 0:
                cs1.extend(str(o))
        for i in range(len(g1)):
            s += (int(g2[i][-6:-2]) * int(cs1[i]))
            g3 = f'''{g2[i]}'''
            cs2 = f'''                         {cs1[i]}
{g2[i][-6:]}  *  {cs1[i]} = {int(g2[i][-6:-2]) * int(cs1[i])}p.'''
            lk1 = Label(wk, text=g3, bg=wh1, font=('Inter', '10'), fg=wh2)
            lk1.place(x=2, y=21 + 50*i)
            lc = Label(wk, text=cs2, bg=wh1, font=('Inter', '10'), fg=wh2)
            lc.place(x=270, y=21 + 50*i)
            li = Label(wk, text=f'''Всегo:{s}p.
 Заказ будет ждать вас в магазине
 Оплата при получении''', bg=wh1, font=('Inter', '10'), fg=wh2)
            li.place(x=2, y=500)
        op = Button(wk, image=d, borderwidth=0, bg=wh1, highlightthickness=0, command=chek)
        op.place(x=250, y=530)
        wk.grab_set()
        wk.mainloop()

    def vit():
        global c13, c14, c15, c16, g

        def k13():
            global c13
            if c13 < 9:
                c13 += 1
            lv1['text'] = c13
            g.append('Витамин D3  165p.')

        def k14():
            global c14
            if c14 < 9:
                c14 += 1
            lv2['text'] = c14
            g.append('Ретинол     749p.')

        def k15():
            global c15
            if c15 < 9:
                c15 += 1
            lv3['text'] = c15
            g.append(f'Омега-3    1499p.')

        def k16():
            global c16
            if c16 < 9:
                c16 += 1
            lv4['text'] = c16
            g.append(f'Витамин К2  659p.')

        def k113():
            global c13
            if c13 > 0:
                c13 -= 1
                g.remove('Витамин D3  165p.')
            lv1['text'] = c13


        def k114():
            global c14
            if c14 > 0:
                c14 -= 1
                g.remove('Ретинол     749p.')
            lv2['text'] = c14


        def k115():
            global c15
            if c15 > 0:
                c15 -= 1
                g.remove('Омега-3    1499p.')
            lv3['text'] = c15


        def k116():
            global c16
            if c16 > 0:
                c16 -= 1
                g.remove('Витамин К2  659p.')
            lv4['text'] = c16

        def bk(e):
            korz.configure(bg=dgr)

        def bk1(e):
            korz.configure(bg='#93F9B9')
        vit = Toplevel(w1)
        vit.title('Фильмы')
        vit.iconbitmap('ic.ico')
        vit.geometry('834x300+200+50')
        vit.resizable(False, False)
        lv = Label(vit, image=ivit)
        lv.pack(anchor=W)
        korz = Button(vit, image=kor, borderwidth=0, height=300, bg='#93F9B9', width=30, command=korz1, activebackground=dgr)
        korz.place(x=802, y=0)
        korz.bind('<Enter>', bk)
        korz.bind('<Leave>', bk1)
        lv1 = Label(vit, text=c13, bg=wh, width=1, height=1, font=('Inter', '14'), fg=ls)
        lv1.place(x=96, y=228)
        p1 = Button(vit, text='+', bg=wh, borderwidth=0, font='40', command=k13, activebackground=wh)
        p1.place(x=112, y=224)
        min1 = Button(vit, text='-', bg=wh, borderwidth=0, font='40', command=k113, activebackground=wh)
        min1.place(x=80, y=223)
        lv2 = Label(vit, text=c14, bg=wh, width=1, height=1, font=('Inter', '14'), fg=ls)
        lv2.place(x=290, y=228)
        min2 = Button(vit, text='-', bg=wh, borderwidth=0, font='40', command=k114, activebackground=wh)
        min2.place(x=274, y=223)
        p2 = Button(vit, text='+', bg=wh, borderwidth=0, font='40', command=k14, activebackground=wh)
        p2.place(x=306, y=224)
        lv3 = Label(vit, text=c15, bg=wh, width=1, height=1, font=('Inter', '14'), fg=ls)
        lv3.place(x=484, y=228)
        min3 = Button(vit, text='-', bg=wh, borderwidth=0, font='40', command=k115, activebackground=wh)
        min3.place(x=468, y=223)
        p3 = Button(vit, text='+', bg=wh, borderwidth=0, font='40', command=k15, activebackground=wh)
        p3.place(x=500, y=224)
        lv4 = Label(vit, text=c16, bg=wh, width=1, height=1, font=('Inter', '14'), fg=ls)
        lv4.place(x=678, y=228)
        p4 = Button(vit, text='+', bg=wh, borderwidth=0, font='40', command=k16, activebackground=wh)
        p4.place(x=694, y=224)
        min4 = Button(vit, text='-', bg=wh, borderwidth=0, font='40', command=k116, activebackground=wh)
        min4.place(x=662, y=223)
        lc13 = Label(vit, text='165p.', bg=wh)
        lc13.place(x=90, y=214)
        lc14 = Label(vit, text='749p.', bg=wh)
        lc14.place(x=284, y=214)
        lc15 = Label(vit, text='1499p.', bg=wh)
        lc15.place(x=478, y=214)
        lc16 = Label(vit, text='659p.', bg=wh)
        lc16.place(x=672, y=214)
        vit.grab_set()
        vit.mainloop()

    def zam1():
        global c9, c10, c11, c12, g

        def k9():
            global c9
            if c9 < 9:
                c9 += 1
            lz1['text'] = c9
            g.append(f'Котлеты нутовыве    145p.')

        def k10():
            global c10
            if c10 < 9:
                c10 += 1
            lz2['text'] = c10
            g.append(f'Тефтели с тофу      299p.')

        def k11():
            global c11
            if c11 < 9:
                c11 += 1
            lz3['text'] = c11
            g.append(f'Нагетсы растительные    249p.')

        def k12():
            global c12
            if c12 < 9:
                c12 += 1
            lz4['text'] = c12
            g.append(f'Колбаса с сыром   469p.')

        def k19():
            global c9
            if c9 > 0:
                c9 -= 1
                g.remove('Котлеты нутовыве    145p.')
            lz1['text'] = c9


        def k110():
            global c10
            if c10 > 0:
                c10 -= 1
                g.remove('Тефтели с тофу      299p.')
            lz2['text'] = c10


        def k111():
            global c11
            if c11 > 0:
                c11 -= 1
                g.remove('Нагетсы растительные    249p.')
            lz3['text'] = c11

        def k112():
            global c12
            if c12 > 0:
                c12 -= 1
                g.remove('Колбаса с сыром   469p.')
            lz4['text'] = c12

        def bk(e):
            korz.configure(bg=dgr)

        def bk1(e):
            korz.configure(bg='#93F9B9')
        zam = Toplevel(w1)
        zam.title('Заменители мяса')
        zam.iconbitmap('ic.ico')
        zam.geometry('834x300+200+50')
        zam.resizable(False, False)
        lz = Label(zam, image=izam)
        lz.pack(anchor=W)
        korz = Button(zam, image=kor, borderwidth=0, height=300, bg='#93F9B9', width=30, command=korz1, activebackground=dgr)
        korz.place(x=802, y=0)
        korz.bind('<Enter>', bk)
        korz.bind('<Leave>', bk1)
        lz1 = Label(zam, text=c9, bg=wh, width=1, height=1, font=('Inter', '14'), fg=ls)
        lz1.place(x=96, y=228)
        p1 = Button(zam, text='+', bg=wh, borderwidth=0, font='40', command=k9, activebackground=wh)
        p1.place(x=112, y=224)
        min1 = Button(zam, text='-', bg=wh, borderwidth=0, font='40', command=k19, activebackground=wh)
        min1.place(x=80, y=223)
        lz2 = Label(zam, text=c10, bg=wh, width=1, height=1, font=('Inter', '14'), fg=ls)
        lz2.place(x=290, y=228)
        min2 = Button(zam, text='-', bg=wh, borderwidth=0, font='40', command=k110, activebackground=wh)
        min2.place(x=274, y=223)
        p2 = Button(zam, text='+', bg=wh, borderwidth=0, font='40', command=k10, activebackground=wh)
        p2.place(x=306, y=224)
        lz3 = Label(zam, text=c11, bg=wh, width=1, height=1, font=('Inter', '14'), fg=ls)
        lz3.place(x=484, y=228)
        min3 = Button(zam, text='-', bg=wh, borderwidth=0, font='40', command=k111, activebackground=wh)
        min3.place(x=468, y=223)
        p3 = Button(zam, text='+', bg=wh, borderwidth=0, font='40', command=k11, activebackground=wh)
        p3.place(x=500, y=224)
        lz4 = Label(zam, text=c12, bg=wh, width=1, height=1, font=('Inter', '14'), fg=ls)
        lz4.place(x=678, y=228)
        p4 = Button(zam, text='+', bg=wh, borderwidth=0, font='40', command=k12, activebackground=wh)
        p4.place(x=694, y=224)
        min4 = Button(zam, text='-', bg=wh, borderwidth=0, font='40', command=k112, activebackground=wh)
        min4.place(x=662, y=223)
        lc9 = Label(zam, text='145p.', bg=wh)
        lc9.place(x=90, y=214)
        lc10 = Label(zam, text='299p.', bg=wh)
        lc10.place(x=284, y=214)
        lc11 = Label(zam, text='249p.', bg=wh)
        lc11.place(x=478, y=214)
        lc12 = Label(zam, text='469p.', bg=wh)
        lc12.place(x=672, y=214)
        zam.grab_set()
        zam.mainloop()

    def tof1():
        global c5, c6, c7, c8, g

        def k5():
            global c5
            if c5 < 9:
                c5 += 1
            lt1['text'] = c5
            g.append(f'Тофу        119p.')

        def k6():
            global c6
            if c6 < 9:
                c6 += 1
            lt2['text'] = c6
            g.append(f'Тофу копчённый    199p.')

        def k7():
            global c7
            if c7 < 9:
                c7 += 1
            lt3['text'] = c7
            g.append(f'Тофу с укропом     128p.')

        def k8():
            global c8
            if c8 < 9:
                c8 += 1
            lt4['text'] = c8
            g.append(f'Творог соевый     299p.')

        def k51():
            global c5
            if c5 > 0:
                c5 -= 1
            g.remove('Тофу        119p.')
            lt1['text'] = c5

        def k61():
            global c6
            if c6 > 0:
                c6 -= 1
                g.remove('Тофу копчённый    199p.')
            lt2['text'] = c6

        def k71():
            global c7
            if c7 > 0:
                c7 -= 1
                g.remove('Тофу с укропом     128p.')
            lt3['text'] = c7

        def k81():
            global c8
            if c8 > 0:
                c8 -= 1
                g.remove('Творог соевый     299p.')
            lt4['text'] = c8

        def bk(e):
            korz.configure(bg=dgr)

        def bk1(e):
            korz.configure(bg='#93F9B9')

        tof = Toplevel(w1)
        tof.title('Фильмы')
        tof.iconbitmap('ic.ico')
        tof.geometry('834x300+200+50')
        tof.resizable(False, False)
        lt = Label(tof, image=itof)
        lt.pack(anchor=W)
        korz = Button(tof, image=kor, borderwidth=0, height=300, bg='#93F9B9', width=30, command=korz1, activebackground=dgr)
        korz.place(x=802, y=0)
        korz.bind('<Enter>', bk)
        korz.bind('<Leave>', bk1)
        lt1 = Label(tof, text=c13, bg=wh, width=1, height=1, font=('Inter', '14'), fg=ls)
        lt1.place(x=96, y=228)
        p1 = Button(tof, text='+', bg=wh, borderwidth=0, font='40', command=k5, activebackground=wh)
        p1.place(x=112, y=224)
        min1 = Button(tof, text='-', bg=wh, borderwidth=0, font='40', command=k51, activebackground=wh)
        min1.place(x=80, y=223)
        lt2 = Label(tof, text=c14, bg=wh, width=1, height=1, font=('Inter', '14'), fg=ls)
        lt2.place(x=290, y=228)
        min2 = Button(tof, text='-', bg=wh, borderwidth=0, font='40', command=k61, activebackground=wh)
        min2.place(x=274, y=223)
        p2 = Button(tof, text='+', bg=wh, borderwidth=0, font='40', command=k6, activebackground=wh)
        p2.place(x=306, y=224)
        lt3 = Label(tof, text=c15, bg=wh, width=1, height=1, font=('Inter', '14'), fg=ls)
        lt3.place(x=484, y=228)
        min3 = Button(tof, text='-', bg=wh, borderwidth=0, font='40', command=k71, activebackground=wh)
        min3.place(x=468, y=223)
        p3 = Button(tof, text='+', bg=wh, borderwidth=0, font='40', command=k7, activebackground=wh)
        p3.place(x=500, y=224)
        lt4 = Label(tof, text=c16, bg=wh, width=1, height=1, font=('Inter', '14'), fg=ls)
        lt4.place(x=678, y=228)
        p4 = Button(tof, text='+', bg=wh, borderwidth=0, font='40', command=k8, activebackground=wh)
        p4.place(x=694, y=224)
        min4 = Button(tof, text='-', bg=wh, borderwidth=0, font='40', command=k81, activebackground=wh)
        min4.place(x=662, y=223)
        lc5 = Label(tof, text='119p.', bg=wh)
        lc5.place(x=90, y=214)
        lc6 = Label(tof, text='199p.', bg=wh)
        lc6.place(x=284, y=214)
        lc7 = Label(tof, text='128p.', bg=wh)
        lc7.place(x=478, y=214)
        lc8 = Label(tof, text='299p.', bg=wh)
        lc8.place(x=672, y=214)
        tof.grab_set()
        tof.mainloop()

    def sn1():
        global c1, c2, c3, c4, g

        def k1():
            global c1
            if c1 < 9:
                c1 += 1
            ls1['text'] = c1
            g.append(f'Козинаки      44p.')

        def k2():
            global c2
            if c2 < 9:
                c2 += 1
            ls2['text'] = c2
            g.append(f'Нутсы(сыр)      99p.')

        def k3():
            global c3
            if c3 < 9:
                c3 += 1
            ls3['text'] = c3
            g.append(f'Флаксы   225p.')

        def k4():
            global c4
            if c4 < 9:
                c4 += 1
            ls4['text'] = c4
            g.append(f'Батончик кокосовый     38p.')

        def k01():
            global c1
            if c1 > 0:
                c1 -= 1
                g.remove('Козинаки      44p.')
            ls1['text'] = c1


        def k02():
            global c2
            if c2 > 0:
                c2 -= 1
                g.remove('Нутсы(сыр)      99p.')
            ls2['text'] = c2


        def k03():
            global c3
            if c3 > 0:
                c3 -= 1
                g.remove('Флаксы   225p.')
            ls3['text'] = c3


        def k04():
            global c4
            if c4 > 0:
                c4 -= 1
                g.remove('Батончик кокосовый     38p.')
            ls4['text'] = c4

        def bk(e):
            korz.configure(bg=dgr)

        def bk1(e):
            korz.configure(bg='#93F9B9')

        sn = Toplevel(w1)
        sn.title('Подробнее')
        sn.iconbitmap('ic.ico')
        sn.geometry('834x300+200+50')

        sn.resizable(False, False)
        ls5 = Label(sn, image=isn)
        ls5.pack(anchor=W)
        korz = Button(sn, image=kor, borderwidth=0, height=300, bg='#93F9B9', width=30, command=korz1, activebackground=dgr)
        korz.place(x=802, y=0)
        korz.bind('<Enter>', bk)
        korz.bind('<Leave>', bk1)
        ls1 = Label(sn, text=c1, bg=wh, width=1, height=1, font=('Inter', '14'), fg=ls)
        ls1.place(x=96, y=228)
        p1 = Button(sn, text='+', bg=wh, borderwidth=0, font='40', command=k1, activebackground=wh)
        p1.place(x=112, y=224)
        min1 = Button(sn, text='-', bg=wh, borderwidth=0, font='40', command=k01, activebackground=wh)
        min1.place(x=80, y=223)
        ls2 = Label(sn, text=c2, bg=wh, width=1, height=1, font=('Inter', '14'), fg=ls)
        ls2.place(x=290, y=228)
        min2 = Button(sn, text='-', bg=wh, borderwidth=0, font='40', command=k02, activebackground=wh)
        min2.place(x=274, y=223)
        p2 = Button(sn, text='+', bg=wh, borderwidth=0, font='40', command=k2, activebackground=wh)
        p2.place(x=306, y=224)
        ls3 = Label(sn, text=c3, bg=wh, width=1, height=1, font=('Inter', '14'), fg=ls)
        ls3.place(x=484, y=228)
        min3 = Button(sn, text='-', bg=wh, borderwidth=0, font='40', command=k03, activebackground=wh)
        min3.place(x=468, y=223)
        p3 = Button(sn, text='+', bg=wh, borderwidth=0, font='40', command=k3, activebackground=wh)
        p3.place(x=500, y=224)
        ls4 = Label(sn, text=c4, bg=wh, width=1, height=1, font=('Inter', '14'), fg=ls)
        ls4.place(x=678, y=228)
        p4 = Button(sn, text='+', bg=wh, borderwidth=0, font='40', command=k4, activebackground=wh)
        p4.place(x=694, y=224)
        min4 = Button(sn, text='-', bg=wh, borderwidth=0, font='40', command=k04, activebackground=wh)
        min4.place(x=662, y=223)
        lc1 = Label(sn, text='44p.', bg=wh)
        lc1.place(x=90, y=214)
        lc2 = Label(sn, text='99p.', bg=wh)
        lc2.place(x=284, y=214)
        lc3 = Label(sn, text='225p.', bg=wh)
        lc3.place(x=478, y=214)
        lc4 = Label(sn, text='38p.', bg=wh)
        lc4.place(x=672, y=214)
        sn.grab_set()
        sn.mainloop()

    def bk(e):
        korz.configure(bg=dgr)

    def bk1(e):
        korz.configure(bg='#93F9B9')

    w1 = Toplevel(m)
    w1.configure(bg=wh)
    w1.iconbitmap('ic.ico')
    w1.geometry('834x600+200+50')
    w1.resizable(False, False)
    lw1 = Label(w1, image=iw1)
    lw1.pack(anchor=W)
    w1.title('Афиша')
    ik1 = PhotoImage(file='Майор Гром.png')
    ik2 = PhotoImage(file='Министерство неджентельменских дел.png')
    ik3 = PhotoImage(file='Планета обезьян.png')
    ik4 = PhotoImage(file='Пушистый вояж.png')
    ik5 = PhotoImage(file='Сто лет тому вперед.png')
    ik6 = PhotoImage(file='незнакомцы.png')
    kor = PhotoImage(file='kor.png')

    korz = Button(w1, image=kor, borderwidth=0, height=300, bg='#93F9B9', width=30, command=korz1, activebackground=dgr)
    korz.place(x=802, y=0)
    korz.bind('<Enter>', bk)
    korz.bind('<Leave>', bk1)

    k1 = Button(w1, image=ik1, bg=wh, borderwidth=0, activebackground=wh, command=sn1)
    k1.place(x=0, y=0)
    k2 = Button(w1, image=ik2, bg=wh, borderwidth=0, activebackground=wh, command=tof1)
    k2.place(x=153, y=0)
    k3 = Button(w1, image=ik3, bg=wh, borderwidth=0, activebackground=wh, command=zam1)
    k3.place(x=303, y=0)
    k4 = Button(w1, image=ik4, bg=wh, borderwidth=0, activebackground=wh, command=vit)
    k4.place(x=452, y=0)
    k5 = Button(w1, image=ik5, bg=wh, borderwidth=0, activebackground=wh, command=vit)
    k5.place(x=600, y=0)
    k6 = Button(w1, image=ik6, bg=wh, borderwidth=0, activebackground=wh, command=sn1)
    k6.place(x=0, y=319)
    k7 = Button(w1, image=ik2, bg=wh, borderwidth=0, activebackground=wh, command=tof1)
    k7.place(x=153, y=0)
    k8 = Button(w1, image=ik3, bg=wh, borderwidth=0, activebackground=wh, command=zam1)
    k8.place(x=303, y=0)
    k9 = Button(w1, image=ik4, bg=wh, borderwidth=0, activebackground=wh, command=vit)
    k9.place(x=452, y=0)
    k10 = Button(w1, image=ik5, bg=wh, borderwidth=0, activebackground=wh, command=vit)
    k10.place(x=600, y=0)

    w1.grab_set()
    w1.mainloop()
def b2():
    def vit1():
        global c13, c14, c15, c16

        def k13():
            global c13
            if c13 < 9:
                c13 += 1
            lv1['text'] = c13
            g.append('Витамин D3  165p.')

        def k14():
            global c14
            if c14 < 9:
                c14 += 1
            lv2['text'] = c14
            g.append('Ретинол     749p.')

        def k15():
            global c15
            if c15 < 9:
                c15 += 1
            lv3['text'] = c15
            g.append(f'Омега-3    1499p.')

        def k16():
            global c16
            if c16 < 9:
                c16 += 1
            lv4['text'] = c16
            g.append(f'Витамин К2  659p.')

        def k113():
            global c13
            if c13 > 0:
                c13 -= 1
                g.remove('Витамин D3  165p.')
            lv1['text'] = c13


        def k114():
            global c14
            if c14 > 0:
                c14 -= 1
                g.remove('Ретинол     749p.')
            lv2['text'] = c14


        def k115():
            global c15
            if c15 > 0:
                c15 -= 1
                g.remove('Омега-3    1499p.')
            lv3['text'] = c15


        def k116():
            global c16
            if c16 > 0:
                c16 -= 1
                g.remove('Витамин К2  659p.')
            lv4['text'] = c16

        def korz1():
            def chek():
                ch = Toplevel(wk)
                ch.geometry('345x600+200+50')
                ch.resizable(False, False)
                ch.title('Чек')
                ch.configure(bg=wh)
                dat = datetime.today()
                dat1 = dat.strftime('%Y.%m.%d')
                tim = dat.strftime('%H:%M:%S')
                n = randrange(100000, 999999)
                n1 = randrange(100000000, 999999999)
                n2 = randrange(1_000_000_000, 9999999999)
                h = f'''ООО "ПРЕМЬЕР ЗАЛ"
Екатеринбург, ул. Сулимова, 50
Кассовый чек №{n}
________________________________________________________________________'''
                lch = Label(ch, text=h, bg=wh)
                lch.pack()
                kon = f'''_______________________________________________________________________
   ИНН: {n1}                          ФП: {n2} 
 Кассир: Иванов И.И.
       Дата: {dat1}                          Время: {tim}
'''
                for o in cs:
                    if o > 0:
                        cs1.extend(str(o))
                for i in range(len(g1)):
                    g3 = f'''{g2[i]}'''
                    cs2 = f'''                         {cs1[i]}
{g2[i][-6:]}  *  {cs1[i]} = {int(g2[i][-6:-2]) * int(cs1[i])}p.'''
                    lk1 = Label(ch, text=g3, bg=wh, font=('Calibri', '10'))
                    lk1.place(x=2, y=100 + 50 * i)
                    lc = Label(ch, text=cs2, bg=wh, font=('Calibri', '10'))
                    lc.place(x=200, y=100 + 50 * i)
                lck = Label(ch, text=kon, bg=wh, justify='left')
                lck.place(x=0, y=82 + 50 * len(g1))
                ch.grab_set()
                ch.mainloop()

            global g, cs, lc1
            wk = Toplevel()
            wk.resizable(False, False)
            wk.geometry('400x600+200+50')
            wk.iconbitmap('ic.ico')
            wk.title('Корзина')
            lk = Label(wk, image=korzina)
            lk.place(x=-2, y=-2)
            lp = Label(wk, width=0, height=0, bg='#58C893')
            lp.pack()
            cs = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15, c16]
            g1 = set(g)
            g2 = list(g1)
            cs = list(cs)
            cs1 = list()
            s = 0
            for o in cs:
                if o > 0:
                    cs1.extend(str(o))
            for i in range(len(g1)):
                s += (int(g2[i][-6:-2]) * int(cs1[i]))
                g3 = f'''{g2[i]}'''
                cs2 = f'''                         {cs1[i]}
{g2[i][-6:]}  *  {cs1[i]} = {int(g2[i][-6:-2]) * int(cs1[i])}p.'''
                lk1 = Label(wk, text=g3, bg=wh1, font=('Inter', '10'), fg=wh2)
                lk1.place(x=2, y=21 + 50 * i)
                lc = Label(wk, text=cs2, bg=wh1, font=('Inter', '10'), fg=wh2)
                lc.place(x=270, y=21 + 50 * i)
                li = Label(wk, text=f'''Всегo:{s}p.
 Заказ будет ждать вас в магазине
 Оплата при получении''', bg=wh1, font=('Inter', '10'), fg=wh2)
                li.place(x=2, y=500)
            op = Button(wk, image=d, borderwidth=0, bg=wh1, highlightthickness=0, command=chek)
            op.place(x=250, y=530)
            wk.grab_set()
            wk.mainloop()

        def bk(e):
            korz.configure(bg=dgr)

        def bk1(e):
            korz.configure(bg='#93F9B9')

        vit = Toplevel(w2)
        vit.title('Расписание')
        vit.iconbitmap('ic.ico')
        vit.geometry('834x300+200+50')
        vit.resizable(False, False)
        lv = Label(vit, image=ivit)
        lv.place(x=0, y=-2)
        kor = PhotoImage(file='kor.png')
        korz = Button(vit, image=kor, borderwidth=0, height=300, bg='#93F9B9', width=30, command=korz1, activebackground=dgr)
        korz.place(x=802, y=0)
        korz.bind('<Enter>', bk)
        korz.bind('<Leave>', bk1)
        lv1 = Label(vit, text=c13, bg=wh, width=1, height=1, font=('Inter', '14'), fg=ls)
        lv1.place(x=96, y=228)
        p1 = Button(vit, text='+', bg=wh, borderwidth=0, font='40', command=k13, activebackground=wh)
        p1.place(x=112, y=224)
        min1 = Button(vit, text='-', bg=wh, borderwidth=0, font='40', command=k113, activebackground=wh)
        min1.place(x=80, y=223)
        lv2 = Label(vit, text=c14, bg=wh, width=1, height=1, font=('Inter', '14'), fg=ls)
        lv2.place(x=290, y=228)
        min2 = Button(vit, text='-', bg=wh, borderwidth=0, font='40', command=k114, activebackground=wh)
        min2.place(x=274, y=223)
        p2 = Button(vit, text='+', bg=wh, borderwidth=0, font='40', command=k14, activebackground=wh)
        p2.place(x=306, y=224)
        lv3 = Label(vit, text=c15, bg=wh, width=1, height=1, font=('Inter', '14'), fg=ls)
        lv3.place(x=484, y=228)
        min3 = Button(vit, text='-', bg=wh, borderwidth=0, font='40', command=k115, activebackground=wh)
        min3.place(x=468, y=223)
        p3 = Button(vit, text='+', bg=wh, borderwidth=0, font='40', command=k15, activebackground=wh)
        p3.place(x=500, y=224)
        lv4 = Label(vit, text=c16, bg=wh, width=1, height=1, font=('Inter', '14'), fg=ls)
        lv4.place(x=678, y=228)
        p4 = Button(vit, text='+', bg=wh, borderwidth=0, font='40', command=k16, activebackground=wh)
        p4.place(x=694, y=224)
        min4 = Button(vit, text='-', bg=wh, borderwidth=0, font='40', command=k116, activebackground=wh)
        min4.place(x=662, y=223)
        lc13 = Label(vit, text='165p.', bg=wh)
        lc13.place(x=90, y=214)
        lc14 = Label(vit, text='749p.', bg=wh)
        lc14.place(x=284, y=214)
        lc15 = Label(vit, text='1499p.', bg=wh)
        lc15.place(x=478, y=214)
        lc16 = Label(vit, text='659p.', bg=wh)
        lc16.place(x=672, y=214)
        vit.grab_set()
        vit.mainloop()
    global bz2
    w2 = Toplevel(m)
    w2.iconbitmap('ic.ico')
    w2.title('Витамины')
    w2.resizable(False, False)
    w2.geometry('800x330+200+50')
    lw2 = Label(w2, image=iw2)
    lw2.pack()
    but = PhotoImage(file='but.png')
    if k == 1:
        bz2k = ser
    else:
        bz2k = wh
    bz2 = Button(w2, image=but, borderwidth=0, bg=bz2k, activebackground=bz2k, command=vit1)
    bz2.place(x=630, y=271)
    w2.grab_set()
    w2.mainloop()


def b4():
    w4 = Toplevel(m)
    w4.title('О нас')
    w4.iconbitmap('ic.ico')
    w4.resizable(False, False)
    w4.geometry('800x535+200+50')
    lw4 = Label(w4, image=iw4)
    lw4.place(x=-2, y=0)
    w4.grab_set()
    w4.mainloop()


def b3():
    w3 = Toplevel(m)
    w3.title('Расписание')
    w3.iconbitmap('ic.ico')
    w3.resizable(False, False)
    w3.geometry('800x501+200+50')
    lw3 = Label(w3, image=iw3)
    lw3.pack()
    w3.grab_set()
    w3.mainloop()


def fb1(e):
    bw1.configure(bg=dgr)


def fb1l(e):
    bw1.configure(bg=gr)


def fb2(e):
    bw2.configure(bg=dgr)


def fb2l(e):
    bw2.configure(bg=gr)


def fb3(e):
    bw3.configure(bg=dgr)


def fb3l(e):
    bw3.configure(bg=gr)

def fs(e):
    bs.configure(bg=dgr)


def fsl(e):
    bs.configure(bg=gr)


k = 0
f = ('Inter', '12')
gr = '#54C590'
dgr = '#1F855C'
wh = 'white'
wh1 = 'white'
wh2 = 'black'
ser = '#343434'
ls = '#4D5257'
g = list()
c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
c6 = 0
c7 = 0
c8 = 0
c9 = 0
c10 = 0
c11 = 0
c12 = 0
c13 = 0
c14 = 0
c15 = 0
c16 = 0


m = Tk()
m.geometry('800x600+200+50')
m.title('ПРЕМЬЕР ЗАЛ')
m.resizable(False, False)
m.iconbitmap('ic.ico')
m1 = PhotoImage(file='main1.png')
m2 = PhotoImage(file='main2.png')
m3 = PhotoImage(file='main3.png')
md1 = PhotoImage(file='maind1.png')
md2 = PhotoImage(file='maind2.png')
md3 = PhotoImage(file='maind3.png')
iw4 = PhotoImage(file='w4.png')
iw3 = PhotoImage(file='w3.png')
iw2 = PhotoImage(file='w2.png')
iw1 = PhotoImage(file='korz.png')
ivit = PhotoImage(file='vitl.png')
izam = PhotoImage(file='zam1.png')
itof = PhotoImage(file='tof1.png')
isn = PhotoImage(file='sn1.png')
korzina = PhotoImage(file='korz.png')
d = PhotoImage(file='zak.png')
l1 = Label(m, image=m1)
l1.place(x=-2, y=0)

sun = PhotoImage(file='sun (3).png')
moon = PhotoImage(file='moon (2).png')
bs = Button(m, image=moon, bg=gr, borderwidth=0, activebackground=dgr, command=moon1)
bs.place(x=769, y=97)
bs.bind('<Enter>', fs)
bs.bind('<Leave>', fsl)
bw1 = Button(m, bg=gr, borderwidth=0, height=1, width=20, text='Фильмы', fg=wh, font=f, activebackground=dgr,
             activeforeground=wh, command=b1)
bw1.place(x=30, y=97)
bw1.bind('<Enter>', fb1)
bw1.bind('<Leave>', fb1l)

bw2 = Button(m, bg=gr, borderwidth=0, height=1, width=20, text='Расписание', fg=wh, font=f, activebackground=dgr,
             activeforeground=wh, command=b2)
bw2.place(x=230, y=97)
bw2.bind('<Enter>', fb2)
bw2.bind('<Leave>', fb2l)

bw3 = Button(m, bg=gr, borderwidth=0, height=1, width=10, text='Контакты', fg=wh, font=f, activebackground=dgr,
             activeforeground=wh, command=b3)
bw3.place(x=430, y=97)
bw3.bind('<Enter>', fb3)
bw3.bind('<Leave>', fb3l)

br1 = PhotoImage(file='r.png')
br = Button(m, image=br1, bg=wh, borderwidth=0, command=r)
br.place(x=689, y=205)
bl1 = PhotoImage(file='l.png')
bl = Button(m, image=bl1, bg=wh, borderwidth=0, command=l)
bl.place(x=55, y=205)

photos = [ImageTk.PhotoImage(Image.open(f"main{i}.png").resize((800, 600))) for i in range(1, 4)]
photo_iterator = itertools.cycle(photos)

def update_photo():
    l1.config(image=next(photo_iterator))
    l1.after(5000, update_photo)
update_photo()

m.mainloop()