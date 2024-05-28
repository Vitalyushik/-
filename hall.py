from tkinter import *
#from ttkbootstrap import *

W = Tk()
W.title('Выбор места')
W.config(width=1024, height= 720)
W.resizable(False,False)

count = 0
bg_color = '#24262C'
grey = 'grey56'
filmname = 'Годзилла и Конг: Новая империя'
font=('Calibri 20')
date = '29 мая 18:00'




def buying():
    global count
    W1 = Toplevel()
    W1.config(width=700, height=400, background=bg_color)
    W1.resizable(False, False)

    logo = PhotoImage(file='logotip-premer-zal-optimized.png')
    logotip = Label(W1, image=logo, background=bg_color).place(x=100,y=100)

    def get_value():
        return var.get()

    if count == 0:
        info = Label(W1, background=bg_color, foreground='white',text=f'Вы не выбрали ни одного билета', font=font).place(x=30, y=50)
    else:
        info = Label(W1, background=bg_color, foreground='white',text=f'Количество билетов: {count} шт., итого к оплате: {count*230} рублей', font=font).place(x=30, y=50)

    var = IntVar()
    cb = Checkbutton(W1, text="""Я согласен с условиями пользлования
и правилами к-т 'Премьер Зал" """,
                     variable=var,
                     command=get_value, background=bg_color, foreground='green',activeforeground='green', font=font, activebackground=bg_color).place(x=30, y=100)

    buy_button = Button(W1,image=buy_image, borderwidth=0, background=bg_color, activebackground= bg_color)
    buy_button.place(x=30, y=200)




"""                          БЛОК РАЗМЕТКИ СТРАНИЦЫ                    """


seet_button = PhotoImage(file='seet.png')
seet_press = PhotoImage(file='seet_press.png')
buy_image = PhotoImage(file='buy.png')

bg = Label(W, background=bg_color).place(x=0, y=0,width=1280, height=960) # Цвет фона

cinema_name = Label(W, text=f'{filmname}',font=font, background=bg_color,foreground='white')  # Обозначение имени фильма
cinema_name.place(x=10, y=10)

buy = Button(W, image=buy_image, borderwidth=0, background=bg_color, activebackground= bg_color, command=buying)
buy.place(x=830, y=-5)

date_film = Label(W, background=bg_color, text=f'{date}', font='Calibri 15', foreground=grey) # Дата показа
date_film.place(x=10, y=45)

border = Label(W, background='white').place(x=0, y=90,width=1280, height=1)

screen = Label(W, background=bg_color, text='ЭКРАН', font='Calibri 23', foreground=grey)
screen.place(x=450, y=110)


#cnt = Label(W, background=bg_color, text=f'КОЛИЧЕСТВО: {count}', font=font, foreground=grey).place(x=650, y=110)
#char = Label(W, background=bg_color, text=count.get(), font=font, foreground=grey).place(x=830, y=110)




"""                            БЛОК ФУНКЦИОНАЛА КНОПОК                      """



def navod_11(e):
    global count
    if seet11['state'] == NORMAL:
        seet11['image'] = seet_press
        seet11.config(state=DISABLED)
        count += 1
        seet11['image'] = seet_press
def otvod_11(e):
    global count
    if seet11['state'] == DISABLED:
        seet11.config(state=NORMAL)
        count -= 1
        seet11['image'] = seet_button

def navod_12(e):
    global count
    if seet12['state'] == NORMAL:
        seet12.config(state=DISABLED)
        count += 1
        seet12['image'] = seet_press
def otvod_12(e):
    global count
    if seet12['state'] == DISABLED:
        seet12.config(state=NORMAL)
        count -= 1
        seet12['image'] = seet_button

def navod_13(e):
    global count
    if seet13['state'] == NORMAL:
        seet13.config(state=DISABLED)
        count += 1
        seet13['image'] = seet_press
def otvod_13(e):
    global count
    if seet13['state'] == DISABLED:
        seet13.config(state=NORMAL)
        count -= 1
        seet13['image'] = seet_button

def navod_14(e):
    global count
    if seet14['state'] == NORMAL:
        seet14.config(state=DISABLED)
        count += 1
        seet14['image'] = seet_press
def otvod_14(e):
    global count
    if seet14['state'] == DISABLED:
        seet14.config(state=NORMAL)
        count -= 1
        seet14['image'] = seet_button

