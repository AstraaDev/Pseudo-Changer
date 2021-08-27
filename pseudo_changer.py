from tkinter import *
import tkinter.font as font

t1=""
t2=""
pseudo = ""
recup = ""

def launch():

    def transition():
        convert()

    # label 0
    lbl0=Label(text='Pseudo Changer', font=("bold", 18))
    lbl0.place(x=82, y=12)
    # label 1
    lbl1=Label(text='Pseudo:')
    lbl1.place(x=0, y=78)
    # label 2
    lbl2=Label(text='Result:')
    lbl2.place(x=0, y=131)

    # text 1
    t1=Entry(bd=2, width=45)
    t1.place(x=57, y=78)
    # text 2
    t2=Entry(bd=2, width=45)
    t2.place(x=57, y=131)
    t2.configure(state="readonly")

    # boutton 1
    tb = font.Font(size=14)
    b1=Button(text='Convert', command=transition)
    b1.place(x=70, y=205)
    b1['font'] = tb
    # boutton 2
    b2=Button(text='Reset', command=reset)
    b2.place(x=151, y=205)
    b2['font'] = tb
    # boutton 3
    b3=Button(text='Copy', state = DISABLED, command=copy)
    b3.place(x=217, y=205)
    b3['font'] = tb

    def convert():
        global pseudo
        recup = t1.get()
        pseudo = recup.upper()

        o = "O"
        i = "I"
        z = "Z"
        e = "E"
        a = "A"
        s = "S"
        t = "T"
        b = "B"

        for o in o:
            pseudo = pseudo.replace(o, '0')
        for i in i:
            pseudo = pseudo.replace(i, '1')
        for z in z:
            pseudo = pseudo.replace(z, '2')
        for e in e:
            pseudo = pseudo.replace(e, '3')
        for a in a:
            pseudo = pseudo.replace(a, '4')
        for s in s:
            pseudo = pseudo.replace(s, '5')
        for t in t:
            pseudo = pseudo.replace(t, '7')
        for b in b:
            pseudo = pseudo.replace(b, '8')

        t2.configure(state="normal")
        t2.delete(0, 'end')
        t2.insert(0, pseudo)
        t2.configure(state="readonly")

        if (b3['state'] == DISABLED):
            b3['state'] = NORMAL
        else:
            b3['state'] = NORMAL
        
def copy():
    global pseudo
    window.clipboard_clear()
    window.clipboard_append(pseudo)
    window.update()

def reset():
    launch()

window=Tk()
mywin=launch()
window.title("PseudoChanger by Astraa")
window.geometry('350x250')
window.mainloop()