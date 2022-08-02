from genericpath import exists
from re import search
from select import select
from time import strftime
from tkinter.font import Font,families
from tkinter.messagebox import askokcancel, showerror, showwarning
from tkinter.filedialog import askopenfile, askopenfilename
from ctypes import windll
from idlelib.tooltip import Hovertip
from tkinter import INSERT,Tk as Window,Button,Entry,Frame,Label,LabelFrame,OptionMenu,StringVar,Text,Scrollbar,Canvas
from os.path import realpath

from lov import interpreter# <3

colors=['snow','ghost white','white smoke','gainsboro','floral white','old lace','linen','antique white','papaya whip','blanched almond','bisque','peach puff','navajo white','lemon chiffon','mint cream','azure','alice blue','lavender','lavender blush','misty rose','dark slate gray','dim gray','slate gray','light slate gray','gray','light grey','midnight blue','navy','cornflower blue','dark slate blue','slate blue','medium slate blue','light slate blue','medium blue','royal blue', 'blue','dodger blue','deep sky blue','sky blue','light sky blue','steel blue','light steel blue','light blue','powder blue','pale turquoise','dark turquoise','medium turquoise','turquoise','cyan','light cyan','cadet blue','medium aquamarine','aquamarine','dark green','dark olive green','dark sea green','sea green','medium sea green','light sea green','pale green','spring green','lawn green','medium spring green','green yellow','lime green','yellow green','forest green','olive drab','dark khaki','khaki','pale goldenrod','light goldenrod yellow','light yellow','yellow','gold','light goldenrod','goldenrod','dark goldenrod','rosy brown','indian red','saddle brown','sandy brown','dark salmon','salmon','light salmon','orange','dark orange','coral','light coral','tomato','orange red','red','hot pink','deep pink','pink','light pink','pale violet red','maroon','medium violet red','violet red','medium orchid','dark orchid','dark violet','blue violet','purple','medium purple','thistle','snow2','snow3','snow4','seashell2','seashell3','seashell4','AntiqueWhite1','AntiqueWhite2','AntiqueWhite3','AntiqueWhite4','bisque2','bisque3','bisque4','PeachPuff2','PeachPuff3','PeachPuff4','NavajoWhite2','NavajoWhite3','NavajoWhite4','LemonChiffon2','LemonChiffon3','LemonChiffon4','cornsilk2','cornsilk3','cornsilk4','ivory2','ivory3','ivory4','honeydew2','honeydew3','honeydew4','LavenderBlush2','LavenderBlush3','LavenderBlush4','MistyRose2','MistyRose3','MistyRose4','azure2','azure3','azure4','SlateBlue1','SlateBlue2','SlateBlue3','SlateBlue4','RoyalBlue1','RoyalBlue2','RoyalBlue3','RoyalBlue4','blue2','blue4','DodgerBlue2','DodgerBlue3','DodgerBlue4','SteelBlue1','SteelBlue2','SteelBlue3','SteelBlue4','DeepSkyBlue2','DeepSkyBlue3','DeepSkyBlue4','SkyBlue1','SkyBlue2','SkyBlue3','SkyBlue4','LightSkyBlue1','LightSkyBlue2','LightSkyBlue3','LightSkyBlue4','SlateGray1','SlateGray2','SlateGray3','SlateGray4','LightSteelBlue1','LightSteelBlue2','LightSteelBlue3','LightSteelBlue4','LightBlue1','LightBlue2','LightBlue3','LightBlue4','LightCyan2','LightCyan3','LightCyan4','PaleTurquoise1','PaleTurquoise2','PaleTurquoise3','PaleTurquoise4','CadetBlue1','CadetBlue2','CadetBlue3','CadetBlue4','turquoise1','turquoise2','turquoise3','turquoise4','cyan2','cyan3','cyan4','DarkSlateGray1','DarkSlateGray2','DarkSlateGray3','DarkSlateGray4','aquamarine2','aquamarine4','DarkSeaGreen1','DarkSeaGreen2','DarkSeaGreen3','DarkSeaGreen4','SeaGreen1','SeaGreen2','SeaGreen3','PaleGreen1','PaleGreen2','PaleGreen3','PaleGreen4','SpringGreen2','SpringGreen3','SpringGreen4','green2','green3','green4','chartreuse2','chartreuse3','chartreuse4','OliveDrab1','OliveDrab2','OliveDrab4','DarkOliveGreen1','DarkOliveGreen2','DarkOliveGreen3','DarkOliveGreen4','khaki1','khaki2','khaki3','khaki4','LightGoldenrod1','LightGoldenrod2','LightGoldenrod3','LightGoldenrod4','LightYellow2','LightYellow3','LightYellow4','yellow2','yellow3','yellow4','gold2','gold3','gold4','goldenrod1','goldenrod2','goldenrod3','goldenrod4','DarkGoldenrod1','DarkGoldenrod2','DarkGoldenrod3','DarkGoldenrod4','RosyBrown1','RosyBrown2','RosyBrown3','RosyBrown4','IndianRed1','IndianRed2','IndianRed3','IndianRed4','sienna1','sienna2','sienna3','sienna4','burlywood1','burlywood2','burlywood3','burlywood4','wheat1','wheat2','wheat3','wheat4','tan1','tan2','tan4','chocolate1','chocolate2','chocolate3','firebrick1','firebrick2','firebrick3','firebrick4','brown1','brown2','brown3','brown4','salmon1','salmon2','salmon3','salmon4','LightSalmon2','LightSalmon3','LightSalmon4','orange2','orange3','orange4','DarkOrange1','DarkOrange2','DarkOrange3','DarkOrange4','coral1','coral2','coral3','coral4','tomato2','tomato3','tomato4','OrangeRed2','OrangeRed3','OrangeRed4','red2','red3','red4','DeepPink2','DeepPink3','DeepPink4','HotPink1','HotPink2','HotPink3','HotPink4','pink1','pink2','pink3','pink4','LightPink1','LightPink2','LightPink3','LightPink4','PaleVioletRed1','PaleVioletRed2','PaleVioletRed3','PaleVioletRed4','maroon1','maroon2','maroon3','maroon4','VioletRed1','VioletRed2','VioletRed3','VioletRed4','magenta2','magenta3','magenta4','orchid1','orchid2','orchid3','orchid4','plum1','plum2','plum3','plum4','MediumOrchid1','MediumOrchid2','MediumOrchid3','MediumOrchid4','DarkOrchid1','DarkOrchid2','DarkOrchid3','DarkOrchid4','purple1','purple2','purple3','purple4','MediumPurple1','MediumPurple2','MediumPurple3','MediumPurple4','thistle1','thistle2','thistle3','thistle4','gray1','gray2','gray3','gray4','gray5','gray6','gray7','gray8','gray9','gray10','gray11','gray12','gray13','gray14','gray15','gray16','gray17','gray18','gray19','gray20','gray21','gray22','gray23','gray24','gray25','gray26','gray27','gray28','gray29','gray30','gray31','gray32','gray33','gray34','gray35','gray36','gray37','gray38','gray39','gray40','gray42','gray43','gray44','gray45','gray46','gray47','gray48','gray49','gray50','gray51','gray52','gray53','gray54','gray55','gray56','gray57','gray58','gray59','gray60','gray61','gray62','gray63','gray64','gray65','gray66','gray67','gray68','gray69','gray70','gray71','gray72','gray73','gray74','gray75','gray76','gray77','gray78','gray79','gray80','gray81','gray82','gray83','gray84','gray85','gray86','gray87','gray88','gray89','gray90','gray91','gray92','gray93','gray94','gray95','gray97','gray98','gray99','white']