def navod_15(e):
    global count
    if seet15['state'] == NORMAL:
        seet15.config(state=DISABLED)
        count += 1
        seet15['image'] = seet_press
def otvod_15(e):
    global count
    if seet15['state'] == DISABLED:
        seet15.config(state=NORMAL)
        count -= 1
        seet15['image'] = seet_button

def navod_16(e):
    global count
    if seet16['state'] == NORMAL:
        seet16.config(state=DISABLED)
        count += 1
        seet16['image'] = seet_press
def otvod_16(e):
    global count
    if seet16['state'] == DISABLED:
        seet16.config(state=NORMAL)
        count -= 1
        seet16['image'] = seet_button

def navod_17(e):
    global count
    if seet17['state'] == NORMAL:
        seet17.config(state=DISABLED)
        count += 1
        seet17['image'] = seet_press
def otvod_17(e):
    global count
    if seet17['state'] == DISABLED:
        seet17.config(state=NORMAL)
        count -= 1
        seet17['image'] = seet_button

def navod_18(e):
    global count
    if seet18['state'] == NORMAL:
        seet18.config(state=DISABLED)
        count += 1
        seet18['image'] = seet_press
def otvod_18(e):
    global count
    if seet18['state'] == DISABLED:
        seet18.config(state=NORMAL)
        count -= 1
        seet18['image'] = seet_button

def navod_19(e):
    global count
    if seet19['state'] == NORMAL:
        seet19.config(state=DISABLED)
        count += 1
        seet19['image'] = seet_press
def otvod_19(e):
    global count
    if seet19['state'] == DISABLED:
        seet19.config(state=NORMAL)
        count -= 1
        seet19['image'] = seet_button

def navod_110(e):
    global count
    if seet110['state'] == NORMAL:
        seet110.config(state=DISABLED)
        count += 1
        seet110['image'] = seet_press
def otvod_110(e):
    global count
    if seet110['state'] == DISABLED:
        seet110.config(state=NORMAL)
        count -= 1
        seet110['image'] = seet_button

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def navod_21(e):
    global count
    if seet21['state'] == NORMAL:
        seet21.config(state=DISABLED)
        count += 1
        seet21['image'] = seet_press
def otvod_21(e):
    global count
    if seet21['state'] == DISABLED:
        seet21.config(state=NORMAL)
        count -= 1
        seet21['image'] = seet_button

def navod_22(e):
    global count
    if seet22['state'] == NORMAL:
        seet22.config(state=DISABLED)
        count += 1
        seet22['image'] = seet_press
def otvod_22(e):
    global count
    if seet22['state'] == DISABLED:
        seet22.config(state=NORMAL)
        count -= 1
        seet22['image'] = seet_button

def navod_23(e):
    global count
    if seet23['state'] == NORMAL:
        seet23.config(state=DISABLED)
        count += 1
        seet23['image'] = seet_press
def otvod_23(e):
    global count
    if seet23['state'] == DISABLED:
        seet23.config(state=NORMAL)
        count -= 1
        seet23['image'] = seet_button

def navod_24(e):
    global count
    if seet24['state'] == NORMAL:
        seet24.config(state=DISABLED)
        count += 1
        seet24['image'] = seet_press
def otvod_24(e):
    global count
    if seet24['state'] == DISABLED:
        seet24.config(state=NORMAL)
        count -= 1
        seet24['image'] = seet_button

def navod_25(e):
    global count
    if seet25['state'] == NORMAL:
        seet25.config(state=DISABLED)
        count += 1
        seet25['image'] = seet_press
def otvod_25(e):
    global count
    if seet25['state'] == DISABLED:
        seet25.config(state=NORMAL)
        count -= 1
        seet25['image'] = seet_button

def navod_26(e):
    global count
    if seet26['state'] == NORMAL:
        seet26.config(state=DISABLED)
        count += 1
        seet26['image'] = seet_press
def otvod_26(e):
    global count
    if seet26['state'] == DISABLED:
        seet26.config(state=NORMAL)
        count -= 1
        seet26['image'] = seet_button

def navod_27(e):
    global count
    if seet27['state'] == NORMAL:
        seet27.config(state=DISABLED)
        count += 1
        seet27['image'] = seet_press
