
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
    nop             : Any                   = None,
    name            : str                   = "",
    cwd             : Path                  = None,
    env             : Dict[str, str]        = None,
    engines         : Dict[str, Callable]   = None,
):
    pass


def _seq(
    seq             : List,
    name            : str                   = "",
    cwd             : Path                  = None,
    env             : Dict[str, str]        = None,
    engines         : Dict[str, Callable]   = None,
):
    for _task in seq:
        seqript = Seqript(
            name = name,
            cwd = cwd,
            env = env,
            engines = engines,
        )
        seqript(**_task)


def _par(
    par             : List,
    name            : str                   = "",
    cwd             : Path                  = None,
    env             : Dict[str, str]        = None,
    engines         : Dict[str, Callable]   = None,
):
    def _run(**_task):
        seqript = Seqript(
            name = name,
            cwd = cwd,
            env = env,
            engines = engines,
        )
        seqript(**_task)
    threads = [Thread(target=_run, kwargs=_task) for _task in par]
    for _thread in threads:
        _thread.start()
    for _thread in threads:
        _thread.join()


def _comment(
    comment         : str                   = "",
    name            : str                   = "",
    cwd             : Path                  = None,
    env             : Dict[str, str]        = None,
    engines         : Dict[str, Callable]   = None,
):
    print(f"[{name}]: {comment}")


def _sleep(
    sleep           : int                   = 0,
    name            : str                   = "",
    cwd             : Path                  = None,
    env             : Dict[str, str]        = None,
    engines         : Dict[str, Callable]   = None,
):
    time.sleep(sleep)
    print(f"[{name}]: Sleep {sleep}ms.")


def _cmd(
    cmd             : List[str],
    name            : str                   = None,
    cwd             : Path                  = None,
    env             : Dict[str, str]        = None,
    engines         : Dict[str, Callable]   = None,
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
                if "name" in kwargs and kwargs['name']:
                    kwargs['name'] = f"{self.name}.{kwargs['name']}"
                else:
                    kwargs['name'] = f"{self.name}.*{_k}"
                if "cwd" in kwargs and kwargs["cwd"]:
                    kwargs["cwd"] = self.cwd / kwargs["cwd"]
                if "env" in kwargs and kwargs["env"]:
                    kwargs["env"] = self.env | kwargs["env"]
                kwargs["engines"] = self.engines
                try:
                    _call(**kwargs)
                except Exception as e:
                    # TODO: Error handling
                    pass
                return

