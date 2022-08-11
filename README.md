# L.O.V.
My advanced MML inspired golfing language (in progress): Lengh, Octave, Velocity / Volume. I do need a better name.

## What?
LOV. This is a lighter Blip interpreter designed to send midi messages to a file and eventually play it on a sound system built in Python sending it to a local (virtual) loopback MIDI device like <a href="https://www.tobias-erichsen.de/software/loopmidi.html">LoopMIDI</a> for exemple, or just to open it with a midi player / editor.

## How?
This fullscreen highly-customisable window will allow you to directly interact with your code, opening docs and exporting to midi. There are help balloons here and there, but I'll explain the bases.

Among your side bar buttons, there is a settings button that opens a window. From there do what you want with the style settings, you can save it in the 'preferences' file or apply it directly to the active window. Note that these are two different actions, you won't be saving your preferences by clicking 'Apply'.
What you want to do then is to input your paths:
- your source directory - where you'll put your text files with code;
- your export directory - you'll export midi files there;
- your Exe directory - the program where this path leads will be feed your code in midi format when you click (or tap) on 'Run'.

For the code part, it's mostly inspired by BeepComp but with some differences: all letters are written as small letters as length and octave symbols. Big letters means sharp notes. Some don't exist, like `B`, that's just a `c`! Yeah, real musicians will hate it but it's fine and makes everything more simple. I'm a simple man. Also, the volume symbols are `+` and `-` instead of `^` and `_`, and loops are made of parentheses. You can just look in the interpreter (`lov.py`), it's really not that complex and more of a human way of going through the code.

However(!), you still need to have a title in the first line and a tempo indicator in the second one (`t120` i.e.) for your document to be saved without errors. I will try to work a little on this but it removes a file browsing barrier and is thus kinda convenient from this point.

## Shortcuts
There is a list of bindings in `ide.py`, here is it from the first release version (t'was at line 288):
```py
    w.bind('<Control-q>',ex)
    w.bind('<Control-r>',restart)
    w.bind('<Control-n>',new)
    w.bind('<Control-o>',load)
    w.bind('<Control-s>',save)
    w.bind('<F5>',play)
    w.bind('<Shift-F5>',export)
    w.bind('<Control-Shift-P>',settings)
```
Don't hesitate to edit these to your tastes.

## Where does icons come from??
These funny little icons are actually UNICODE! They're called Dingbats and are pretty cute. I put in the repo `U2700.pdf` right from <a href="http://www.unicode.org/charts/">unicode.org</a> with all these dingbats and their corresponding unicode code things. I really hope they come right on your screen, if not you can always modify their custom font `sF` in `ide.py` after the bindings. The codes are written before the bindings, in Python unicode chars are written `\u****` so you can replace the icons as well.

## Logging
I put a smart home-made logging system in the ide wich displays and times everything in the console. The release is window-based and no log will be available, you need the Python script to have it. Just launch `ide.py`.

## Call me babee!
I think that's it. If you have something to say, email me at my funny alias `breee@duck.com`. Feel free to ask for help, report bugs or just say hello!
I built this thing for me but mostly for you. And you can improve it by finding bugs and bringing them to me. Note that a lot of warnings and errors or just weird mechanics you can stumble upon aren't always bugs, I actually mistook several times simple mistakes for fat bugs.













## TO-DO
- [x] Link the IDE to the interpreter.
- [x] Hovertips
- Finish the status bar:
  - [x] cursor;
  - [x] lengh;
  - [x] channels lenghs in beats (from interpreter);
  - [x] alive time;
  - [x] current time;
  - [x] perfect packing.
- [x] Clean Settings window widgets' definitions
- Finish side buttons actions:
  - [x] close;
  - [x] restart;
  - [x] open;
  - [x] new;
  - [x] save /!\REWRITE/!\;
  - [x] run;
  - [x] export;
  - [x] settings.
- Finish the Settings window:
  - [x] customisation settings;
  - [x] folder settings;
  - [ ] ~~interpreter settings? (output, think about easy command detection insertion in code)~~
  - [x] clean up bottom part.