def otvod_27(e):
    global count
    if seet27['state'] == DISABLED:
        seet27.config(state=NORMAL)
        count -= 1
        seet27['image'] = seet_button

def navod_28(e):
    global count
    if seet28['state'] == NORMAL:
        seet28.config(state=DISABLED)
        count += 1
        seet28['image'] = seet_press
def otvod_28(e):
    global count
    if seet28['state'] == DISABLED:
        seet28.config(state=NORMAL)
        count -= 1
        seet28['image'] = seet_button

def navod_29(e):
    global count
    if seet29['state'] == NORMAL:
        seet29.config(state=DISABLED)
        count += 1
        seet29['image'] = seet_press
def otvod_29(e):
    global count
    if seet29['state'] == DISABLED:
        seet29.config(state=NORMAL)
        count -= 1
        seet29['image'] = seet_button

def navod_210(e):
    global count
    if seet210['state'] == NORMAL:
        seet210.config(state=DISABLED)
        count += 1
        seet210['image'] = seet_press
def otvod_210(e):
    global count
    if seet210['state'] == DISABLED:
        seet210.config(state=NORMAL)
        count -= 1
        seet210['image'] = seet_button


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def navod_31(e):
    global count
    if seet31['state'] == NORMAL:
        seet31.config(state=DISABLED)
        count += 1
        seet31['image'] = seet_press
def otvod_31(e):
    global count
    if seet31['state'] == DISABLED:
        seet31.config(state=NORMAL)
        count -= 1
        seet31['image'] = seet_button

def navod_32(e):
    global count
    if seet32['state'] == NORMAL:
        seet32.config(state=DISABLED)
        count += 1
        seet32['image'] = seet_press
def otvod_32(e):
    global count
    if seet32['state'] == DISABLED:
        seet32.config(state=NORMAL)
        count -= 1
        seet32['image'] = seet_button

def navod_33(e):
    global count
    if seet33['state'] == NORMAL:
        seet33.config(state=DISABLED)
        count += 1
        seet33['image'] = seet_press
def otvod_33(e):
    global count
    if seet33['state'] == DISABLED:
        seet33.config(state=NORMAL)
        count -= 1
        seet33['image'] = seet_button

def navod_34(e):
    global count
    if seet34['state'] == NORMAL:
        seet34.config(state=DISABLED)
        count += 1
        seet34['image'] = seet_press
def otvod_34(e):
    global count
    if seet34['state'] == DISABLED:
        seet34.config(state=NORMAL)
        count -= 1
        seet34['image'] = seet_button

def navod_35(e):
    global count
    if seet35['state'] == NORMAL:
        seet35.config(state=DISABLED)
        count += 1
        seet35['image'] = seet_press
def otvod_35(e):
    global count
    if seet35['state'] == DISABLED:
        seet35.config(state=NORMAL)
        count -= 1
        seet35['image'] = seet_button

def navod_36(e):
    global count
    if seet36['state'] == NORMAL:
        seet36.config(state=DISABLED)
        count += 1
        seet36['image'] = seet_press
def otvod_36(e):
    global count
    if seet36['state'] == DISABLED:
        seet36.config(state=NORMAL)
        count -= 1
        seet36['image'] = seet_button

def navod_37(e):
    global count
    if seet37['state'] == NORMAL:
        seet37.config(state=DISABLED)
        count += 1
        seet37['image'] = seet_press
def otvod_37(e):
    global count
    if seet37['state'] == DISABLED:
        seet37.config(state=NORMAL)
        count -= 1
        seet37['image'] = seet_button

def navod_38(e):
    global count
    if seet38['state'] == NORMAL:
        seet38.config(state=DISABLED)
        count += 1
        seet38['image'] = seet_press
def otvod_38(e):
    global count
    if seet38['state'] == DISABLED:
        seet38.config(state=NORMAL)
        count -= 1
        seet38['image'] = seet_button

def navod_39(e):
    global count
    if seet39['state'] == NORMAL:
        seet39.config(state=DISABLED)
        count += 1
        seet39['image'] = seet_press
def otvod_39(e):
    global count
    if seet39['state'] == DISABLED:
        seet39.config(state=NORMAL)
        count -= 1
        seet39['image'] = seet_button

def navod_310(e):
    global count
    if seet310['state'] == NORMAL:
        seet310.config(state=DISABLED)
        count += 1
        seet310['image'] = seet_press
