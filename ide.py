from tkinter import Tk as Window,Text,Frame,Button
from tkinter.font import Font

bgC='black'
fgC='lime'

def ex():w.destroy()
def new():pass
def load():pass
def save():pass
def run():pass
def settings():pass

chars={
    'exit':'\u274E',
    'new':'\u2747',
    'load':'\u2934',
    'save':'\u2935',
    'run':'\u25B6',
    'settings':'\u2699'
}
fcts=[ex,new,load,save,run,settings]
btns={}

w=Window()
w.title('LOV IDE <3')

sF=Font(family='Arial',size=16)
tF=Font(family='Terminal',size=13)

w.wm_attributes('-fullscreen','True')
side=Frame(w,width=50,bg=bgC,relief='ridge',bd=0).pack(fill='y',side='left')
status=Frame(w,height=20,bg=bgC,relief='ridge',bd=1).pack(fill='x',side='bottom')
text=Text(w,bg=bgC,fg=fgC,insertbackground=fgC,font=tF,bd=20).pack(expand=True,fill='both')
for i,b in enumerate(chars):btns[b]=Button(side,bg=bgC,fg=fgC,activebackground=fgC,activeforeground=bgC,text=chars[b],font=sF,relief='flat',command=fcts[i]).place(x=1,y=10+50*i)
w.focus_force()
w.mainloop()