w=Window()
w.title('LOV IDE <3')
w.wm_attributes('-fullscreen','True')
x,y=w.winfo_screenwidth(),w.winfo_screenheight()
saved=True# if you don't write anything, there's nothing to save

with open('preferences') as f:exec(f.read())
if not Src:Src='/'.join(realpath(__file__).split('\\')[:-1])
if not Exp:Exp='/'.join(realpath(__file__).split('\\')[:-1])

def t(w:Entry,t:str):
    """Modify the text of a Tkinter Entry object."""
    w.delete(0,'end')
    w.insert(0,t)
def ex(e=None):
    global id,saved
    if saved or askokcancel('Confirm Exit','Your document will be lost.'):
        for win in ['s','g','root']:
            try:exec(win+'.destroy()')
            except:pass
        w.destroy()
def restart(e=None):
    global saved
    if saved or askokcancel('Confirm Restart','Your document will be lost.'):
        ex()
        from os import execl
        from sys import executable as e,argv
        execl(e,e,*argv)
def new(e=None):
    global saved
    if saved or askokcancel('Confirm New','Your document will be lost.'):
        pass
def load(e=None):
    global saved
    if saved or askokcancel('Confirm Load','Your document will be lost.'):
        pass
def save(e=None):
    global saved
    if not saved:
        data=text.get('1.0','end-1c')
        result=search(r't[0-9]+',data)
        a,b=(None,None) if not result else result.span()
        path=data.splitlines()[0]+'.midi'if a and '\n'in data[:b]else askopenfilename(initialdir=Src)
        if not path or (exists(path) and not askokcancel('Overwrite?','File already exists. Overwrite?')):return
        with open(path,'w') as f:f.write(data)
        saved=True