def otvod_310(e):
    global count
    if seet310['state'] == DISABLED:
        seet310.config(state=NORMAL)
        count -= 1
        seet310['image'] = seet_button


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


def navod_41(e):
    global count
    if seet41['state'] == NORMAL:
        seet41.config(state=DISABLED)
        count += 1
        seet41['image'] = seet_press
def otvod_41(e):
    global count
    if seet41['state'] == DISABLED:
        seet41.config(state=NORMAL)
        count -= 1
        seet41['image'] = seet_button

def navod_42(e):
    global count
    if seet42['state'] == NORMAL:
        seet42.config(state=DISABLED)
        count += 1
        seet42['image'] = seet_press
def otvod_42(e):
    global count
    if seet42['state'] == DISABLED:
        seet42.config(state=NORMAL)
        count -= 1
        seet42['image'] = seet_button

def navod_43(e):
    global count
    if seet43['state'] == NORMAL:
        seet43.config(state=DISABLED)
        count += 1
        seet43['image'] = seet_press
def otvod_43(e):
    global count
    if seet43['state'] == DISABLED:
        seet43.config(state=NORMAL)
        count -= 1
        seet43['image'] = seet_button

def navod_44(e):
    global count
    if seet44['state'] == NORMAL:
        seet44.config(state=DISABLED)
        count += 1
        seet44['image'] = seet_press
def otvod_44(e):
    global count
    if seet44['state'] == DISABLED:
        seet44.config(state=NORMAL)
        count -= 1
        seet44['image'] = seet_button

def navod_45(e):
    global count
    if seet45['state'] == NORMAL:
        seet45.config(state=DISABLED)
        count += 1
        seet45['image'] = seet_press
def otvod_45(e):
    global count
    if seet45['state'] == DISABLED:
        seet45.config(state=NORMAL)
        count -= 1
        seet45['image'] = seet_button

def navod_46(e):
    global count
    if seet46['state'] == NORMAL:
        seet46.config(state=DISABLED)
        count += 1
        seet46['image'] = seet_press
def otvod_46(e):
    global count
    if seet46['state'] == DISABLED:
        seet46.config(state=NORMAL)
        count -= 1
        seet46['image'] = seet_button

def navod_47(e):
    global count
    if seet47['state'] == NORMAL:
        seet47.config(state=DISABLED)
        count += 1
        seet47['image'] = seet_press
def otvod_47(e):
    global count
    if seet47['state'] == DISABLED:
        seet47.config(state=NORMAL)
        count -= 1
        seet47['image'] = seet_button

def navod_48(e):
    global count
    if seet48['state'] == NORMAL:
        seet48.config(state=DISABLED)
        count += 1
        seet48['image'] = seet_press
def otvod_48(e):
    global count
    if seet48['state'] == DISABLED:
        seet48.config(state=NORMAL)
        count -= 1
        seet48['image'] = seet_button

def navod_49(e):
    global count
    if seet49['state'] == NORMAL:
        seet49.config(state=DISABLED)
        count += 1
        seet49['image'] = seet_press
def otvod_49(e):
    global count
    if seet49['state'] == DISABLED:
        seet49.config(state=NORMAL)
        count -= 1
        seet49['image'] = seet_button

def navod_410(e):
    global count
    if seet410['state'] == NORMAL:
        seet410.config(state=DISABLED)
        count += 1
        seet410['image'] = seet_press
def otvod_410(e):
    global count
    if seet410['state'] == DISABLED:
        seet410.config(state=NORMAL)
        count -= 1
        seet410['image'] = seet_button


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

def navod_51(e):
    global count
    if seet51['state'] == NORMAL:
        seet51.config(state=DISABLED)
        count += 1
        seet51['image'] = seet_press
def otvod_51(e):
    global count
    if seet51['state'] == DISABLED:
        seet51.config(state=NORMAL)
        count -= 1
        seet51['image'] = seet_button

def navod_52(e):
    global count
    if seet52['state'] == NORMAL:
        seet52.config(state=DISABLED)
        count += 1
        seet52['image'] = seet_press
def otvod_52(e):
    global count
    if seet52['state'] == DISABLED:
        seet52.config(state=NORMAL)
        count -= 1
        seet52['image'] = seet_button

def navod_53(e):
    global count
    if seet53['state'] == NORMAL:
        seet53.config(state=DISABLED)
        count += 1
        seet53['image'] = seet_press
