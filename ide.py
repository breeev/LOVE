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
    global x,y,s,ffamily,fsize,bgc,fgc,pside,relief,bd,f1,f2,f3,f4,f5,f6,f7,f8,c,o,q,butt
    s=Window()
    width=480
    height=480
    s.geometry(f'{width}x{height}+{int((x/2)-(width/2))}+{int((y/2)-(height/2))}')
    s.overrideredirect(True)
    s.attributes('-topmost',True)
    s.config(bg=fgC)
    border=1
    f1=Frame(s,bg=bgC,width=width-2*border,height=height-2*border)
    f1.place(x=border,y=border)
    c=LabelFrame(s,text="Customisation",fg=fgC,bg=bgC)
    c.grid(column=0,row=0,columnspan=3,padx=30,pady=30,ipadx=10,ipady=10)
    f2=Label(c,text="Font family: ",bg=bgC,fg=fgC)
    f2.grid(column=0,row=0,sticky='E')
    ffamily=Entry(c,bg=bgC,fg=fgC,insertbackground=fgC,selectbackground=fgC,selectforeground=bgC)
    ffamily.grid(column=1,row=0)
    t(ffamily,family)
    f3=Label(c,text="Font size: ",bg=bgC,fg=fgC)
    f3.grid(column=0,row=1,sticky='E')
    fsize=Entry(c,bg=bgC,fg=fgC,insertbackground=fgC,selectbackground=fgC,selectforeground=bgC)
    fsize.grid(column=1,row=1)
    t(fsize,size)
    f4=Label(c,text="Background color: ",bg=bgC,fg=fgC)
    f4.grid(column=0,row=2,sticky='E')
    bgc=Entry(c,bg=bgC,fg=fgC,insertbackground=fgC,selectbackground=fgC,selectforeground=bgC)
    bgc.grid(column=1,row=2)
    t(bgc,bgC)
    f5=Label(c,text="Foreground color: ",bg=bgC,fg=fgC)
    f5.grid(column=0,row=3,sticky='E')
    fgc=Entry(c,bg=bgC,fg=fgC,insertbackground=fgC,selectbackground=fgC,selectforeground=bgC)
    fgc.grid(column=1,row=3)
    t(fgc,fgC)
    f6=Label(c,text="Panel side: ",bg=bgC,fg=fgC)
    f6.grid(column=0,row=4,sticky='E')
    pside=StringVar(c)
    pside.set(Pside)
    o=OptionMenu(c,pside,'left','right')
    o.grid(column=1,row=4)
    o.config(bg=bgC,fg=fgC,activebackground=fgC,activeforeground=bgC,highlightthickness=0,width=15)
    f7=Label(c,text="Text box relief: ",bg=bgC,fg=fgC)
    f7.grid(column=0,row=5,sticky='E')
    relief=StringVar(c)
    relief.set(Relief)
    q=OptionMenu(c,relief,'flat','raised','sunken','groove','ridge')
    q.grid(column=1,row=5)
    q.config(bg=bgC,fg=fgC,activebackground=fgC,activeforeground=bgC,highlightthickness=0,width=15)
    f8=Label(c,text="Text box border size: ",bg=bgC,fg=fgC)
    f8.grid(column=0,row=6,sticky='E')
    bd=Entry(c,bg=bgC,fg=fgC,insertbackground=fgC,selectbackground=fgC,selectforeground=bgC)
    bd.grid(column=1,row=6)
    t(bd,Bd)
    butt=[
        Button(s,text="Apply",bg=bgC,fg=fgC,activebackground=fgC,activeforeground=bgC,command=Apply),
        Button(s,text="Save",bg=bgC,fg=fgC,activebackground=fgC,activeforeground=bgC,command=Save),
        Button(s,text="Close",bg=bgC,fg=fgC,activebackground=fgC,activeforeground=bgC,command=lambda:Close(s)),
    ]
    for i in range(0,3):butt[i].grid(column=i,row=1)
    s.mainloop()

def Apply():
    global x,y,s,ffamily,fsize,bgc,fgc,pside,relief,bd,f1,f2,f3,f4,f5,f6,f7,f8,c,o,q,butt,chars,family,size,bgC,fgC,Pside,Relief,Bd,tF
    frames=[f1,side,status]
    labelframes=[c]
    labels=[f2,f3,f4,f5,f6,f7,f8,clock]
    entries=[ffamily,fsize,bgc,fgc,bd]
    buttons=[*butt,*[btns[i] for i in btns]]
    optionmenus=[o,q]
    texts=[text]
    family=ffamily.get()
    size=int(fsize.get())
    bgC=bgc.get()
    fgC=fgc.get()
    Pside=pside.get()
    Relief=relief.get()
    Bd=int(bd.get())
    tF=Font(family=family,size=size)
    s.config(bg=fgC)
    for widget in frames:widget.configure(bg=bgC)
    for widget in labelframes+labels:widget.configure(bg=bgC,fg=fgC)
    for widget in buttons+optionmenus:widget.configure(bg=bgC,fg=fgC,activebackground=fgC,activeforeground=bgC)
    for widget in entries:widget.configure(bg=bgC,fg=fgC,insertbackground=fgC,selectbackground=fgC,selectforeground=bgC)
    for widget in texts:widget.configure(bg=bgC,fg=fgC,insertbackground=fgC,selectbackground=fgC,selectforeground=bgC,font=tF,relief=Relief,bd=Bd)
    side.pack(fill='y',side=Pside)
    for i,z in enumerate(chars):btns[z].place(x=x-50 if Pside=='right' else 1,y=10+50*i)
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

side=Frame(w,width=50,bg=bgC,bd=0)
side.pack(fill='y',side=Pside)
status=Frame(w,height=25,bg=bgC,bd=0)
status.pack(fill='x',side='bottom')
text=Text(w,bg=bgC,fg=fgC,insertbackground=fgC,font=tF,bd=Bd,relief=Relief,selectbackground=fgC,selectforeground=bgC)
text.pack(expand=True,fill='both')
for i,v in enumerate(chars):
    btns[v]=Button(w,bg=bgC,fg=fgC,activebackground=fgC,activeforeground=bgC,text=chars[v],font=sF,relief='flat',command=fcts[i])
    btns[v].place(x=x-50 if Pside=='right' else 1,y=10+50*i)
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