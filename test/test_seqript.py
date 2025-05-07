
# -*- coding: UTF-8 -*-


import os
import json

from seqript.seqript import Seqript
import seqript.engine
import seqript.engine.contrib



PATH_ROOT = os.path.dirname(os.path.abspath(__file__))
FILE_SEQRIPT = os.path.join(PATH_ROOT, "test_seqript.json")
ENGINES = Seqript._DEFAULT_ENGINES | {
    "sleep": seqript.engine.contrib.sleep,
    "comment": seqript.engine.contrib.comment,
}

seqript = Seqript(
    name = "test",
    cwd = None,
    env = None,
    engines = ENGINES,
)

with open(FILE_SEQRIPT, "r") as f:
    _seqript = json.load(f)

seqript(**_seqript)