def otvod_53(e):
    global count
    if seet53['state'] == DISABLED:
        seet53.config(state=NORMAL)
        count -= 1
        seet53['image'] = seet_button

def navod_54(e):
    global count
    if seet54['state'] == NORMAL:
        seet54.config(state=DISABLED)
        count += 1
        seet54['image'] = seet_press
def otvod_54(e):
    global count
    if seet54['state'] == DISABLED:
        seet54.config(state=NORMAL)
        count -= 1
        seet54['image'] = seet_button

def navod_55(e):
    global count
    if seet55['state'] == NORMAL:
        seet55.config(state=DISABLED)
        count += 1
        seet55['image'] = seet_press
def otvod_55(e):
    global count
    if seet55['state'] == DISABLED:
        seet55.config(state=NORMAL)
        count -= 1
        seet55['image'] = seet_button

def navod_56(e):
    global count
    if seet56['state'] == NORMAL:
        seet56.config(state=DISABLED)
        count += 1
        seet56['image'] = seet_press
def otvod_56(e):
    global count
    if seet56['state'] == DISABLED:
        seet56.config(state=NORMAL)
        count -= 1
        seet56['image'] = seet_button

def navod_57(e):
    global count
    if seet57['state'] == NORMAL:
        seet57.config(state=DISABLED)
        count += 1
        seet57['image'] = seet_press
def otvod_57(e):
    global count
    if seet57['state'] == DISABLED:
        seet57.config(state=NORMAL)
        count -= 1
        seet57['image'] = seet_button

def navod_58(e):
    global count
    if seet58['state'] == NORMAL:
        seet58.config(state=DISABLED)
        count += 1
        seet58['image'] = seet_press
def otvod_58(e):
    global count
    if seet58['state'] == DISABLED:
        seet58.config(state=NORMAL)
        count -= 1
        seet58['image'] = seet_button

def navod_59(e):
    global count
    if seet59['state'] == NORMAL:
        seet59.config(state=DISABLED)
        count += 1
        seet59['image'] = seet_press
def otvod_59(e):
    global count
    if seet59['state'] == DISABLED:
        seet59.config(state=NORMAL)
        count -= 1
        seet59['image'] = seet_button

def navod_510(e):
    global count
    if seet510['state'] == NORMAL:
        seet510.config(state=DISABLED)
        count += 1
        seet510['image'] = seet_press
def otvod_510(e):
    global count
    if seet510['state'] == DISABLED:
        seet510.config(state=NORMAL)
        count -= 1
        seet510['image'] = seet_button

def navod_511(e):
    global count
    if seet511['state'] == NORMAL:
        seet511.config(state=DISABLED)
        count += 1
        seet511['image'] = seet_press
def otvod_511(e):
    global count
    if seet511['state'] == DISABLED:
        seet511.config(state=NORMAL)
        count -= 1
        seet511['image'] = seet_button

def navod_512(e):
    global count
    if seet512['state'] == NORMAL:
        seet512.config(state=DISABLED)
        count += 1
        seet512['image'] = seet_press
def otvod_512(e):
    global count
    if seet512['state'] == DISABLED:
        seet512.config(state=NORMAL)
        count -= 1
        seet512['image'] = seet_button

def navod_513(e):
    global count
    if seet513['state'] == NORMAL:
        seet513.config(state=DISABLED)
        count += 1
        seet513['image'] = seet_press
def otvod_513(e):
    global count
    if seet513['state'] == DISABLED:
        seet513.config(state=NORMAL)
        count -= 1
        seet513['image'] = seet_button

"""ПЕРВЫЙ РЯД"""
seet11 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color, state=NORMAL)
seet11.place(x=170, y=200)
seet11.bind('<Button-1>', navod_11)
seet11.bind('<ButtonRelease-3>', otvod_11)

seet12 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
seet12.place(x=220, y=200)
seet12.bind('<Button-1>', navod_12)
seet12.bind('<ButtonRelease-3>', otvod_12)


seet13 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
seet13.place(x=270, y=200)
seet13.bind('<Button-1>', navod_13)
seet13.bind('<ButtonRelease-3>', otvod_13)

seet14 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
seet14.place(x=320, y=200)
seet14.bind('<Button-1>', navod_14)
seet14.bind('<ButtonRelease-3>', otvod_14)

