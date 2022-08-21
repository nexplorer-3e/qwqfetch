from __future__ import annotations
from platform import release
from .. import globals


def get() -> dict[str, str]:
    sys_name = globals.get(["platform"])[0]["name"]
    if sys_name == "Linux":
        kernel = release()
    elif sys_name == "Darwin":
        from distro import version
        kernel = f"Darwin {version()}"
    elif sys_name == "Windows":
        from ..tools import get_wmic
        kernel = f"NT {get_wmic('os get version')}"
    else:
        kernel = ""
    return {'Kernel': kernel}
