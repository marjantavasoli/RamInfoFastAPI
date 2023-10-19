from pathlib import Path
import time
import threading
import re
import sys
from database import RamInfo


def get_ram_info():
    if sys.platform == 'linux':
        return get_linux_ram_info()
    elif sys.platform == 'win32':
        return get_windows_ram_info()
    elif sys.platform == "macos":
        return get_macos_ram_info()
    else:
        raise NotImplementedError()


def get_linux_ram_info():
    total, free, available = 0, 0, 0
    import sys
    print(sys.platform)
    with Path("/proc/meminfo").open() as fin:
        for line in fin.readlines():
            if line.startswith("MemTotal:"):
                total = int(re.search(r"(?<=:)(.*)(?=kB)", line).group())

            elif line.startswith("MemFree:"):
                free = int(re.search(r"(?<=:)(.*)(?=kB)", line).group())

            elif line.startswith("MemAvailable:"):
                available = int(re.search(r"(?<=:)(.*)(?=kB)", line).group())

    return total, free, available - free


def get_windows_ram_info():
    raise NotImplementedError()


def get_macos_ram_info():
    raise NotImplementedError()


def insert_ram_info(seconds=60):
    while True:
        total, free, used = get_ram_info()
        ram_info = RamInfo(total=total, free=free, used=used)
        ram_info.add()
        time.sleep(seconds)


def run_insert_ram_info(seconds=60):
    thread = threading.Thread(target=insert_ram_info, args=(seconds,))
    thread.start()


def get_last_ram_information(number: int):
    return [ri.to_dict() for ri in RamInfo.get_last(int(number))]
