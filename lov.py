from mido import Message,MidiFile,MidiTrack,MetaMessage,bpm2tempo
def t(x:int)->int:return int(1920/x)
mid=MidiFile()
st="120@1l4o4cccde,d,ceddl1c"
notes="cCdDefFgGaAb"
i=0
while i<len(st):
    char=st[i]
    ddump=""
    if char=="@":
        if ddump:mid.tracks.append(MidiTrack([MetaMessage('midi_port',port=0),MetaMessage('set_tempo',tempo=bpm2tempo(int(ddump)))]))
        i+=1
        char=st[i]
        track=MidiTrack()
        mid.tracks.append(track)
        track.append(MetaMessage('midi_port',port=int(char,16)))
        l=4
        o=4
        v=64
        s=0
        while char!="@" and i<len(st)-1:
            i+=1
            char=st[i]
            if char=='<':o-=1
            elif char=='>':o+=1
            elif char=='+':v+=1
            elif char=='-':v-=1
            elif char=='l':
                d=''
                i+=1
                char=st[i]
                while char.isdigit():
                    d+=char
                    i+=1
                    char=st[i]
                i-=1
                l=int(d)
            elif char=='o':
                i+=1
                o=int(st[i])
            elif char=='v':
                i+=1
                v=int(st[i],16)
            elif char=='"':
                d=''
                i+=1
                char=st[i]
                while char!='"':
                    d+=char
                    i+=1
                    char=st[i]
                track.append(MetaMessage('lyrics',text=d))
            elif char in notes:
                n=notes.index(char)+12*(o+1)
                track.extend([Message('note_on',note=n,velocity=v,time=int(s) if s else 0),Message('note_off',note=n,velocity=127,time=int(1920/l))])
                if s:s=0
            elif char==',':track[-1].time+=int(1920/l)
            elif char=='.':s+=1920/l
        i-=1
    elif char.isdigit:ddump+=char
    i+=1
mid.save('new_song.mid')
print(mid.tracks)