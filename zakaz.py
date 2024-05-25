from tkinter import *
from random import *
from datetime import datetime
from PIL import ImageTk, Image
import itertools

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

#ФУНКЦИИ ВЫЗЫВАЮЩИЕ ОПИСАНИЕ КАЖДОГО ФИЛЬМА
    def vit():
        def bk(e):
            korz.configure(bg=dgr)

        def bk1(e):
            korz.configure(bg='#93F9B9')
        vit = Toplevel(w1)
        vit.title('О ФИЛЬМЕ ПУШИСТЫЙ ВОЯЖ')
        vit.iconbitmap('ic.ico')
        vit.geometry('834x400')
        vit.resizable(False, False)
        lv = Label(vit, image=ivit)
        lv.pack(anchor=W)
        korz = Button(vit, image=kor, borderwidth=0, height=300, bg='#93F9B9', width=30, command=korz1, activebackground=dgr)
        korz.place(x=802, y=0)
        korz.bind('<Enter>', bk)
        korz.bind('<Leave>', bk1)
        vit.grab_set()
        vit.mainloop()

    def sltn():
        def bk(e):
            korz.configure(bg=dgr)

        def bk1(e):
            korz.configure(bg='#93F9B9')
        sltn = Toplevel(w1)
        sltn.title('О ФИЛЬМЕ СТО ЛЕТ ТОМУ ВПЕРЕД')
        sltn.iconbitmap('ic.ico')
        sltn.geometry('834x400')
        sltn.resizable(False, False)
        lv = Label(sltn, image=isltn)
        lv.pack(anchor=W)
        korz = Button(sltn, image=kor, borderwidth=0, height=300, bg='#93F9B9', width=30, command=korz1, activebackground=dgr)
        korz.place(x=802, y=0)
        korz.bind('<Enter>', bk)
        korz.bind('<Leave>', bk1)
        sltn.grab_set()
        sltn.mainloop()

    def superp():
        def bk(e):
            korz.configure(bg=dgr)

        def bk1(e):
            korz.configure(bg='#93F9B9')

        superp = Toplevel(w1)
        superp.title('О ФИЛЬМЕ СУПЕРПТАШКИ')
        superp.iconbitmap('ic.ico')
        superp.geometry('834x400')
        superp.resizable(False, False)
        lv = Label(superp, image=isuperp)
        lv.pack(anchor=W)
        korz = Button(superp, image=kor, borderwidth=0, height=300, bg='#93F9B9', width=30, command=korz1, activebackground=dgr)
        korz.place(x=802, y=0)
        korz.bind('<Enter>', bk)
        korz.bind('<Leave>', bk1)
        superp.grab_set()
        superp.mainloop()

    def adel():
        def bk(e):
            korz.configure(bg=dgr)

        def bk1(e):
            korz.configure(bg='#93F9B9')

        adel = Toplevel(w1)
        adel.title('О ФИЛЬМЕ АСФАЛЬТОВЫЕ ДЖУНГЛИ')
        adel.iconbitmap('ic.ico')
        adel.geometry('834x400')
        adel.resizable(False, False)
        lv = Label(adel, image=iadel)
        lv.pack(anchor=W)
        korz = Button(adel, image=kor, borderwidth=0, height=300, bg='#93F9B9', width=30, command=korz1, activebackground=dgr)
        korz.place(x=802, y=0)
        korz.bind('<Enter>', bk)
        korz.bind('<Leave>', bk1)
        adel.grab_set()
        adel.mainloop()


    def nez():
        def bk(e):
            korz.configure(bg=dgr)

        def bk1(e):
            korz.configure(bg='#93F9B9')

        nez = Toplevel(w1)
        nez.title('О ФИЛЬМЕ НЕЗНАКОМЦЫ')
        nez.iconbitmap('ic.ico')
        nez.geometry('834x400')
        nez.resizable(False, False)
        lv = Label(nez, image=inez)
        lv.pack(anchor=W)
        korz = Button(nez, image=kor, borderwidth=0, height=300, bg='#93F9B9', width=30, command=korz1, activebackground=dgr)
        korz.place(x=802, y=0)
        korz.bind('<Enter>', bk)
        korz.bind('<Leave>', bk1)
        nez.grab_set()
        nez.mainloop()

    def vp():
        def bk(e):
            korz.configure(bg=dgr)

        def bk1(e):
            korz.configure(bg='#93F9B9')

        vp = Toplevel(w1)
        vp.title('О ФИЛЬМЕ ВИННИ ПУХ')
        vp.iconbitmap('ic.ico')
        vp.geometry('834x400')
        vp.resizable(False, False)
        lv = Label(vp, image=ivp)
        lv.pack(anchor=W)
        korz = Button(vp, image=kor, borderwidth=0, height=300, bg='#93F9B9', width=30, command=korz1, activebackground=dgr)
        korz.place(x=802, y=0)
        korz.bind('<Enter>', bk)
        korz.bind('<Leave>', bk1)
        vp.grab_set()
        vp.mainloop()

    def sudn():
        def bk(e):
            korz.configure(bg=dgr)

        def bk1(e):
            korz.configure(bg='#93F9B9')

        sudn = Toplevel(w1)
        sudn.title('О ФИЛЬМЕ СУДНАЯ НОЧЬ')
        sudn.iconbitmap('ic.ico')
        sudn.geometry('834x400')
        sudn.resizable(False, False)
        lv = Label(sudn, image=isudn)
        lv.pack(anchor=W)
        korz = Button(sudn, image=kor, borderwidth=0, height=300, bg='#93F9B9', width=30, command=korz1, activebackground=dgr)
        korz.place(x=802, y=0)
        korz.bind('<Enter>', bk)
        korz.bind('<Leave>', bk1)
        sudn.grab_set()
        sudn.mainloop()

    def zam1():
        def bk(e):
            korz.configure(bg=dgr)

        def bk1(e):
            korz.configure(bg='#93F9B9')
        zam = Toplevel(w1)
        zam.title('О ФИЛЬМЕ ПЛАНЕТА ОБЕЗЬЯН')
        zam.iconbitmap('ic.ico')
        zam.geometry('834x400')
        zam.resizable(False, False)
        lz = Label(zam, image=izam)
        lz.pack(anchor=W)
        korz = Button(zam, image=kor, borderwidth=0, height=300, bg='#93F9B9', width=30, command=korz1, activebackground=dgr)
        korz.place(x=802, y=0)
        korz.bind('<Enter>', bk)
        korz.bind('<Leave>', bk1)
        zam.grab_set()
        zam.mainloop()

    def tof1():
        tof = Toplevel(w1)
        tof.title('О ФИЛЬМЕ МИНЕСТЕРСТВО НЕДЖЕНТЕЛЬМЕНСКИХ ДЕЛ')
        tof.iconbitmap('ic.ico')
        tof.geometry('834x400')
        tof.resizable(False, False)
        lt = Label(tof, image=itof)
        lt.pack(anchor=W)
        korz = Button(tof, image=kor, borderwidth=0, height=300, bg='#93F9B9', width=30, command=korz1, activebackground=dgr)
        korz.place(x=802, y=0)
        korz.bind('<Enter>', bk)
        korz.bind('<Leave>', bk1)
        tof.grab_set()
        tof.mainloop()

    def sn1():

        def bk(e):
            korz.configure(bg=dgr)

        def bk1(e):
            korz.configure(bg='#93F9B9')

        sn = Toplevel(w1)
        sn.title('О ФИЛЬМЕ МАЙОР ГРОМ')
        sn.iconbitmap('ic.ico')
        sn.geometry('834x400')

        sn.resizable(False, False)
        ls5 = Label(sn, image=isn)
        ls5.pack(anchor=W)
        korz = Button(sn, image=kor, borderwidth=0, height=300, bg='#93F9B9', width=30, command=korz1, activebackground=dgr)
        korz.place(x=802, y=0)
        korz.bind('<Enter>', bk)
        korz.bind('<Leave>', bk1)
        sn.grab_set()
        sn.mainloop()
