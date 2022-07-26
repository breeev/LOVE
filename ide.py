from tkinter import Tk as Window,Text,Frame,Button,Label,Entry,LabelFrame,OptionMenu,StringVar
from tkinter.font import Font
from tkinter.ttk import Style
from time import strftime

w=Window()
w.title('LOV IDE <3')
w.wm_attributes('-fullscreen','True')
x,y=w.winfo_screenwidth(),w.winfo_screenheight()
s=None

with open('preferences') as f:exec(f.read())

def t(w:Entry,t:str):
    """Modify the text of a Tkinter Entry object."""
    w.delete(0,'end')
    w.insert(0,t)

def ex(e=None):
    global id,s
    try:Close(s)
    except:pass
    w.destroy()
def new(e=None):print(e)
def load(e=None):pass
def save(e=None):pass
def run(e=None):pass

def settings(e=None):
    global x,y,s,ffamily,fsize,bgc,fgc,pside,relief,bd
    s=Window()
    width=480
    height=480
    s.geometry(f'{width}x{height}+{int((x/2)-(width/2))}+{int((y/2)-(height/2))}')
    s.overrideredirect(True)
    s.attributes('-topmost',True)
    s.config(bg=fgC)
    border=1
    Frame(s,bg=bgC,width=width-2*border,height=height-2*border).place(x=border,y=border)
    c=LabelFrame(s,text="Customisation",fg=fgC,bg=bgC)
    c.grid(column=0,row=0,columnspan=3,padx=30,pady=30,ipadx=10,ipady=10)
    Label(c,text="Font family: ",bg=bgC,fg=fgC).grid(column=0,row=0,sticky='E')
    ffamily=Entry(c,bg=bgC,fg=fgC,insertbackground=fgC,selectbackground=fgC,selectforeground=bgC)
    ffamily.grid(column=1,row=0)
    t(ffamily,family)
    Label(c,text="Font size: ",bg=bgC,fg=fgC).grid(column=0,row=1,sticky='E')
    fsize=Entry(c,bg=bgC,fg=fgC,insertbackground=fgC,selectbackground=fgC,selectforeground=bgC)
    fsize.grid(column=1,row=1)
    t(fsize,size)
    Label(c,text="Background color: ",bg=bgC,fg=fgC).grid(column=0,row=2,sticky='E')
    bgc=Entry(c,bg=bgC,fg=fgC,insertbackground=fgC,selectbackground=fgC,selectforeground=bgC)
    bgc.grid(column=1,row=2)
    t(bgc,bgC)
    Label(c,text="Foreground color: ",bg=bgC,fg=fgC).grid(column=0,row=3,sticky='E')
    fgc=Entry(c,bg=bgC,fg=fgC,insertbackground=fgC,selectbackground=fgC,selectforeground=bgC)
    fgc.grid(column=1,row=3)
    t(fgc,fgC)
    Label(c,text="Panel side: ",bg=bgC,fg=fgC).grid(column=0,row=4,sticky='E')
    pside=StringVar(c)
    pside.set(Pside)
    o=OptionMenu(c,pside,'left','right')
    o.grid(column=1,row=4)
    o.config(bg=bgC,fg=fgC,activebackground=bgC,activeforeground=fgC,highlightthickness=0,width=15)
    Label(c,text="Text box relief: ",bg=bgC,fg=fgC).grid(column=0,row=5,sticky='E')
    relief=StringVar(c)
    relief.set(Relief)
    q=OptionMenu(c,relief,'flat','raised','sunken','groove','ridge')
    q.grid(column=1,row=5)
    q.config(bg=bgC,fg=fgC,activebackground=bgC,activeforeground=fgC,highlightthickness=0,width=15)
    Label(c,text="Text box border size: ",bg=bgC,fg=fgC).grid(column=0,row=6,sticky='E')
    bd=Entry(c,bg=bgC,fg=fgC,insertbackground=fgC,selectbackground=fgC,selectforeground=bgC)
    bd.grid(column=1,row=6)
    t(bd,Bd)
    b=[
        Button(s,text="Apply",bg=bgC,fg=fgC,activebackground=fgC,activeforeground=bgC,command=Apply),
        Button(s,text="Save",bg=bgC,fg=fgC,activebackground=fgC,activeforeground=bgC,command=Save),
        Button(s,text="Close",bg=bgC,fg=fgC,activebackground=fgC,activeforeground=bgC,command=lambda:Close(s)),
    ]
    for i in range(0,3):b[i].grid(column=i,row=1)
    s.mainloop()

def Apply():pass
def Save():
    data=f"""# text box font
family='{ffamily.get()}'
size={fsize.get()}
bgC='{bgc.get()}'
fgC='{fgc.get()}'
Pside='{pside.get()}'# side-pannel side
Relief='{relief.get()}'
Bd={bd.get()}"""
    with open('preferences','w') as f:f.write(data)
def Close(s):s.destroy()

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

w.bind('<Control-q>',ex)
w.bind('<Control-n>',new)
w.bind('<Control-o>',load)
w.bind('<Control-s>',save)
w.bind('<F5>',run)
w.bind('<Control-Shift-P>',settings)

# static
sF=Font(family='Arial',size=16)
tF=Font(family=family,size=size)

side=Frame(w,width=50,bg=bgC,bd=0).pack(fill='y',side=Pside)
status=Frame(w,height=25,bg=bgC,bd=0).pack(fill='x',side='bottom')
text=Text(w,bg=bgC,fg=fgC,insertbackground=fgC,font=tF,bd=Bd,relief=Relief,selectbackground=fgC,selectforeground=bgC).pack(expand=True,fill='both')
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