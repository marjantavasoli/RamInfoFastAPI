from pathlib import Path

with Path("/proc/meminfo").open() as fin:
    line = fin.readline()
    if line.startswith("MemTotal:"):
        print(int(line[9:-3]))