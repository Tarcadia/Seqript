
# -*- coding: UTF-8 -*-


from typing import List

import os
import shlex
from subprocess import Popen



def cmd(
    seqript,
    cmd             : List[str],
):
    if isinstance(cmd, str):
        cmd = shlex.split(cmd)
    _proc = Popen(
        args=cmd,
        cwd=str(seqript.cwd),
        env=(os.environ | seqript.env),
    )
    _proc.wait()

