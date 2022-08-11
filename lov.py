from genericpath import exists
from os import mkdir
from mido import Message,MidiFile,MidiTrack,MetaMessage,bpm2tempo,tick2second
def interpreter(string:str,exe='',export='')->dict:
    # string=string.replace('\n','').replace(' ','')
    dic={}
    def incr():
        nonlocal i,char
        i+=1
        char=string[i]
    mid=MidiFile()
    # string="My First Song\nt240Tinky Winky... La-la@1l8o4((3c+))l4de,d,+c-e+d-dl6cv1dvFcc,,@2l2o3c.<g."
    notes="cCdDefFgGaAb"
    i=0
    ddump=""
    while i<len(string):
        char=string[i]
        if char=="@":
            if ddump:
                # print('{:>11}{:>5}'.format('BPM: ',ddump))
                dic['BPM']=ddump
                t=bpm2tempo(int(ddump))
                mid.tracks.append(MidiTrack([MetaMessage('midi_port',port=0),MetaMessage('set_tempo',tempo=t)]))
                ddump=""
            incr()
            track=MidiTrack()
            mid.tracks.append(track)
            track.append(MetaMessage('midi_port',port=int(char,16)))
            ch=char
            l,o,v=4,4,64# LOV <3
            t=60
            s=0
            while char!="@" and i<len(string)-1:
                incr()
                if char=='<':o-=1
                elif char=='>':o+=1
                elif char=='+' and v<127-14:v+=15
                elif char=='-' and v>0:v-=15
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
                    o=int(string[i])
                elif char=='v':
                    i+=1
                    v=int(2*string[i],16)
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
                        if char==')':level-=1
                        elif char=='(':level+=1
                        incr()
                    i-=1
                    string=string[:ids]+(int(r) if r else 2)*string[ida:i]+string[i+1:]
                    i=ids-1
            # print('Channel {}: {:>5} beats'.format(ch,(tick2second(sum(m.time for m in track),480,t)*1000000)/t))
            dic[ch]=round((tick2second(sum(m.time for m in track),480,t)*1000000)/t,3)
            i-=1
        elif char=='t':
            incr()
            while char.isdigit():
                ddump+=char
                incr()
            i-=1
        i+=1
    if exe or export:name=string.splitlines()[0]+'.mid'
    if exe:
        cachedir='.cache/'
        if not exists(cachedir):mkdir(cachedir)
        mid.save(cachedir+name)
        from os import system
        print(f'start "{exe}" {cachedir}"{name}"')
        system(f'start "{exe}" {cachedir}"{name}"')
    elif export:mid.save(export+name)
    else:return dic