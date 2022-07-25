from mido import Message,MidiFile,MidiTrack,MetaMessage,bpm2tempo
def incr():
    global i,char
    i+=1
    char=st[i]
mid=MidiFile()
st="240@1l8o4(6c)l4de,d,ceddl6cdcc,,@2l2o3c.<g."
notes="cCdDefFgGaAb"
i=0
ddump=""
while i<len(st):
    char=st[i]
    if char=="@":
        if ddump:
            mid.tracks.append(MidiTrack([MetaMessage('midi_port',port=0),MetaMessage('set_tempo',tempo=bpm2tempo(int(ddump)))]))
            ddump=""
        incr()
        track=MidiTrack()
        mid.tracks.append(track)
        track.append(MetaMessage('midi_port',port=int(char,16)))
        l,o,v=4,4,64# LOV <3
        s=0
        while char!="@" and i<len(st)-1:
            incr()
            if char=='<':o-=1
            elif char=='>':o+=1
            elif char=='+':v+=1
            elif char=='-':v-=1
            elif char=='l':
                d=''
                incr()
                while char.isdigit():
                    d+=char
                    incr()
                i-=1
                l=int(d)
            elif char=='o':
                i+=1
                o=int(st[i])
            elif char=='v':
                i+=1
                v=int(st[i],16)
            elif char=="'":
                d=''
                incr()
                while char!="'":
                    d+=char
                    incr()
                track.append(MetaMessage('lyrics',text=d))
            elif char in notes:
                n=notes.index(char)+12*(o+1)
                track.extend([Message('note_on',note=n,velocity=v,time=int(s) if s else 0),Message('note_off',note=n,velocity=127,time=int(1920/l))])
                if s:s=0
            elif char==',':track[-1].time+=int(1920/l)
            elif char=='.':s+=1920/l
            elif char=='(':
                ids=i
                r=''
                incr()
                while char.isdigit():
                    r+=char
                    incr()
                ida=i
                level=1
                while level:
                    incr()
                    if char==')':level-=1
                    elif char=='(':level+=1
                st=st[:ids]+(int(r) if r else 2)*st[ida:i]+st[i+1:]
                i=ids-1
        i-=1
    elif char.isdigit:ddump+=char
    i+=1
mid.save('new_song.mid')
print(mid.tracks)

from os import system
system(r'D:\MidiSheetMusic-2.6.2.exe C:\Users\breva\LOV\new_song.mid')