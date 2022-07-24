from mido import Message,MidiFile,MidiTrack
mid=MidiFile()
track=MidiTrack()
mid.tracks.append(track)
track.append(Message('note_on',note=64,velocity=64,time=0))
track.append(Message('note_off',note=64,velocity=127,time=int(1920/8)))
track.append(Message('note_on',note=65,velocity=64,time=0))
track.append(Message('note_off',note=65,velocity=127,time=int(1920/8)))
mid.save('new_song.mid')