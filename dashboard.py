from tkinter import *

window=Tk()

window.title('Dashboard')
window.geometry('1270x668+0+0')
window.resizable(0,0)
window.config(bg='white')

bg_image=PhotoImage(file='inventory.png')
titleLable=Label(window,image=bg_image,compound=LEFT,text='                               سیستم فروش و انبار داری ',font=('Yekan',30,'bold'), bg='#813ffe',fg='#07070a',anchor='w',padx=20)
titleLable.place(x=0,y=0,relwidth=1)

logoButten=Button(window,text='خروج',font=('Yekan',16,'bold'),fg='#07070a')
logoButten.place(x=1100,y=10)

window.mainloop()

