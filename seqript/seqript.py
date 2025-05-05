
# -*- coding: UTF-8 -*-


from typing import Union, Optional, Generic, TypeVar
from typing import Iterable, Iterator, AsyncIterator
from typing import Tuple, List, Set, Dict, Any
from typing import Callable

import os
import time
import shlex
from pathlib import Path
from threading import Thread
from subprocess import Popen



def _nop(
    seqript         : "Seqript",
    nop             : Any                   = None,
):
    pass


def _seq(
    seqript         : "Seqript",
    seq             : List,
):
    for _task in seq:
        seqript(**_task)


def _par(
    seqript         : "Seqript",
    par             : List,
):
    def _run(**_task):
        seqript(**_task)
    threads = [Thread(target=_run, kwargs=_task) for _task in par]
    for _thread in threads:
        _thread.start()
    for _thread in threads:
        _thread.join()


def _comment(
    seqript         : "Seqript",
    comment         : str                   = "",
):
    print(f"[{seqript.name}]: {comment}")


def _sleep(
    seqript         : "Seqript",
    sleep           : int                   = 0,
):
    print(f"[{seqript.name}]: Start sleep {sleep}s.")
    time.sleep(sleep)
    print(f"[{seqript.name}]: Done sleep {sleep}s.")


def _cmd(
    seqript         : "Seqript",
    cmd             : List[str],
):
    cwd = cwd or Path.cwd()
    env = env or dict()
    if isinstance(cmd, str):
        cmd = shlex.split(cmd)
    _proc = Popen(
        args=cmd,
        cwd=str(cwd),
        env=os.environ | env,
    )
    _proc.wait()


class Seqript:

    _DEFAULT_ENGINES = {
        "nop": _nop,
        "seq": _seq,
        "par": _par,
        "comment": _comment,
        "sleep": _sleep,
        "cmd": _cmd,
    }

    def __init__(
        self,
        name        : str                   = None,
        cwd         : Path                  = None,
        env         : Dict[str, str]        = None,
        engines     : Dict[str, Callable]   = _DEFAULT_ENGINES,
    ):
        self.name = name
        self.cwd = cwd or Path.cwd()
        self.env = env or dict()
        self.engines = engines or dict()

    def __call__(self, **kwargs):
        for _k, _call in self.engines.items():
            if _k in kwargs:
                seqript = Seqript(
                    name = f"{self.name}.{kwargs.pop("name", f"*{_k}")}",
                    cwd = self.cwd / kwargs.pop("cwd", ""),
                    env = self.env | kwargs.pop("env", {}),
                    engines = self.engines,
                )
                try:
                    _call(seqript, **kwargs)
                except Exception as e:
                    # TODO: Error handling
                    pass
                return

