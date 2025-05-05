
# -*- coding: UTF-8 -*-


import os
import json
from seqript.seqript import Seqript



PATH_ROOT = os.path.dirname(os.path.abspath(__file__))
FILE_SEQRIPT = os.path.join(PATH_ROOT, "test_seqript.json")

seqript = Seqript(
    name = "test",
    cwd = None,
    env = None,
)

with open(FILE_SEQRIPT, "r") as f:
    _seqript = json.load(f)

seqript(**_seqript)