#АФИША С ВЫБОРОМ ФИЛЬМА
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
    ik7 = PhotoImage(file='Винни Пух.png')
    ik8 = PhotoImage(file='суперпташки.png')
    ik9 = PhotoImage(file='судная ночь.png')
    ik10 = PhotoImage(file='Асфальтовые джунгли.png')
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
    k5 = Button(w1, image=ik5, bg=wh, borderwidth=0, activebackground=wh, command=sltn)
    k5.place(x=600, y=0)
    k6 = Button(w1, image=ik6, bg=wh, borderwidth=0, activebackground=wh, command=nez)
    k6.place(x=0, y=319)
    k7 = Button(w1, image=ik7, bg=wh, borderwidth=0, activebackground=wh, command=vp)
    k7.place(x=153, y=319)
    k8 = Button(w1, image=ik8, bg=wh, borderwidth=0, activebackground=wh, command=superp)
    k8.place(x=303, y=319)
    k9 = Button(w1, image=ik9, bg=wh, borderwidth=0, activebackground=wh, command=sudn)
    k9.place(x=452, y=319)
    k10 = Button(w1, image=ik10, bg=wh, borderwidth=0, activebackground=wh, command=adel)
    k10.place(x=600, y=319)

    w1.grab_set()
    w1.mainloop()
def b2():
    def vit1():
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
ivp = PhotoImage(file='О фильме Винни Пух.png')
isuperp = PhotoImage(file='О фильме Суперпташки.png')
isudn = PhotoImage(file='О фильме Судная ночь.png')
inez = PhotoImage(file='О фильме Незнакомцы.png')
iadel = PhotoImage(file='О фильме Асфальтовые джунгли.png')
isltn = PhotoImage(file='О фильме сто лет тому вперед.png')
ivit = PhotoImage(file='О фильме пушистый вояж.png')
izam = PhotoImage(file='о фильме планета обезьян.png')
itof = PhotoImage(file='О фильме мин неджентельменских дел.png')
isn = PhotoImage(file='О фильме Гром.png')
korzina = PhotoImage(file='korz.png')
d = PhotoImage(file='zak.png')
l1 = Label(m, image=m1)
l1.place(x=-2, y=0)


bw1 = Button(m, bg=gr, borderwidth=0, height=1, width=20, text='ФИЛЬМЫ', fg=wh, font=f, activebackground=dgr,
             activeforeground=wh, command=b1)
bw1.place(x=30, y=97)
bw1.bind('<Enter>', fb1)
bw1.bind('<Leave>', fb1l)

bw2 = Button(m, bg=gr, borderwidth=0, height=1, width=20, text='РАСПИСАНИЕ', fg=wh, font=f, activebackground=dgr,
             activeforeground=wh, command=b2)
bw2.place(x=230, y=97)
bw2.bind('<Enter>', fb2)
bw2.bind('<Leave>', fb2l)

bw3 = Button(m, bg=gr, borderwidth=0, height=1, width=10, text='КОНТАКТЫ', fg=wh, font=f, activebackground=dgr,
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