seet15 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
seet15.place(x=370, y=200)
seet15.bind('<Button-1>', navod_15)
seet15.bind('<ButtonRelease-3>', otvod_15)

seet16 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
seet16.place(x=570, y=200)
seet16.bind('<Button-1>', navod_16)
seet16.bind('<ButtonRelease-3>', otvod_16)

seet17 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
seet17.place(x=620, y=200)
seet17.bind('<Button-1>', navod_17)
seet17.bind('<ButtonRelease-3>', otvod_17)

seet18 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
seet18.place(x=670, y=200)
seet18.bind('<Button-1>', navod_18)
seet18.bind('<ButtonRelease-3>', otvod_18)

seet19 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
seet19.place(x=720, y=200)
seet19.bind('<Button-1>', navod_19)
seet19.bind('<ButtonRelease-3>', otvod_19)

seet110 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
seet110.place(x=770, y=200)
seet110.bind('<Button-1>', navod_110)
seet110.bind('<ButtonRelease-3>', otvod_110)

"""ВТОРОЙ РЯД"""
seet21 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
seet21.place(x=170, y=300)
seet21.bind('<Button-1>', navod_21)
seet21.bind('<ButtonRelease-3>', otvod_21)


seet22 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
seet22.place(x=220, y=300)
seet22.bind('<Button-1>', navod_22)
seet22.bind('<ButtonRelease-3>', otvod_22)


seet23 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
seet23.place(x=270, y=300)
seet23.bind('<Button-1>', navod_23)
seet23.bind('<ButtonRelease-3>', otvod_23)

seet24 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
seet24.place(x=320, y=300)
seet24.bind('<Button-1>', navod_24)
seet24.bind('<ButtonRelease-3>', otvod_24)

seet25 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
seet25.place(x=370, y=300)
seet25.bind('<Button-1>', navod_25)
seet25.bind('<ButtonRelease-3>', otvod_25)

seet26 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
seet26.place(x=570, y=300)
seet26.bind('<Button-1>', navod_26)
seet26.bind('<ButtonRelease-3>', otvod_26)

seet27 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
seet27.place(x=620, y=300)
seet27.bind('<Button-1>', navod_27)
seet27.bind('<ButtonRelease-3>', otvod_27)

seet28 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
seet28.place(x=670, y=300)
seet28.bind('<Button-1>', navod_28)
seet28.bind('<ButtonRelease-3>', otvod_28)

seet29 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
seet29.place(x=720, y=300)
seet29.bind('<Button-1>', navod_29)
seet29.bind('<ButtonRelease-3>', otvod_29)

seet210 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
seet210.place(x=770, y=300)
seet210.bind('<Button-1>', navod_210)
seet210.bind('<ButtonRelease-3>', otvod_210)

"""ТРЕТИЙ РЯД"""
seet31 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
seet31.place(x=170, y=400)
seet31.bind('<Button-1>', navod_31)
seet31.bind('<ButtonRelease-3>', otvod_31)

seet32 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
seet32.place(x=220, y=400)
seet32.bind('<Button-1>', navod_32)
seet32.bind('<ButtonRelease-3>', otvod_32)

seet33 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
seet33.place(x=270, y=400)
seet33.bind('<Button-1>', navod_33)
seet33.bind('<ButtonRelease-3>', otvod_33)

seet34 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
seet34.place(x=320, y=400)
seet34.bind('<Button-1>', navod_34)
seet34.bind('<ButtonRelease-3>', otvod_34)

seet35 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
seet35.place(x=370, y=400)
seet35.bind('<Button-1>', navod_35)
seet35.bind('<ButtonRelease-3>', otvod_35)

seet36 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
seet36.place(x=570, y=400)
seet36.bind('<Button-1>', navod_36)
seet36.bind('<ButtonRelease-3>', otvod_36)

seet37 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
seet37.place(x=620, y=400)
seet37.bind('<Button-1>', navod_37)
seet37.bind('<ButtonRelease-3>', otvod_37)

seet38 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
seet38.place(x=670, y=400)
seet38.bind('<Button-1>', navod_38)
seet38.bind('<ButtonRelease-3>', otvod_38)

seet39 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
seet39.place(x=720, y=400)
seet39.bind('<Button-1>', navod_39)
seet39.bind('<ButtonRelease-3>', otvod_39)

