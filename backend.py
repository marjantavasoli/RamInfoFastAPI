from pathlib import Path
import time
import threading
import re
import sys
from database import RamInfo


def get_ram_info():
    """
    this method returns memory information of linux systems
    :return:
    total: int
    free: int
    used: int
    """
    total, free, buffers, cached = 0, 0, 0, 0
    with Path("/proc/meminfo").open() as fin:
        for line in fin.readlines():
            if line.startswith("MemTotal:"):
                total = get_numbers_meminfo_line(line)
            elif line.startswith("MemFree:"):
                free = get_numbers_meminfo_line(line)
            elif line.startswith("Buffers:"):
                buffers = get_numbers_meminfo_line(line)
            elif line.startswith("Cached:"):
                cached = get_numbers_meminfo_line(line)
    return total, free, total - free - buffers - cached


def get_numbers_meminfo_line(line):
    """
    this method gets one line of /proc/meminfo and return the number included in MB
    :param
    line:
    :return:
    a number in MB
    """
    match = re.search(r"(?<=:)(.*)(?=kB)", line)
    if match is not None:
        return int(match.group()) // 1024
    return 0


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
    """
    this method get number of last minutes and return ram information for each minute
    :param
    number: int
    :return:
    a json including list of RamInfo objects
    """
    return [ri.to_dict() for ri in RamInfo.get_last(int(number))]