def play(e=None):
    try:interpreter(text.get('1.0','end-1c'),Exe)
    except Exception as e:showerror('Error',e)
def export(e=None):
    try:interpreter(text.get('1.0','end-1c'),export=Exp)
    except Exception as e:showerror('Error',str(e).title())

def colorshowcase(e=None):
    global inventory,g
    g=Window()
    g.bind('<Control-q>',ex)
    g.geometry('1164x800')
    i=0
    for u in colors:
        Label(g,text=u,bg=u,width=13).place(x=97*(i//800),y=i%800)
        i+=20
    g.mainloop()
def fontshowcase(e=None):
    global inventory,root
    root=Window()
    root.bind('<Control-q>',ex)
    root.title('Font Families')
    fonts=list(families())
    fonts.sort()
    def populate(frame):
        '''Put in the fonts'''
        listnumber = 1
        for item in fonts:
            Label(frame,text=item,font=(item,16)).pack()
            listnumber+=1
    def onFrameConfigure(canvas):
        '''Reset the scroll region to encompass the inner frame'''
        canvas.configure(scrollregion=canvas.bbox("all"))
    canvas=Canvas(root,borderwidth=0,background="#ffffff")
    frame=Frame(canvas,background="#ffffff")
    vsb=Scrollbar(root,orient="vertical",command=canvas.yview)
    canvas.configure(yscrollcommand=vsb.set)
    vsb.pack(side="right",fill="y")
    canvas.pack(side="left",fill="both",expand=True)
    canvas.create_window((4,4),window=frame,anchor="nw")
    frame.bind("<Configure>",lambda event,canvas=canvas:onFrameConfigure(canvas))
    populate(frame)
    root.mainloop()
def settings(e=None):
    global x,y,s,family,size,bgc,fgc,pside,relief,bd,f1,f2,f3,f4,f5,f6,f7,f8,c,o,q,butt,link,src,exp,fonting,f,f9,f10,exe,f11
    try:s.focus_force()
    except:s=Window()
    s.bind('<Control-q>',ex)
    width,height=480,480
    s.geometry(f'+{int((x/2)-(width/2))}+{int((y/2)-(height/2))}')
    s.overrideredirect(True)
    s.config(bg=fgC)
    border=1
    f1=Frame(s,bg=bgC,width=width-2*border,height=height-2*border)
    f1.place(x=border,y=border)
    lastClickX=0
    lastClickY=0
    def SaveLastClickPos(event):
        global lastClickX,lastClickY
        lastClickX=event.x
        lastClickY=event.y
    def Dragging(event):
        xx,yy=event.x-lastClickX+s.winfo_x(),event.y-lastClickY+s.winfo_y()
        s.geometry("+%s+%s" % (xx,yy))
    f1.bind('<Button-1>',SaveLastClickPos)
    f1.bind('<B1-Motion>',Dragging)
    c=LabelFrame(s,text="Customisation",fg=fgC,bg=bgC)
    c.grid(column=0,row=0,columnspan=3,padx=30,pady=30,ipadx=10,ipady=10)
    f2=Label(c,text="Font family: ",bg=bgC,fg=fgC)
    f2.grid(column=0,row=0,sticky='E')
    family=Entry(c,bg=bgC,fg=fgC,insertbackground=fgC,selectbackground=fgC,selectforeground=bgC)
    family.grid(column=1,row=0)
    t(family,Family)
    f3=Label(c,text="Font size: ",bg=bgC,fg=fgC)
    f3.grid(column=0,row=1,sticky='E')
    size=Entry(c,bg=bgC,fg=fgC,insertbackground=fgC,selectbackground=fgC,selectforeground=bgC)
    size.grid(column=1,row=1)
    t(size,Size)
    fonting=Button(c,text="Tkinter fonts",bg=bgC,fg=fgC,activebackground=fgC,activeforeground=bgC,command=fontshowcase,width=15)
    fonting.grid(column=1,row=2)
    f4=Label(c,text="Background color: ",bg=bgC,fg=fgC)
    f4.grid(column=0,row=3,sticky='E')
    bgc=Entry(c,bg=bgC,fg=fgC,insertbackground=fgC,selectbackground=fgC,selectforeground=bgC)
    bgc.grid(column=1,row=3)
    t(bgc,bgC)
    f5=Label(c,text="Foreground color: ",bg=bgC,fg=fgC)
    f5.grid(column=0,row=4,sticky='E')
    fgc=Entry(c,bg=bgC,fg=fgC,insertbackground=fgC,selectbackground=fgC,selectforeground=bgC)
    fgc.grid(column=1,row=4)
    t(fgc,fgC)
    link=Button(c,text="Tkinter colors",bg=bgC,fg=fgC,activebackground=fgC,activeforeground=bgC,command=colorshowcase,width=15)
    link.grid(column=1,row=5)
    f6=Label(c,text="Panel side: ",bg=bgC,fg=fgC)
    f6.grid(column=0,row=6,sticky='E')
    pside=StringVar(c)
    pside.set(Side)
    o=OptionMenu(c,pside,'left','right')
    o['menu'].config(bg=bgC,fg=fgC,activebackground=fgC,activeforeground=bgC)
    o.grid(column=1,row=6)
    o.config(bg=bgC,fg=fgC,activebackground=fgC,activeforeground=bgC,highlightthickness=0,width=15)
    Hovertip(o,'Side of the side pannel\n(where the main buttons are)')
    f7=Label(c,text="Text box relief: ",bg=bgC,fg=fgC)
    f7.grid(column=0,row=7,sticky='E')
    relief=StringVar(c)
    relief.set(Relief)
    q=OptionMenu(c,relief,'flat','raised','sunken','groove','ridge')
    q['menu'].config(bg=bgC,fg=fgC,activebackground=fgC,activeforeground=bgC)
    q.grid(column=1,row=7)
    q.config(bg=bgC,fg=fgC,activebackground=fgC,activeforeground=bgC,highlightthickness=0,width=15)
    Hovertip(q,'Style of the text box border')
    f8=Label(c,text="Text box border size: ",bg=bgC,fg=fgC)
    f8.grid(column=0,row=8,sticky='E')
    bd=Entry(c,bg=bgC,fg=fgC,insertbackground=fgC,selectbackground=fgC,selectforeground=bgC)
    bd.grid(column=1,row=8)
    t(bd,Bd)
    f=LabelFrame(s,text="Files and folders",fg=fgC,bg=bgC)
    f.grid(column=0,row=1,columnspan=3,padx=30,pady=30,ipadx=10,ipady=10)
    f9=Label(f,text="Source folder: ",bg=bgC,fg=fgC)
    f9.grid(column=0,row=0,sticky='E')
    src=Entry(f,bg=bgC,fg=fgC,insertbackground=fgC,selectbackground=fgC,selectforeground=bgC,width=30)
    src.grid(column=1,row=0)
    t(src,Src)
    Hovertip(src,'Where you store your text files\n(where to look when opening a file)',500)
    f10=Label(f,text="Export folder: ",bg=bgC,fg=fgC)
    f10.grid(column=0,row=1,sticky='E')
    exp=Entry(f,bg=bgC,fg=fgC,insertbackground=fgC,selectbackground=fgC,selectforeground=bgC,width=30)
    exp.grid(column=1,row=1)
    t(exp,Exp)
    Hovertip(exp,'Where to store exported text files (midi files)')
    f11=Label(f,text="Executable path: ",bg=bgC,fg=fgC)
    f11.grid(column=0,row=2,sticky='E')
    exe=Entry(f,bg=bgC,fg=fgC,insertbackground=fgC,selectbackground=fgC,selectforeground=bgC,width=30)
    exe.grid(column=1,row=2)
    t(exe,Exe)
    butt=[Button(s,text="Apply",bg=bgC,fg=fgC,activebackground=fgC,activeforeground=bgC,command=Apply),Button(s,text="Save",bg=bgC,fg=fgC,activebackground=fgC,activeforeground=bgC,command=Save),Button(s,text="Close",bg=bgC,fg=fgC,activebackground=fgC,activeforeground=bgC,command=lambda:s.destroy())]
    sticks=['e','n','w']
    for i in range(0,3):butt[i].grid(column=i,row=2,sticky=sticks[i])
    s.mainloop()

def Apply():
    global x,y,s,family,size,bgc,fgc,side,relief,bd,f1,f2,f3,f4,f5,f6,f7,f8,c,o,q,butt,chars,Family,Size,bgC,fgC,Side,Relief,Bd,link,fonting,f,f9,f10,src,exp,exe,f11
    frames=[f1,side,status]
    labelframes=[c,f]
    labels=[f2,f3,f4,f5,f6,f7,f8,f9,f10,clock,f11]
    entries=[family,size,bgc,fgc,bd,src,exp,exe]
    buttons=[*butt,*[btns[i] for i in btns],link,fonting]
    optionmenus=[o,q]
    texts=[text]
    Family=family.get()
    Size=int(size.get())
    bgC=bgc.get()
    fgC=fgc.get()
    Side=pside.get()
    Relief=relief.get()
    Bd=int(bd.get())
    s.config(bg=fgC)
    for widget in frames:widget.configure(bg=bgC)
    for widget in labelframes+labels:widget.configure(bg=bgC,fg=fgC)
    for widget in buttons+optionmenus:widget.configure(bg=bgC,fg=fgC,activebackground=fgC,activeforeground=bgC)
    for widget in optionmenus:widget['menu'].config(bg=bgC,fg=fgC,activebackground=fgC,activeforeground=bgC)
    for widget in entries:widget.configure(bg=bgC,fg=fgC,insertbackground=fgC,selectbackground=fgC,selectforeground=bgC)
    for widget in texts:widget.configure(bg=bgC,fg=fgC,insertbackground=fgC,selectbackground=fgC,selectforeground=bgC,font=Font(family=Family,size=Size),relief=Relief,bd=Bd)
    side.pack(fill='y',side=Side)
    for i,z in enumerate(chars):btns[z].place(x=x-60 if Side=='right' else -15,y=-2+60*i)
def Save():
    data=f"""# text box font
Family='{family.get()}'
Size={size.get() if size.get() else 0}
bgC='{bgc.get()}'
fgC='{fgc.get()}'
Side='{pside.get()}'# side-pannel side
Relief='{relief.get()}'
Bd={bd.get() if bd.get() else 0}
# Source and destination folders
Src=r'{src.get()}'# where to find text files
Exp=r'{exp.get()}'# where to put midi files
Exe=r'{exe.get()}'"""
    with open('preferences','w') as f:f.write(data)

chars={
    'exit':'\u2716',
    'restart':'\u2724',
    'new':'\u271A',
    'load':'\u2727',
    'save':'\u2726',
    'play':'\u2764',
    'export':'a',
    'settings':'\u2763'
}
fcts=[ex,restart,new,load,save,play,export,settings]
btns={}

w.bind('<Control-q>',ex)
w.bind('<Control-r>',restart)
w.bind('<Control-n>',new)
w.bind('<Control-o>',load)
w.bind('<Control-s>',save)
w.bind('<F5>',play)
w.bind('<Shift-F5>',export)
w.bind('<Control-Shift-P>',settings)

# static
sF=Font(family='Arial',size=30)
tF=Font(family=Family,size=Size)

side=Frame(w,width=50,bg=bgC,bd=0)
side.pack(fill='y',side=Side)
status=Frame(w,height=25,bg=bgC,bd=2)
status.pack(fill='x',side='bottom')
text=Text(w,bg=bgC,fg=fgC,insertbackground=fgC,font=tF,bd=Bd,relief=Relief,selectbackground=fgC,selectforeground=bgC)
text.pack(expand=True,fill='both')
for i,v in enumerate(chars):
    btns[v]=Button(w,bg=bgC,fg=fgC,activebackground=fgC,activeforeground=bgC,text=chars[v],font=sF,relief='flat',command=fcts[i])
    btns[v].place(x=x-60 if Side=='right' else -15,y=-2+60*i)
    btns[v].lower(belowThis=text)
    Hovertip(btns[v],v,hover_delay=500)
vcursor=StringVar(status)
vcursor.set('0 / 0')
cursor=Label(status,textvariable=vcursor,bg=bgC,fg=fgC)
cursor.grid(row=0,column=0,sticky='w')
vchsizes=StringVar(status)
chsizes=Label(status,textvariable=vchsizes,bg=bgC,fg=fgC)
chsizes.grid(row=0,column=1,padx=20)
def update(e=None):
    global saved
    u=len(text.get('1.0','end-1c').splitlines())
    vcursor.set(f"{text.index(INSERT)} / {u if u else 1}.{len(text.get('1.0','end-1c'))}")
    if u and saved:saved=False
lastString=''
def chsizeloop():
    global lastString
    newString=text.get('1.0','end-1c')
    try:
        if lastString!=newString:
            dic=interpreter(newString)
            vchsizes.set((8*' ').join([f'@{i}-{dic[i]}' for i in dic]))
    except Exception as e:print(f'Background interpreter failed: {e}')
    finally:
        lastString=newString
        chsizes.after(1000,chsizeloop)
chsizes.after(1000,chsizeloop)
text.bind('<KeyPress>',lambda e:cursor.after(1,update))
time1=''
vclock=StringVar(w)
clock=Label(w,textvariable=vclock,bg=bgC,fg=fgC)
clock.place(x=x-80,y=y-23)
al=-1
def tick():
    """Controls the clock (bottom right on status bar)."""
    global time1,id,al
    time2=strftime('%H:%M')# get current time
    if time2!=time1:
        time1=time2
        al+=1
        vclock.set(time2+" | {:0>2}:{:0>2}".format(al//60,al%60))# if time string has changed,update it
    clock.after(1000,tick)# calls itself every second to update the time display as needed
tick()
w.focus_force()
text.focus_force()
w.mainloop()
