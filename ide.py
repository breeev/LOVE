from tkinter import Tk as Window,Text,Frame,Button,Label
from tkinter.font import Font
from time import strftime

settingsWindowActive=False

def ex():
    global id,settingsWindowActive
    if settingsWindowActive:close()
    w.destroy()
def close(s):s.destroy()
def new():pass
def load():pass
def save():pass
def run():pass
def settings():
    settingsWindowActive=True
    s=Window()
    s.overrideredirect(True)
    s.config(bg=bgC)
    Button(s,text="Close",bg=bgC,fg=fgC,command=lambda:close(s)).pack()
    s.mainloop()
    settingsWindowActive=False

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
w.wm_attributes('-fullscreen','True')
x,y=w.winfo_screenwidth(),w.winfo_screenheight()

# static
sF=Font(family='Arial',size=16)

bgC='black'
fgC='lime'
Pside='left'# side-pannel side
source=''# where text files are stored
dest=''# where mid files are stored
tF=Font(family='Terminal',size=13)# text box font

side=Frame(w,width=50,bg=bgC,bd=0).pack(fill='y',side=Pside)
status=Frame(w,height=25,bg=bgC,bd=0).pack(fill='x',side='bottom')
text=Text(w,bg=bgC,fg=fgC,insertbackground=fgC,font=tF,bd=50,relief='sunken').pack(expand=True,fill='both')
for i,b in enumerate(chars):btns[b]=Button(side,bg=bgC,fg=fgC,activebackground=fgC,activeforeground=bgC,text=chars[b],font=sF,relief='flat',command=fcts[i]).place(x=x-50 if Pside=='right' else 1,y=10+50*i)
time1=''
clock=Label(w,bg=bgC,fg=fgC)
clock.place(x=x-40,y=y-23)
def tick():
    """Controls the clock (bottom right on status bar)."""
    global time1,id
    time2=strftime('%H:%M')# get current time
    if time2!=time1:time1=time2;clock.config(text=time2)# if time string has changed, update it
    clock.after(1000,tick)# calls itself every second to update the time display as needed
tick()
w.focus_force()
w.mainloop()