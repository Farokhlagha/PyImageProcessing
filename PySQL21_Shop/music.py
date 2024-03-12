# https://github.com/mdoege/PySynth
# in terminal
# cd ..
# git clone https://github.com/mdoege/PySynth.git
# cd PySynth
# python setup.py install

import pysynth as ps

notes = [("c5", 4), ("e5", 4), ("g5", 4), ("c6", 4), ("g5", 4), ("e5", 4),
         ("c5", 4), ("g4", 4), ("c5", 4), ("e5", 4), ("g5", 4), ("c6", 4),
         ("g5", 4), ("e5", 4), ("c5", 4), ("g4", 4)]

ps.make_wav(notes, fn = "music.wav")