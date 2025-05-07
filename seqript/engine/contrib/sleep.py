
# -*- coding: UTF-8 -*-


import time



def sleep(
    seqript,
    sleep           : int                   = 0,
):
    print(f"[{seqript.name}]: Start sleep {sleep}s.")
    time.sleep(sleep)
    print(f"[{seqript.name}]: Done sleep {sleep}s.")