seet310 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
seet310.place(x=770, y=400)
seet310.bind('<Button-1>', navod_310)
seet310.bind('<ButtonRelease-3>', otvod_310)


"""ЧЕТВЕРТЫЙ РЯД"""
seet41 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
seet41.place(x=170, y=500)
seet41.bind('<Button-1>', navod_41)
seet41.bind('<ButtonRelease-3>', otvod_41)

seet42 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
seet42.place(x=220, y=500)
seet42.bind('<Button-1>', navod_42)
seet42.bind('<ButtonRelease-3>', otvod_42)

seet43 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
seet43.place(x=270, y=500)
seet43.bind('<Button-1>', navod_43)
seet43.bind('<ButtonRelease-3>', otvod_43)

seet44 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
seet44.place(x=320, y=500)
seet44.bind('<Button-1>', navod_44)
seet44.bind('<ButtonRelease-3>', otvod_44)

seet45 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
seet45.place(x=370, y=500)
seet45.bind('<Button-1>', navod_45)
seet45.bind('<ButtonRelease-3>', otvod_45)

seet46 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
seet46.place(x=570, y=500)
seet46.bind('<Button-1>', navod_46)
seet46.bind('<ButtonRelease-3>', otvod_46)

seet47 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
seet47.place(x=620, y=500)
seet47.bind('<Button-1>', navod_47)
seet47.bind('<ButtonRelease-3>', otvod_47)

seet48 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
seet48.place(x=670, y=500)
seet48.bind('<Button-1>', navod_48)
seet48.bind('<ButtonRelease-3>', otvod_48)

seet49 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
seet49.place(x=720, y=500)
seet49.bind('<Button-1>', navod_49)
seet49.bind('<ButtonRelease-3>', otvod_49)

seet410 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
seet410.place(x=770, y=500)
seet410.bind('<Button-1>', navod_410)
seet410.bind('<ButtonRelease-3>', otvod_410)

"""ПЯТЫЙ РЯД"""

seet51 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
seet51.place(x=170, y=600)
seet51.bind('<Button-1>', navod_51)
seet51.bind('<ButtonRelease-3>', otvod_51)


seet52 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
seet52.place(x=220, y=600)
seet52.bind('<Button-1>', navod_52)
seet52.bind('<ButtonRelease-3>', otvod_52)

seet53 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
seet53.place(x=270, y=600)
seet53.bind('<Button-1>', navod_53)
seet53.bind('<ButtonRelease-3>', otvod_53)

seet54 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
seet54.place(x=320, y=600)
seet54.bind('<Button-1>', navod_54)
seet54.bind('<ButtonRelease-3>', otvod_54)

seet55 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
seet55.place(x=370, y=600)
seet55.bind('<Button-1>', navod_55)
seet55.bind('<ButtonRelease-3>', otvod_55)

seet56 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
seet56.place(x=420, y=600)
seet56.bind('<Button-1>', navod_56)
seet56.bind('<ButtonRelease-3>', otvod_56)

seet57 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
seet57.place(x=470, y=600)
seet57.bind('<Button-1>', navod_57)
seet57.bind('<ButtonRelease-3>', otvod_57)

seet58 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
seet58.place(x=520, y=600)
seet58.bind('<Button-1>', navod_58)
seet58.bind('<ButtonRelease-3>', otvod_58)

seet59 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
seet59.place(x=570, y=600)
seet59.bind('<Button-1>', navod_59)
seet59.bind('<ButtonRelease-3>', otvod_59)

seet510 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
seet510.place(x=620, y=600)
seet510.bind('<Button-1>', navod_510)
seet510.bind('<ButtonRelease-3>', otvod_510)

seet511 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
seet511.place(x=670, y=600)
seet511.bind('<Button-1>', navod_511)
seet511.bind('<ButtonRelease-3>', otvod_511)

seet512 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
seet512.place(x=720, y=600)
seet512.bind('<Button-1>', navod_512)
seet512.bind('<ButtonRelease-3>', otvod_512)

seet513 = Button(W, image=seet_button, borderwidth=0, background=bg_color, activebackground=bg_color)
seet513.place(x=770, y=600)
seet513.bind('<Button-1>', navod_513)
seet513.bind('<ButtonRelease-3>', otvod_513)


W.mainloop()