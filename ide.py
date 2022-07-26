from tkinter import Tk as Window,Text,Frame,Button,PhotoImage
from tkinter.font import Font
from cairosvg import svg2png

backgroundColor='black'
foregroundColor='lime'
chars={
    'exit':'\u274E',
    'new':'\u2747',
    'load':'\u2934',
    'save':'\u2935',
    'run':'\u25B6',
    'settings':'\u2699'
}
btns={}

def ex():root.destroy()
def new():pass
def load():pass
def save():pass
def run():pass
def settings():pass
fcts=[ex,new,load,save,run,settings]

root=Window()
sideFont=Font(family='Arial',size=16)
root.wm_attributes('-fullscreen', 'True')
side=Frame(root,width=50,bg=backgroundColor,relief='ridge',bd=1).pack(fill='y',side='left')
status=Frame(root,height=20,bg=backgroundColor,relief='ridge',bd=1).pack(fill='x',side='bottom')
text=Text(root,bg=backgroundColor).pack(expand=True, fill='both')
for i,b in enumerate(chars):btns[b]=Button(side,bg=backgroundColor,fg=foregroundColor,activebackground=foregroundColor,activeforeground=backgroundColor,text=chars[b],font=sideFont,relief='flat',command=fcts[i]).place(x=1,y=10+50*i)
root.focus_force()
root.mainloop()