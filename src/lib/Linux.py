import os
import socket

def hostinfo():
    data = {}
    data['hostname'] = socket.gethostname()
    return data

def cpuinfo():
    data = {}
    filename = '/proc/cpuinfo'
    if os.path.isfile(filename):
        for line in [ line.replace("\t", "").strip().split(":") for line in open(filename).readlines() ]:
            if len(line) == 2:
                data[line[0]] = line[1]
    return data

def meminfo():
    data = {}
    filename = '/proc/meminfo'
    if os.path.isfile(filename):
        for line in [ line.replace("\t", "").strip().split(":") for line in open(filename).readlines() ]:
            if len(line) == 2:
                data[line[0]] = line[1].strip()
    return data

ALL = [ hostinfo, cpuinfo, meminfo ]
