from curses.ascii import isdigit
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
        track=MidiTrack()
        mid.tracks.append(track)
        track.append(MetaMessage('midi_port',port=int(st[i],16)))
        i+=1
        char=st[i]
        l=4
        o=4
        v=64
        while char!="@":
            if char=='<':o-=1
            elif char=='>':o+=1
            elif char=='+':v+=1
            elif char=='-':v-=1
            elif char=='l':
                d=''
                i+=1
                char=st[i]
                while char.isdigit:
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
            elif char=='e':
                d=''
                i+=1
                char=st[i]
                while char!='e':
                    d+=char
                    i+=1
                    char=st[i]
                track.append(MetaMessage('lyrics',text=d))
            elif char in notes:
                track.extend([Message('note_on',note=notes.index(char)+12*o,velocity=v),Message])
            i+=1
    elif char.isdigit:ddump+=char
    else:i+=1
track=MidiTrack()
mid.tracks.append(track)
track.append(MetaMessage('set_tempo',tempo=bpm2tempo(200)))
track.append(Message('note_on',note=64,velocity=64,time=0))
track.append(Message('note_off',note=64,velocity=127,time=t(3)))
track.append(Message('note_on',note=65,velocity=64,time=0))
track.append(Message('note_off',note=65,velocity=127,time=t(3)))
track.append(Message('note_on',note=66,velocity=64,time=0))
track.append(Message('note_off',note=66,velocity=127,time=t(3)))
mid.save('new_song.mid')