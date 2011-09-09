import os

def hostinfo():
    data = {}
    data['os'], data['hostname'], data['kernel'], data['kernelcomp'], data['arch'] = os.uname()
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

def mounts():
    data = {}
    filename = '/proc/mounts'
    if os.path.isfile(filename):
        for line in [ line.strip().split() for line in open(filename).readlines() ]:
            if len(line) > 3 and line[0] not in ['none', 'rootfs']:
                data[line[1]] = {
                    'fstype': line[2],
                    'device': line[0]
                }
                try:
                    stat = os.statvfs(line[1])
                except Exception, e:
                    print "Exception on fs: %s (%s)" % (line[1], str(e))
                else:
                    data[line[1]].update({
                        'f_blocks': stat.f_blocks,
                        'f_bfree': stat.f_bfree,
                        'f_bavail': stat.f_bavail,
                        'f_files': stat.f_files,
                        'f_ffree': stat.f_ffree,
                        'f_favail': stat.f_favail,
                    })
    return data

ALL = [ hostinfo, cpuinfo, meminfo, mounts ]
